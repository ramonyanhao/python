import subprocess
import tkinter.filedialog
import queue

def runas():
    cmdpath = tkinter.filedialog.askopenfilenames()
    command = 'runas /user:administrator "%s"'%cmdpath
    result = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stdin=subprocess.PIPE)
    admin = 'administrator'

    if admin.encode() in result.stdout.read():
        password = bytes('louisenie','utf-8')
        stdout,stderr = result.communicate(b'%s\n'%password)
        print(stdout.decode('utf-8'))
    else:
        subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stdin=subprocess.PIPE)



if __name__ == '__main__':
    runas()