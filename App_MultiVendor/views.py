from django.shortcuts import render, HttpResponse, HttpResponseRedirect, reverse, redirect
from django.contrib.auth.decorators import login_required
from App_MultiVendor.forms import VendorProfileForm
from App_Login.forms import SignUpForm
from App_Login.models import User
from App_MultiVendor.models import VendorProfile
from App_Shop.models import Product
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, ListView, DetailView, View, TemplateView, DeleteView

# Authetication
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate

# Messages
from django.contrib import messages

# Create your views here.

@login_required
def vendorhome(request):
    return render(request, 'App_MultiVendor/home.html', context={})

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
        vendor_profile = VendorProfile(vendoruser=user,vendor_name=shop_name,address=address,is_vendor=True)
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
            user = authenticate(request, email=username, password=password)
            if user is not None:
                vendor = VendorProfile.objects.get(vendoruser=user)
                if user.is_authenticated and vendor.is_vendor:
                    login(request, user)
                    return HttpResponseRedirect(reverse('App_MultiVendor:vendorhome'))
                else:
                    return redirect('loginvendor')
            else:
                return redirect('signupvendor')
    return render(request, 'App_MultiVendor/login.html', context={'form':form})




class add_product(LoginRequiredMixin,CreateView):
    model = Product
    template_name = 'App_MultiVendor/add_product.html'
    fields = ('mainimage','name','category','preview_text','detail_text','price','old_price')
    def form_valid(self, form):
        product_obj = form.save(commit=False)
        vendor = VendorProfile.objects.get(vendoruser=self.request.user)
        product_obj.shop_info = vendor
        if vendor.is_vendor:
            product_obj.save()
            return redirect('App_MultiVendor:vendorhome')
        else:
            return redirect('App_MultiVendor:loginvendor')
