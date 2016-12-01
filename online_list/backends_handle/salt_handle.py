#_*_coding:utf-8_*_
import os,sys
BaseDir = "/".join(os.path.dirname(os.path.abspath(__file__)).split("/")[:-2])
sys.path.append(BaseDir)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Catch_list.settings")
import django
django.setup()
import time
#import salt.client,salt.config
import json
from online_list import views
#from hosts import models
from django.utils import timezone
from Catch_list import settings


def salt_online_mgr_cmd(hosts,cmd_model,remot_cmd,default_args):
    #time.sleep(2)
    #print "going to run:",hosts,remot_cmd
    hosts = hosts
    cmd_model = cmd_model
    default_args = default_args
    remot_cmd = remot_cmd
    result_list = {'ip':'10.120.116.70','group':'00','appname':'oltp-center','version':'onlineTest_v6.6_20160709','stat':'online'}

    print "going to run",hosts,cmd_model,default_args,remot_cmd
    return result_list
    try:
        pass

    except Exception,e :
        print("\033[31;1m%s\033[0m" % e)
        task_result = e
        result = 'failed'

def salt_offline_mgr_cmd(hosts,cmd_model,remot_cmd,default_args):
    #time.sleep(2)
    #print "going to run:",hosts,remot_cmd
    hosts = hosts
    cmd_model = cmd_model
    default_args = default_args
    remot_cmd = remot_cmd
    result_list = {'ip':'10.120.116.71','group':'01','appname':'oltp-center','version':'onlineTest_v6.6_20160709','stat':'online'}
    #print result_list

    print "going to run",hosts,cmd_model,default_args,remot_cmd
    #return salt_offline_mgr_cmd(hosts,cmd_model,remot_cmd,default_args)
    return result_list
    try:
        pass

    except Exception,e :
        print("\033[31;1m%s\033[0m" % e)
        task_result = e
        result = 'failed'
    #here--------------now
    """
    bind_host = host_obj
    s = paramiko.SSHClient()
    s.load_system_host_keys()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        if bind_host.host_user.auth_type == 'ssh-password':
            s.connect(bind_host.host.ip_addr,
                      int(bind_host.host.port),
                      bind_host.host_user.username,
                      bind_host.host_user.password,
                      timeout=5)
        else:#rsa_key
            pass
            '''
            key = paramiko.RSAKey.from_private_key_file(settings.RSA_PRIVATE_KEY_FILE)
            s.connect(bind_host.host.ip_addr,
                      int(bind_host.host.port),
                      bind_host.host_user.username,
                      pkey=key,
                      timeout=5)
            '''
        stdin,stdout,stderr = s.exec_command(task_content)
        result = stdout.read(),stderr.read()
        cmd_result = filter(lambda x:len(x)>0,result)[0]
        result = 'success'
        #print cmd_result

    except Exception,e:
        print("\033[31;1m%s\033[0m" % e)
        cmd_result = e
        result = 'failed'

    #for line in cmd_result:
    #    print line,
"""