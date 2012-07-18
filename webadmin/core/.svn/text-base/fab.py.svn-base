# -*- coding: utf8 -*-
import os
import datetime
import pty
import signal
import subprocess
import re
from webadmin.core.models import Task

dirname = os.path.dirname(os.path.abspath(__file__))
catapult_dir = os.path.join(dirname, '..', '..')

func = {'setup' : '安装',
        'deploy' : '部署',
        'ideploy' : '增量部署',
        'rollback' : '回滚',
        'exterminate' : '清理',
       }

def run_task(proj, deploy, owner, version=None, flag=None):

    os.chdir(catapult_dir)
    dest = ''

    if flag == 1 and (deploy[0] == 'setup' or deploy[0] == 'ideploy' or deploy[0] == 'deploy'):
        task = subprocess.Popen('fab proj:' + proj[0] + ' ' + deploy[0] + ":" + version, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
    elif flag == 0:
        task = subprocess.Popen('fab proj:' + proj[0] + ' ' + deploy[0], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
    b = Task.objects.get(name=proj[0],flag=1)
    while 1:
            ret = subprocess.Popen.poll(task)
            if ret == 0:
                b.log = task.stdout.readlines()
                b.deploy_func = func[deploy[0]]
                dest = str(b.log)
                if flag == 0:
                    b.rev = ' '
                    b.version = ' '
                elif flag == 1 and (deploy[0] == 'setup' or deploy[0] == 'deploy'):
                    t_rev = re.search("echo '\d+' > REV", dest)
                    b.rev = t_rev.group().split('\'')[1]
                    b.version = version
                elif flag == 1 and deploy[0] == 'ideploy':
                    t_rev = re.search("echo '\d+' > REV", dest)
                    b.rev = t_rev.group().split('\'')[1]
                    b.version = version
                b.flag = 0
                b.owner = owner
                b.save()
                break
            elif ret == 1:
                b.log = task.stdout.readlines()
                b.deploy_func = func[deploy[0]]
                b.rev = 0
                b.version = 0
                b.flag = 0
                b.owner = owner
                b.save()
                return 'error'

def std_log(proj):
    global catapult_dir
    if not os.path.exists (catapult_dir + '/log/' + str(datetime.date.today())):
        os.makedirs(catapult_dir + '/log/' + str(datetime.date.today()))
    return open(catapult_dir + '/log/' + str(datetime.date.today()) + '/' + proj[0]+'.txt', 'w')

pid = None #FIXME: only for demo

def run(*args):
    master, slave = pty.openpty()
    global pid
    pid = os.fork()
    if pid == 0:
        os.close(master)
        #os.dup2(slave, 0)
        os.dup2(slave, 1)
        os.dup2(slave, 2)
        if slave > 2:
            os.close(slave)
        os.execlp(args[0], *args)
    else:
        os.close(slave)
        while 1:
            msg = os.read(master, 1024)
            if not msg:
                break
            yield msg
        os.close(master)
        os.waitpid(pid, 0)
        pid = None


def term():
    os.kill(pid, signal.SIGINT)
    return 'killed %d' % pid


def run_test(proj_name, deploy):
    dirname = os.path.dirname(os.path.abspath(__file__))
    catapult_dir = os.path.join(dirname, '..', '..')
    os.chdir(catapult_dir)

    if deploy == 'setup':
        os.system("fab proj:" + proj_name + " " + deploy)

    elif deploy == 'deploy':
        os.system("fab proj:" + proj_name + " " + deploy)

    elif deploy == 'ideploy':
        os.system("fab proj:" + proj_name + " " + deploy)
        
    elif deploy == 'exterminate':
        os.system("fab proj:" + proj_name + " " + deploy)


if __name__ == '__main__':
    for output in run_test():
        os.write(1, output)
