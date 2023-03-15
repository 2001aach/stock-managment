from django.urls import path

from newapp import views

urlpatterns=[
    path('',views.mainpage,name='mainpage'),
    path('adminpage',views.adminpage,name='adminpage'),
    path('user',views.user,name='user'),
    path('loginpage',views.loginpage,name='loginpage'),
    path('register',views.register,name='register'),
    path('user_view',views.user_view,name='user_view'),
    path('s_view',views.s_view,name='s_view'),
    path('addstock',views.addstock,name='addstock'),
    path('userstk_view',views.userstk_view,name='userstk_view '),
    path('stock_view',views.stock_view,name='stock_view'),
    path('delete_stock/<int:id>/',views.delete_stock,name='delete_stock'),
    path('update_stock/<int:id>/',views.update_stock,name='update_stock'),



]
