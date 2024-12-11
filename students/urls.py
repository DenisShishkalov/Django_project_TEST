from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('student_list/', views.student_list, name='student_list'),
    path('student_detail/<int:student_id>/', views.student_detail, name='student_detail'),

    path('mymodel/create/', views.MyModelCreateView.as_view(), name='mymodel_create'),
    path('mymodel/list/', views.MyModelListView.as_view(), name='mymodel_list'),
]
