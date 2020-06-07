from django.db import models
from django.utils import timezone
# Create your models here.
from django.db import models
import uuid
import datetime
from django.utils import timezone
from django.contrib.auth.hashers import make_password, check_password


class List(models.Model):
    list_name = models.CharField(max_length=500, null=False, blank=False)
    created = models.DateTimeField(default=datetime.datetime.now(), null=False)

class Task(models.Model):
    list_name = models.CharField(max_length=500, null=False, blank=False)
    task_name = models.CharField(max_length=500, null=False, blank=False)
    task_desc = models.CharField(max_length=4000, null=True, blank=True)
    due_date = models.DateField(default=timezone.now, null= False)
    label = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=100, null=True, blank=True)
    priority = models.CharField(max_length=100, null=True, blank=True)


class UserManager(models.Manager):
    def get_queryset(self):
        return super(UserManager, self).get_queryset()


class User(models.Model):
    email = models.EmailField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=257, blank=False, null=False)
    password = models.CharField(max_length=257, blank=False, null=False)
    expiry_window = models.IntegerField(default=3600)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    objects = UserManager()

    def set_password(self, password):
        self.password = make_password(password=password, hasher='default')

    def verify_password(self, password):
        return check_password(password=password, encoded=self.password, preferred='default')

    def is_authenticated(self):
        return True

def generate_id():
    """
    Generates unique id used as token in authentication
    """
    return uuid.uuid4().hex + str(timezone.now().microsecond)


# class AuthTokens(models.Model):
#     """
#     Represents token object used for authorization in protected APIs to be used by third parties.
#     """
#
#     id = models.CharField(max_length=128, default=generate_id, primary_key=True)
#     client = models.ForeignKey(to=ExternalClient, on_delete=models.SET_NULL, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     modified_at = models.DateTimeField(auto_now=True)
