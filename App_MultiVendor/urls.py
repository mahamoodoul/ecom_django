from django.urls import path
from App_MultiVendor import views

app_name = "App_MultiVendor"

urlpatterns = [
    path('', views.vendorhome, name="vendorhome"),
    path('signupvendor/', views.sign_up_vendor, name="signupvendor"),
    path('loginvendor/', views.loginvendor, name="loginvendor"),
    path('add_product/', views.add_product.as_view(), name="add_product"),

]
