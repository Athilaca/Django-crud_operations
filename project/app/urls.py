from django.urls import path,include
from . import views

urlpatterns = [
   
    path("",views.home,name="home"),
    path("log", views.perform_login, name='login'),
    path("admin_logout",views.admin_logout,name="admin_logout"),
    path("signup",views.perform_signup,name="perform_signup"),
    path("admin_dashboard",views.admin,name="admin"),
    path("add",views.add_user,name="add"),
    path('delete/<int:id>',views.delete,name='delete'),
    path('update/<int:id>',views.update,name='update'),
    path("user_logout",views.user_logout,name="user_logout")

    
]


