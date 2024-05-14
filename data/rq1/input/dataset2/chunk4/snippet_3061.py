#Source: https://stackoverflow.com/questions/69801765/opening-tun-interface-throws-either-io-unsupportedoperation-or-filenotfounderror
import os
import sys
import struct
import logging
import threading
import traceback
import subprocess

if sys.platform == "linux" or sys.platform == "linux2":
    import fcntl

from select import select

import spinel.util as util
import spinel.config as CONFIG

IFF_TUN = 0x0001
IFF_TAP = 0x0002
IFF_NO_PI = 0x1000
IFF_TUNSETIFF = 0x400454ca
IFF_TUNSETOWNER = IFF_TUNSETIFF + 2


class TunInterface(object):
    """ Utility class for creating a TUN network interface. """

    def __init__(self, identifier):
        self.identifier = identifier
        self.ifname = "tun" + str(self.identifier)
        self.tun = None
        self.fd = None

        platform = sys.platform
        if platform == "linux" or platform == "linux2":
            self.__init_linux()
        elif platform == "darwin":
            self.__init_osx()
        else:
            raise RuntimeError(
                "Platform \"{}\" is not supported.".format(platform))

        self.ifconfig("up")
        #self.ifconfig("inet6 add fd00::1/64")
        self.__start_tun_thread()

    def __init_osx(self):
        CONFIG.LOGGER.info("TUN: Starting osx " + self.ifname)
        filename = "/dev/" + self.ifname
        self.tun = os.open(filename, os.O_RDWR)
        self.fd = self.tun
        # trick osx to auto-assign a link local address
        self.addr_add("fe80::1")
        self.addr_del("fe80::1")



    def __init_linux(self):
        CONFIG.LOGGER.info("TUN: Starting linux " + self.ifname)
        self.tun = open("/dev/net/tun", "r+b")
        self.fd = self.tun.fileno()

        ifr = struct.pack("16sH", self.ifname, IFF_TUN | IFF_NO_PI)
        fcntl.ioctl(self.tun, IFF_TUNSETIFF, ifr)  # Name interface tun#
        fcntl.ioctl(self.tun, IFF_TUNSETOWNER, 1000)  # Allow non-sudo access


    def close(self):
        """ Close this tunnel interface. """
        if self.tun:
            os.close(self.fd)
            self.fd = None
            self.tun = None

    @classmethod
    def command(cls, cmd):
        """ Utility to make a system call. """
        subprocess.check_call(cmd, shell=True)

    def ifconfig(self, args):
        """ Bring interface up and/or assign addresses. """
        self.command('ifconfig ' + self.ifname + ' ' + args)


    def __run_tun_thread(self):
        while self.fd:
            try:
                ready_fd = select([self.fd], [], [])[0][0]
                if ready_fd == self.fd:
                    packet = os.read(self.fd, 4000)
                    if CONFIG.DEBUG_TUN:
                        CONFIG.LOGGER.debug("\nTUN: RX (" + str(len(packet)) +
                                            ") " + util.hexify_str(packet))
                    self.write(packet)
            except:
                traceback.print_exc()
                break

        CONFIG.LOGGER.info("TUN: exiting")
        if self.fd:
            os.close(self.fd)
            self.fd = None

    def __start_tun_thread(self):
        """Start reader thread"""
        self._reader_alive = True
        self.receiver_thread = threading.Thread(target=self.__run_tun_thread)
        self.receiver_thread.setDaemon(True)
        self.receiver_thread.start()