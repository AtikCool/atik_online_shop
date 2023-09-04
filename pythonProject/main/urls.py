from django.urls import path
from . import views
app_name = 'main'
urlpatterns = [
    path('menu/category/<str:slug>', views.menu, ),
    path('', views.main, name='main'),
    path('menu', views.menu, name='menu'),
    path('menu/<str:slug>', views.detail, name='detail'),
    path('baskets/add/<int:product_id>/', views.basket_add, name='basket_add'),
    path('baskets/remove/<int:basket_id>', views.basket_remove, name='basket_remove'),
    path('menu/page/<int:page>/', views.menu,  name='paginator')

]