#_*_coding:utf-8_*_

import os,sys
BaseDir = "/".join(os.path.dirname(os.path.abspath(__file__)).split("/")[:-2])
sys.path.append(BaseDir)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Catch_list.settings")
import django
django.setup()   #Django 测试依赖于 DJANGO_SETTINGS_MODULE 环境变量. 如果我们想要使用单独的 PY 脚本来测试 Django,那么应该在我们的程序开始初始化 Django 环境.否则就会报出 AppRegistryNotReady 异常.
import multiprocessing
#from hosts import models
#print models.Host.objects.all()
from django.core.exceptions import ObjectDoesNotExist
import salt_handle
from  salt_handle import salt_offline_mgr_cmd
from salt_handle import salt_online_mgr_cmd
from online_list import views
#import salt.client

def by_paramiko(task_id):
    try:
        task_obj = models.TaskLog.objects.get(id=task_id)
        pool = multiprocessing.Pool(processes=5)
        res = []
        if task_obj.task_type == 'multi_cmd':
            for h in task_obj.hosts.select_related():
                p = pool.apply_async(paramiko_handle.paramiko_ssh,args=(task_id,h,task_obj.cmd))
                res.append(p)
        elif task_obj.task_type in ('file_send','file_get'):
            for h in task_obj.hosts.select_related():
                p = pool.apply_async(paramiko_handle.paramiko_sftp,args=(task_id,h,task_obj.cmd,task_obj.task_type,task_obj.user.id))
                res.append(p)
        #for r in res:
         #   print r.get()
        pool.close()
        pool.join()

    except ObjectDoesNotExist,e:
        sys.exit(e)
def by_ansible(task_id):
    pass
def by_saltstack(task_type):
    try:
        hosts = "inside_sys_all"
        cmd_model = "cmd.run"
        remot_cmd = "[cat /etc/hosts]"
        default_args = "expr_form='nodegroup'"
        task_type = task_type
        pool = multiprocessing.Pool(processes=5)
        host_list = []
        print "by_saltstack=====",task_type
        if task_type == "online_mgr":
            p = pool.apply_async(salt_handle.salt_online_mgr_cmd,args=(hosts,cmd_model,remot_cmd,default_args))
            host_list.append(p.get())
            print "打印====p",p
        elif task_type == "offline_mgr":
            p = pool.apply_async(salt_handle.salt_offline_mgr_cmd,args=(hosts,cmd_model,remot_cmd,default_args))
            host_list.append(p.get())
            print "打印====p",p

        #for r in host_list:
        #    print r.get()

        print "host_list:",host_list
        #return list(host_list)
        #return host_list
        pool.close()
        pool.join()
        print host_list
        return host_list
    except ObjectDoesNotExist,e:
        sys.exit(e)


if __name__== '__main__':
    required_args = ['-task_type','-run_type']
    for arg in required_args:
        if not arg in sys.argv:
            sys.exit("arg [%s] is required!" % arg)
    if len(sys.argv) <5:
        sys.exit("3 arguments expected but %s given "% len(sys.argv))
    #task_id = sys.argv[sys.argv.index("-task_id") + 1 ]
    task_type = sys.argv[sys.argv.index("-task_type") + 1 ]

    #print "-===========",task_type
    run_type = sys.argv[sys.argv.index("-run_type") + 1 ]
    print "-===========",task_type,run_type
    if hasattr(__import__(__name__),run_type):
        func = getattr(__import__(__name__),run_type)
        func(task_type)
    else:
        sys.exit("Invalid run_type, only support [by_paramiko,by_ansible,by_saltstack]")



