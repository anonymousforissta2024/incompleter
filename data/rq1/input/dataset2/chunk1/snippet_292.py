#Source: https://stackoverflow.com/questions/41719307/typeerror-popen-object-is-not-callable
import subprocess, codecs

def serviceStatus(RadiaService):
    status = []
    cmd = 'sc query ' + RadiaService
    pDetails = subprocess.Popen(cmd, shell = True, stdout = subprocess.PIPE)
    for item in pDetails():
        status.append(item)
    finalStatus = b''.join(status).decode('utf-8')
    print(finalStatus)

if __name__ == '__main__':
    serviceStatus('RCA')