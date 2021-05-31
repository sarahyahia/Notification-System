from django.shortcuts import render
from django.views.generic import (ListView)
from .models import Notification

class NotificationListView(ListView):
    model = Notification
    context_object_name = 'notifications'
    paginate_by = 10
    template_name = 'notifications.html'
    def get_queryset(self):
        notifications = self.model.objects.filter(receiver=self.request.user) 
        
        # mark as reads if `user` is visit on this page.
        
        # notifications.update(isRead=True)
        print(notifications.all())
        return notifications

def isRead(request,id):
    notifications = Notification.objects.get(id = id)
    notifications.update(isRead=True)
    return Notification.objects.all()