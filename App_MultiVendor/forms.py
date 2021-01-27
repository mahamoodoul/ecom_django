from django.forms import ModelForm
from App_Login.models import User
from App_MultiVendor.models import VendorProfile

from django.contrib.auth.forms import UserCreationForm


# forms

class VendorProfileForm(ModelForm):
    class Meta:
        model = VendorProfile
        exclude = ('date_joined',)
