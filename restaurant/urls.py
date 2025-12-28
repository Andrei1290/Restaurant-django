from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import LoginForm

urlpatterns = [
    path('', views.menu_view, name='menu'),
    path('cart/', views.cart_view, name='cart'),
    
    path('login/', auth_views.LoginView.as_view(
        template_name='restaurant/login.html',
        authentication_form=LoginForm
    ), name='login'),

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('register/', views.register_view, name='register'),

    path('profile/', views.profile_view, name='profile'),

    path('add-to-cart/<int:item_id>/', views.add_to_cart, name='add_to_cart'),
    path('add-to-favorites/<int:item_id>/', views.add_to_favorites, name='add_to_favorites'),
    path('remove-from-favorites/<int:item_id>/', views.remove_from_favorites, name='remove_from_favorites'),
    path('cart/increase/<int:cart_item_id>/', views.increase_quantity, name='increase_quantity'),
    path('cart/decrease/<int:cart_item_id>/', views.decrease_quantity, name='decrease_quantity'),
    path('cart/remove/<int:cart_item_id>/', views.remove_cart_item, name='remove_cart_item'),

    path('checkout/', views.checkout_view, name='checkout'),
]
