#!/usr/bin/env python
#-*- coding:utf-8 -*-
from django.shortcuts import render_to_response
from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from django.http import JsonResponse
# Create your views here.
import json
import task


def online_index(request):
    host_list=[{'ip':'10.120.116.61','group':'00','appname':'oltp-center','version':'onlineTest_v6.6_20160709','stat':'online'},
               {'ip':'10.120.116.62','group':'00','appname':'oltp-befor','version':'onlineTest_v6.6_20160709','stat':'online'},
               {'ip':'10.120.116.63','group':'00','appname':'oltp-asy','version':'onlineTest_v6.6_20160709','stat':'online'},
               {'ip':'10.120.116.64','group':'00','appname':'oltp-timer','version':'onlineTest_v6.6_20160709','stat':'online'},
               {'ip':'10.120.116.65','group':'00','appname':'oltp-account','version':'onlineTest_v6.6_20160709','stat':'online'},
    ]
    #tas_obj = task.Task(request)
    #host_list = tas_obj.handle()
    return  render_to_response('online_list/online_mgr.html',{'host_list':host_list})
    #print host_list
def online_mgr(request):
    """host_list=[{'ip':'10.120.116.61','group':'00','appname':'oltp-center','version':'onlineTest_v6.6_20160709','stat':'online'},
               {'ip':'10.120.116.62','group':'00','appname':'oltp-befor','version':'onlineTest_v6.6_20160709','stat':'online'},
               {'ip':'10.120.116.63','group':'00','appname':'oltp-asy','version':'onlineTest_v6.6_20160709','stat':'online'},
               {'ip':'10.120.116.64','group':'00','appname':'oltp-timer','version':'onlineTest_v6.6_20160709','stat':'online'},
               {'ip':'10.120.116.65','group':'00','appname':'oltp-account','version':'onlineTest_v6.6_20160709','stat':'online'},
    ]"""
    task_type = request.GET.get("task_type")
    print task_type
    tas_obj = task.Task(request)
    host_list = tas_obj.handle()
    print "host_list=======",host_list
    #return  HttpResponse(json.dumps(res))
    return  HttpResponse(json.dumps(host_list))
    #print HttpResponse(json.dumps(host_list))
def offline_mgr(request):
    '''
    host_list=[{'ip':'10.120.116.71','group':'01','appname':'oltp-center','version':'onlineTest_v6.6_20160709','stat':'online'},
               {'ip':'10.120.116.72','group':'01','appname':'oltp-befor','version':'onlineTest_v6.6_20160709','stat':'online'},
               {'ip':'10.120.116.73','group':'01','appname':'oltp-asy','version':'onlineTest_v6.6_20160709','stat':'online'},
               {'ip':'10.120.116.74','group':'01','appname':'oltp-timer','version':'onlineTest_v6.6_20160709','stat':'online'},
               {'ip':'10.120.116.75','group':'01','appname':'oltp-account','version':'onlineTest_v6.6_20160709','stat':'online'},
    ]  '''
    task_type = request.GET.get("task_type")
    print task_type
    tas_obj = task.Task(request)
    host_list = tas_obj.handle()
    print "sdfsaff",type(host_list)

    print "host_list=======",host_list
    #return  render_to_response('online_list/online_mgr.html',{'host_list':host_list})
    return JsonResponse(host_list,safe=False)
