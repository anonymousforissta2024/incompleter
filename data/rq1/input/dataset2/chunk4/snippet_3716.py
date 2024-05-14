#Source: https://stackoverflow.com/questions/49377109/typeerror-missing-1-required-positional-argument-value
import os,time,pexpect,re, subprocess, smtplib
from email import encoders
from email.header import Header
from email.mime.text import MIMEText

#-----------------------------------------

dir = os.environ['HOME']
ouser = 'x02d726'
opasw = 'qwe12'
nLocalport = 7000
lookip = '127.0.0.1'
rsg_target = "rpahost0"
command = "ls -ltrh | grep tunnel | tail"
nstage = 0
mail_addr = 'cheng.huang@qq.com'
otp_file = dir + '/otplist/C591260'
otp_list = []
rsg_file = dir + '/.rsg_hosts'
known_hosts = dir + '/.ssh/known_hosts'
rsg_port = "auto"

#-----------------------------------------

def printlog(prompt):
    year, mon, mday, hour, min, sec, wday, yday, isdst = time.localtime()
    print("%04d-%02d-%02d %02d:%02d:%02d %s" % (year, mon , mday, hour, min, 
sec, prompt))

def get_egw_name(ref_arr, key):
    for oneline in ref_arr:
        if (re.search(key, oneline)):
            templine = oneline
            oneline = re.sub('^\s+|\s+$','',oneline)
            egw_ssg = re.split('\s+',oneline)[2]
            result = re.split(':',egw_ssg)[0]
            return result

def sendworker(to_addr):
    from_addr = 'itk-bj.ericsson.se'
    smtp_server = 'smtp.eamcs.ericsson.se'

    msg = MIMEText('There is no otp left ,please input new OTP list', 
'plain', 'utf-8')
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = Header(u'OTP List is Blank', 'utf-8')

    server = smtplib.SMTP(smtp_server, 25)
    #server.set_debuglevel(1)
    server.sendmail(from_addr, to_addr, msg.as_string())
    server.quit()

def ssh_cmd(port, target, user, ip, pasw, cmd ):
    printlog("=== Script Start ===")
    printlog("Monitoring via remote logon")
    time.sleep(1)
    ssh = pexpect.spawn('/usr/bin/ssh -p %s -o HostKeyAlias=%s %s@%s %s' % 
(port, target, user, ip, cmd ),timeout=6000)
    try:
        i = ssh.expect(['Password: ', 'continue connecting (yes/no)?'], 
timeout=15)
        if i == 0 :
            print(ssh.before.decode(),ssh.after.decode())
            ssh.sendline(pasw)
        elif i == 1:
            print(ssh.before.decode(),ssh.after.decode())
            ssh.sendline('yes')
            ssh.expect('Password: ')
            print(ssh.before.decode(),ssh.after.decode())
            ssh.sendline(pasw)
    except pexpect.EOF:
        print ("no connection EOF,please check RSG tunnel")
    except pexpect.TIMEOUT:
        print ("your pexpect has TIMEOUT")
    else:
        ssh.expect(pexpect.EOF)
        print (ssh.before.decode(),ssh.after().decode()) # if I disable this line, there will be no error.
        flag = ssh.before.decode()
        return flag
    ssh.close()

if __name__ == '__main__':
    if os.path.exists(os.environ['HOME'] + "/.ssh/known_hosts"):
        os.remove(known_hosts)
    else:
        pass
    label = ssh_cmd(nLocalport, rsg_target, ouser, lookip, opasw, command)
    if re.search('tunnel_check', str(label)):
        nstage = 1
    if (nstage == 0):
        printlog("Tunnel was down and  will re-establish now\n")
        rsg = open (rsg_file,'r')
        rsg_in = rsg.readlines()
        rsg.close()
        egwname = get_egw_name(rsg_in, rsg_target)
        try :
            otp = open(otp_file, 'r')
            otp_arrary = otp.readlines()
            otp.close()
            for ot in otp_arrary:
                ot = ot.strip()
                ot = ot.replace('^\s*|\s*$', '')
                otp_list.append(ot)
            otp_num = len(otp_list) + 1
            if (otp_num > 0):
                os.remove(rsg_file)
                try :
                    new_otp = otp_list[0]
                except IndexError:
                    printlog('There is no otp left ,please input new OTP list')
                    sendworker(mail_addr)
                    sys.exit()
                else:
                    out = open(rsg_file, 'w')
                    for line in rsg_in :
                        line = line.strip()
                        line = line.replace('^\s+|\s+$','')
                        if (re.match(egwname, line)):
                            temp_line = line
                            old_otp = re.split('\s+',temp_line)[5]
                            old_otp = old_otp.replace('^\s+|\s+$', '')
                            line = line.replace(old_otp, new_otp).replace('\\','')
                            printlog(line + "\n")
                        out.write(line + "\n")
                    out.close()
                    os.remove(otp_file)
                    time.sleep(1)
                    outotp = open(otp_file , 'w+')
                    i = 0
                    while (i < len(otp_list)):
                        outotp.write(otp_list[i] + "\n")
                        i += 1
                    outotp.close()
                    os.system("pkill -9 -f \"ssh\.\*-L " + str(nLocalport) + "\"")
                    os.system("sleep 10")
                    os.system("pkill -9 -f \"rtunnel\.\*-p " + str(nLocalport) + "\"")
                    os.system("nohup /opt/ericsson/itk/bin/rtunnel -d -q -g -p " + str(nLocalport) + "-rp auto " + rsg_target + " &")
                    os.system("sleep 10")
                    printlog("Kill the rtunnel process\n");
                    printlog("Tunnel is re-established again\n");
            else:
                sendworker(mail_addr)
        except IOError:
            print ("File is not accessible.")
    else:
        printlog("Tunnel OK")