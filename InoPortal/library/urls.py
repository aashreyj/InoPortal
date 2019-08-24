from django.urls import path
from .views import LibStudentViewSet

urlpatterns = [
    path('entry/', LibStudentViewSet.as_view(
        {
            'get': 'list',
            'post': 'create'
        }
    )),
    path('entry/<str:roll>', LibStudentViewSet.as_view(
        {
            'get': 'retrieve',
            'put': 'update'
        }
    ))
]
