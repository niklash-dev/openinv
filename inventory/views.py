from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import storage_item, storage_container, storage_location

ITEM_LIMIT = 300 # Hard limit for searchg results

@login_required
def inventory(request):
    query = request.GET.get('query', '')
    if query != '':
        items = storage_item.objects.filter(name__contains=query)
    else:
        items = storage_item.objects.all()
    total_items = len(items)
    items = items[:ITEM_LIMIT] # Hard limit Items
    return render(request, 'inventory.html', {'items': items, 'search': query, 'total_items': total_items})

@login_required
def container(request):
    containers = storage_container.objects.all()
    return render(request, 'container.html', {'containers': containers})

@login_required
def location(request):
    locations = storage_location.objects.all()
    return render(request, 'location.html', {'locations': locations})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('inventory')
        else:
            return render(request, 'login.html', {'error': 'Invalid login credentials'})
    if request.user.is_authenticated:
        return redirect('inventory')
    return render(request, 'login.html')

def base(request):
    return redirect('inventory')
