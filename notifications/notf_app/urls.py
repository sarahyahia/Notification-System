from django.urls import path
from . import views

urlpatterns = [    
    path('show/',views.NotificationListView.as_view(), name='index'),
    path('mark/<int:id>',views.isRead, name='markAsRead')   
]