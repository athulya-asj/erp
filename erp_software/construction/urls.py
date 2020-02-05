from django.contrib import admin
from django.urls import path,include
from construction import views


urlpatterns = [
    path('',views.index),
    path('login',views.login,name="login"),
    path('loginsubmit',views.loginsubmit,name="loginsubmit"),
    path('adminaddcontractor',views.adminaddcontractor,name="adminaddcontractor"),
    path('admin_submit_contractor',views.admin_submit_contractor,name="admin_submit_contractor"),
    path('adminaddemployee',views.adminaddemployee,name="adminaddemployee"),
    path('admin_submit_employee',views.admin_submit_employee,name="admin_submit_employee"),
    path('adminaddcontract',views.adminaddcontract,name="adminaddcontract"),
    path('admin_submit_work',views.admin_submit_work,name="admin_submit_work"),
    path('adminremovecontractor',views.adminremovecontractor,name="adminremovecontractor"),
    path('deletecontractor',views.deletecontractor,name="deletecontractor"),
    path('adminremoveemployee',views.adminremoveemployee,name="adminremoveemployee"),
    path('deleteemployee',views.deleteemployee,name="deleteemployee"),
    path('adminviewemployee',views.adminviewemployee,name="adminviewemployee"),
    path('adminviewcontractor',views.adminviewcontractor,name="adminviewcontractor"),
    path('adminviewcontractor',views.adminviewcontractor,name="adminviewcontractor"),
    path('logout',views.logout,name="logout"),
    path('contractor_view_work',views.contractor_view_work,name="contractor_view_work"),
    path('contractor_update_status',views.contractor_update_status,name="contractor_update_status"),
    path('updatestatus',views.updatestatus,name="updatestatus"),
    path('contractor_select_employee',views.contractor_select_employee,name="contractor_select_employee"),
    path('contractor_submit_employee',views.contractor_submit_employee,name="contractor_submit_employee"),
    path('employee_view_work',views.employee_view_work,name="employee_view_work"),







]
