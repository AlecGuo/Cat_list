#_*_coding:utf-8_*_
import models
from django.db import transaction
from Catch_list import settings
import os,sys,json
import  subprocess

class Task(object):
    def __init__(self,request):
        self.request = request
        self.task_type = self.request.GET.get("task_type")
    def handle(self):
        if self.task_type:
            if hasattr(self,self.task_type):
                func = getattr(self,self.task_type)
                print func
                print "adasfsafasfsf---"
                return func()

            else:
                raise TypeError


    #@transaction.atomic   #作用当所有的数据创建成后统一的save一下
    def online_mgr(self):
        print '--------going to run task ---------'
        print self.request.GET
        #create task info
        #invoke backend multitask script
        p = subprocess.Popen([
            'python',
            settings.MutiTaskScript,
            '-task_type',self.task_type,
            '-run_type',settings.MutiTaskRunType,
        ],preexec_fn=os.setsid,stdout=subprocess.PIPE)
        print '------>pid:',p.pid

        print type(p)
        print "9999999",p.stdout.read()
        #return {'task_id':task_obj.id}
    def offline_mgr(self):
        print '--------going to run task ---------'
        print self.request.GET
        #create task info

        #invoke backend multitask script
        p = subprocess.Popen([
            'python',
            settings.MutiTaskScript,
            '-task_type',self.task_type,
            '-run_type',settings.MutiTaskRunType,
        ],preexec_fn=os.setsid)
        #host_list.append(p)

        print '------>pid:',p.pid

        #return {'task_id':task_obj.id}
        #从数据库提取结果数据
    def get_task_result(self):
        #task_id = self.request.GET.get('task_id')
        if task_id:
            res_list = models.TaskLogDetail.objects.filter(child_of_task_id=task_id)
            return list(res_list.values('id',
                                        'bind_host__host__hostname',
                                        'bind_host__host__ip_addr',
                                        'bind_host__host_user__username',
                                        'date',
                                        'event_log',
                                        'result',
                                        ))
