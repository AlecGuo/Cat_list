#!/usr/bin/env python
#-*- coding:utf-8 -*-
from django.shortcuts import render_to_response
from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from django.http import JsonResponse
# Create your views here.
import json
import task


def online_index(request):
    host_list=[
               {'ip':'xxx','group':'00','appname':'xxx','version':'xxx','stat':'online'},
    ]
    #tas_obj = task.Task(request)
    #host_list = tas_obj.handle()
    return  render_to_response('online_list/online_mgr.html',{'host_list':host_list})
    #print host_list
def online_mgr(request):

    task_type = request.GET.get("task_type")
    print task_type
    tas_obj = task.Task(request)
    host_list = tas_obj.handle()
    print "host_list=======",host_list
    #return  HttpResponse(json.dumps(res))
    return  HttpResponse(json.dumps(host_list))
    #print HttpResponse(json.dumps(host_list))
def offline_mgr(request):

    task_type = request.GET.get("task_type")
    print task_type
    tas_obj = task.Task(request)
    host_list = tas_obj.handle()
    print "sdfsaff",type(host_list)

    print "host_list=======",host_list
    #return  render_to_response('online_list/online_mgr.html',{'host_list':host_list})
    return JsonResponse(host_list,safe=False)
