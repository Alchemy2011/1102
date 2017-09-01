import os

def ssh_auto2():
    # try:
    #     os.system('rpm -qa | grep openssh')
    # except:
    #     pass
    os.system("ssh-keygen -t rsa -P ''")
    os.system("\n")
    os.system('cat ~/.ssh/id_rsa.pub >> ')