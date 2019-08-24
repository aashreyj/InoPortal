from django.urls import path
from .views import PermissionViewSet, AttendanceViewSet

urlpatterns = [
    path('attendance/', AttendanceViewSet.as_view({
        'get': 'list'
    })),
    path('attendance/<str:roll>/', AttendanceViewSet.as_view({
        'get': 'retrieve',
        'put': 'update'
    })),
    path('permission/', PermissionViewSet.as_view({
        'get': 'list'
    })),
    path('permission/<str:roll>', PermissionViewSet.as_view({
        'get': 'retrieve',
        'put': 'update'
    }))
]
