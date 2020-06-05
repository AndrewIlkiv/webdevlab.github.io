from django.urls import path
from .views import OrderList, TaskDelete

urlpatterns = [
    path('', OrderList.as_view(), name='order_list'),
    path('<str:id>/delete/', TaskDelete.as_view(), name='order_delete')

]