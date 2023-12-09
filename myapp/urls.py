from django.contrib import admin
from django.urls import path,include
from myapp.views import   send_email,order, products, detail, cart_view, return_view, add_reply, cancel_view,add_review,contact_us,contact_us_success,category,faq_list
app_name='myapp'

urlpatterns = [
    path('category/', category, name='myapp:category'),
    path('',category,name='category'),
    path('products/<int:product_id>/<slug:slug>',products,name='products'), 
    path('<int:product_id>/<slug:slug>',detail,name='detail'), 
    path('cart/',cart_view,name='cart_view'),
    path('order/',order,name='order'),
    path('success/',return_view,name='return_view'),
    path('cancel/',cancel_view,name='cancel_view'),
    path('sendmail/',send_email,name="send_email"),
    # Assuming 'add_reply' is the URL endpoint for adding replies
    path('product/<int:product_id>/add_review/', add_review, name='add_review'),
    #path('otp/<str:otp>/<str:password>/<str:email>/',otp,name='otp'),
    path('contact/', contact_us, name='contact_us'),  # Define the URL pattern for contact_us
    path('contact/success/', contact_us_success, name='contact_us_success'),  # Success page after submitting contact form
    path('faqs/', faq_list, name='faq_list'),
]
