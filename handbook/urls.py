from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('catalog/ishop',views.ishop,name="ishop"),
    path('catalog/smarket',views.smarket,name='smarket'),
    path('catalog/shopping',views.shopping,name='shopping'),
    path('catalog/fshop',views.fshop,name='fshop'),
    path('catalog/icompany',views.icompany,name='icompany'),
    path('catalog/edu',views.edu,name='edu'),
    path('catalog/<int:pk>/details',views.company_detail,name='company_detail'),
    path('register',views.register,name='register'),
    path('addnew',views.addnewcomp,name='addnew'),
    path('catalog/<int:pk>/edit',views.editcompany,name='editcompany'),
]