from django.urls import path, include
from . import views

urlpatterns=[
    path('',views.Category_list.as_view(), name="Categories"),
]
