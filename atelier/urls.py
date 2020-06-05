from django.contrib import admin
from django.urls import path
from photoatelier.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include

urlpatterns = [
    path('', home_view, name='home'),
    path('admin/', admin.site.urls),
    path('about/', about_view, name='about'),
    path('contact/', contact_view, name='contact'),
    path('register/', register_page, name='register'),
    path('order/', include('photoatelier.urls'), name='order_list'),
    path('stuff/', stuff_view, name='stuff'),
    path('login/', login_page, name='login'),
    # path('list/', include('photoatelier.urls')),

]
