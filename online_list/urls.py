#_*_coding:utf-8_*_
from django.conf.urls import url

import views

urlpatterns = [
     url("^$", views.online_index, name="online_index"),
     url("^online_mgr/$", views.online_mgr, name="online_mgr"),
     url("^offline_mgr/$", views.offline_mgr, name="offline_mgr"),
     #url("^multi_file_transfer/$", views.multi_file_transfer, name="multi_file_transfer"),
     #url("^multi_cmd/$", views.multi_cmd, name="multi_cmd"),
     #url("^submit_task/$", views.submit_task, name="submit_task"),
     #url("^get_task_result/$", views.get_task_result, name="get_task_result"),
     #url("^file_upload/$", views.file_upload, name="file_upload"),

]