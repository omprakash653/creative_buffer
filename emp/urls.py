from django.contrib import admin
from django.urls import path,include
from .views import *
# from emp import views

urlpatterns=[
    path("home/",emp_home),
    path("add-emp/",add_emp),
    path("delete-emp/<int:emp_id>",delete_emp),
    path("update-emp/<int:emp_id>",update_emp),
    path("do-update-emp/<int:emp_id>",do_update_emp),
    path('user_login', user_login, name='login'),
    path('user_signup', user_signup, name='signup'),
    path("user_logout", user_logout, name= "logout"),
]