from django.urls import path
from .views import AttendanceViewSet

urlpatterns = [
    path('attendance/', AttendanceViewSet.as_view({
        'get': 'list'
    })),
    path('attendance/<str:roll>/', AttendanceViewSet.as_view({
        'get': 'retrieve',
        'put': 'update'
    }))
]
