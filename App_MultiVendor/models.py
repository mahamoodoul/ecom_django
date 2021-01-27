from django.db import models

# To Create a Custom User Model and Admin Panel

from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils.translation import ugettext_lazy

# To automatically create one to one objects

from django.db.models.signals import post_save
from django.dispatch import receiver
from App_Login. models import User

# Create your models here.

class VendorProfile(models.Model):
    vendor_name = models.CharField(max_length=264)
    address = models.TextField(max_length=300)
    vendoruser = models.OneToOneField(User, on_delete=models.CASCADE,related_name='vendor_info')
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.vendor_name + "'s Profile"

    def is_fully_filled(self):
        fields_names = [f.name for f in self._meta.get_fields()]

        for field_name in fields_names:
            value = getattr(self, field_name)
            if value is None or value=='':
                return False
        return True
