from django.shortcuts import render, HttpResponse, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from App_MultiVendor.forms import VendorProfileForm
from App_Login.forms import SignUpForm
from App_Login.models import User
from App_MultiVendor.models import VendorProfile

# Authetication
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate

# Messages
from django.contrib import messages

# Create your views here.


def vendorhome(request):
    return HttpResponse("1")

def sign_up_vendor(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        shop_name = request.POST.get('shop_name')
        address = request.POST.get('address')
        user = User.objects._create_user(
            email=email,
            password= password
        )
        user.set_password(password)
        vendor_profile = VendorProfile(vendoruser=user,vendor_name=shop_name,address=address)
        vendor_profile.save()
        messages.success(request, "Account Created Successfully!")
        return HttpResponseRedirect(reverse('App_MultiVendor:loginvendor'))
    return render(request, 'App_MultiVendor/sign_up.html', context={})


def loginvendor(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = VendorProfile.objects.get(email= username, password= password)
            if user is not None:
                login(request, user)
                # return HttpResponse("Loged in")
                return HttpResponseRedirect(reverse('App_MultiVendor:vendorhome'))
    return render(request, 'App_MultiVendor/login.html', context={'form':form})
