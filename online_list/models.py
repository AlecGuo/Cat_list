#_*_coding:utf-8_*_
from __future__ import unicode_literals

from django.db import models
# Create your models here.


class TaskLog(models.Model):
    #end_time = models.DateTimeField(null=True,blank=True)
    #task_type_choices = (('multi_cmd',"CMD"),('file_send',"批量发送文件"),('file_get',"批量下载文件"))
    #task_type = models.CharField(choices=task_type_choices,max_length=50)
    #user = models.ForeignKey('UserProfile')
    #hosts = models.ManyToManyField('BindHostToUser')
    #expire_time = models.IntegerField(default=30)
    #task_pid = models.IntegerField(default=0)
    ip_addr = models.GenericIPAddressField(unique=True)
    start_time = models.DateTimeField(auto_now_add=True)
    ip_addr = models.GenericIPAddressField(unique=True)
    app_group = models.CharField(max_length=64,blank=True,null=True)
    online_apps = models.TextField()
    apps_version = models.TextField()
    stat = models.CharField(max_length=64,blank=True,null=True)
    task_id = models.CharField(max_length=64,blank=True,null=True)
    def __unicode__(self):
        return "ip_addr:%s stat:%s" %(self.ip_addr,self.stat)
    class Meta:
        verbose_name = u'服务列表获取'
        verbose_name_plural = u'服务列表获取'
