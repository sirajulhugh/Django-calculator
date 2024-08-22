
from django.urls import path,include
from .import views

urlpatterns = [
    path('page1',views.page1,name="page1"),
    path('contactus',views.page2,name="page2"),
    path('',views.page3,name="page3"),
    path('page4',views.page4,name="page4"),
    path('sum',views.sum,name="sum"),
    path('anssum',views.anssum,name="anssum"),
    path('calculator',views.calculator,name="calculator"),
    path('calcu',views.calcu,name="calcu")

    
]