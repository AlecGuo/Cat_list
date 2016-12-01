from django.shortcuts import render,HttpResponseRedirect,HttpResponse
#from django.contrib.auth import authenticate,login,logout
#from django.contrib.auth.decorators import login_required
#from django.views.decorators.csrf import csrf_exempt
import json

def index(request):
    return  HttpResponseRedirect('online_list/')


