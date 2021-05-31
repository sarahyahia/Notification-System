from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

# class User(models.Model):
#     name = models.CharField(max_length=200)
#     notifications = models.ManyToManyField(Notification)
#     isRead = models.BooleanField(default=False)



class Notification(models.Model):
    title = models.CharField(max_length=256)
    msg = models.TextField()
    isRead = models.BooleanField(_('Is read?'), default=False)
    receiver = models.ForeignKey(User, related_name='notification_receiver', on_delete=models.DO_NOTHING)
    
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.msg}"

    class Meta:
        verbose_name_plural = _('notifications')
        ordering = ['created']