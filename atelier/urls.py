

from django.contrib import admin
from django.urls import path
from photoatelier.views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', home_view, name='home'),
    path('admin/', admin.site.urls),
    path('about/', about_view, name='about'),
    path('contact/', contact_view, name='contact'),
    path('register/', register_view, name='register'),
    path('order/', order_view, name='order'),
    path('stuff/', stuff_view, name='stuff'),
]
