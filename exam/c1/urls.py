from django.urls import path
from.import views
urlpatterns=[path('',views.home,name='home'),
path('admin0',views.admin0,name='admin0'),
path('admin1',views.admin1,name='admin1'),
path('user0', views.user0, name='user0'),
path('user1', views.user1, name='user1'),
path('user2',views.user2,name='user2'),

path('user4',views.user4,name='user4'),
path('product7', views.product7, name='product7'),
path('viewadminproduct', views.viewadminproduct, name='viewadminproduct'),
path('productregister', views.productregister, name='productregister'),
path('search1', views.search1, name='search1'),
path('adminsearch1', views.adminsearch1, name='adminsearch1'),

path('login', views.login, name='login'),

path('adminlogin', views.adminlogin, name='adminlogin'),
path('adminlogout1', views.adminlogout1, name='adminlogout1'),
path('logout', views.logout, name='logout'),
path('add', views.add, name='add'),
path('book1', views.book1, name='book1'),
path('adminbook1', views.adminbook1, name='adminbook1'),
path('book9', views.book9, name='book9'),
path('register', views.register, name='register'),
path('homepg1', views.homepg1, name='homepg1'),
path('homepg2', views.homepg2, name='homepg2'),
path('about1', views.about1, name='about1'),
path('deleteproduct', views.deleteproduct, name='deleteproduct'),
path('viewadminfeedback', views.viewadminfeedback, name='viewadminfeedback'),

path('feedback', views.feedback, name='feedback'),
path('feed', views.feed, name='feed'),
path('viewuserdetails', views.viewuserdetails, name='viewuserdetails'),
path('userdel', views.userdel, name='userdel'),
             ]




