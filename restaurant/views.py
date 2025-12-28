from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Item, Favorite, CartItem
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
from django.contrib.auth import login

def menu_view(request):
    items = Item.objects.all()
    return render(request, 'restaurant/menu.html', {'items': items})


@login_required
def cart_view(request):
    cart_items = CartItem.objects.filter(user=request.user)
    for ci in cart_items:
        ci.total_price = ci.item.price * ci.quantity
    total_price = sum(ci.total_price for ci in cart_items)

    return render(request, 'restaurant/cart.html', {'cart_items': cart_items, 'total_price': total_price})

@login_required
def add_to_favorites(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    Favorite.objects.get_or_create(user=request.user, item=item)
    return redirect('menu')


@login_required
def add_to_cart(request, item_id):
    item = get_object_or_404(Item, id=item_id)

    # Если уже есть в корзине — увеличиваем количество
    cart_item, created = CartItem.objects.get_or_create(user=request.user, item=item)
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('menu')  # или куда хочешь перенаправлять после добавления

from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

@login_required
def increase_quantity(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id, user=request.user)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart')

@login_required
def decrease_quantity(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id, user=request.user)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart')

@login_required
def remove_cart_item(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id, user=request.user)
    cart_item.delete()
    return redirect('cart')

@login_required
def profile_view(request):
    favorites = Favorite.objects.filter(user=request.user).select_related('item')
    return render(request, 'restaurant/profile.html', {'favorites': favorites})


@login_required
def remove_from_favorites(request, item_id):
    fav = get_object_or_404(Favorite, user=request.user, item_id=item_id)
    fav.delete()
    return redirect('profile')

@login_required
def checkout_view(request):
    cart_items = CartItem.objects.filter(user=request.user)
    if request.method == 'POST':
        # Удаляем все товары из корзины после «оплаты»
        cart_items.delete()
        return render(request, 'restaurant/checkout_success.html')  # страница после оплаты

    total_price = sum(ci.item.price * ci.quantity for ci in cart_items)
    return render(request, 'restaurant/checkout.html', {'cart_items': cart_items, 'total_price': total_price})



def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('menu')
    else:
        form = RegisterForm()

    return render(request, 'restaurant/register.html', {'form': form})