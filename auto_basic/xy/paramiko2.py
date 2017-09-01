# coding:utf8
import paramiko


def main():
    host = "10.0.138.208"
    port = 22
    user = "root"
    pswd = "1"

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, port, user, pswd)
    stdin, stdout, stderr = ssh.exec_command('ifconfig')
    print stdout.read()
    ssh.close()


if __name__ == '__main__':
    try:
        main()
    except Exception, e:
        print e
