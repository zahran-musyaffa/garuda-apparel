from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductForm
from main.models import Product
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import CarForm
from .models import Car
from django.http import HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST


# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get('filter', "all")
    selected_category = request.GET.get('category')

    if selected_category:
        product_list = Product.objects.filter(category=selected_category)
    elif filter_type == "all":
        product_list = Product.objects.all()
    else:
        product_list = Product.objects.filter(user=request.user)

    context = {
        'name': 'Zahran Musyaffa Ramadhan Mulya',
        'npm': '2406365401',
        'class': 'PBP KKI',
        'product_list': product_list,
        'last_login': request.COOKIES.get('last_login', 'Not Found'),
        'selected_category': selected_category or 'all',
    }
    
    return render(request, "main.html", context)

@login_required(login_url='/login')
def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product_entry = form.save(commit=False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product.html", context)

@login_required(login_url='/login')
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.increment_views()

    context = {
        'product': product
    }

    return render(request, "product_detail.html", context)

def show_xml(request):
    product_list = Product.objects.all()
    xml_data = serializers.serialize("xml", product_list)
    return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    product_list = Product.objects.all()
    data = [
        {
            'id': product.id,
            'name': product.name,
            'description': product.description,
            'category': product.category,
            'thumbnail': product.thumbnail,
            'product_views': product.product_views,
            'is_featured': product.is_featured,
            'status': product.status,
            'price': product.price,
            'user_id': product.user_id,
        }
        for product in product_list
    ]
    return JsonResponse(data, safe=False)

def show_xml_by_id(request, id):
    try:
        product = get_object_or_404(Product, pk=id)
        xml_data = serializers.serialize("xml", [product])
        return HttpResponse(xml_data, content_type="application/xml")
    except Product.DoesNotExist:
        return HttpResponse(status=404)

def show_json_by_id(request, id):
    try:
        product = Product.objects.select_related('user').get(pk=id)
        json_data = {
            'id': product.id,
            'name': product.name,
            'description': product.description,
            'category': product.category,
            'thumbnail': product.thumbnail,
            'product_views': product.product_views,
            'is_featured': product.is_featured,
            'status': product.status,
            'price': product.price,
            'user_id': product.user_id,
            'user_username': product.user.username if product.user_id else None,
        }
        return JsonResponse(json_data)
    except Product.DoesNotExist:
        return JsonResponse({'detail': 'Product not found'}, status=404)

def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

# AJAX Product CRUD
@csrf_exempt
@require_POST
def create_product_ajax(request):
    try:
        product = Product(
            user=request.user if request.user.is_authenticated else None,
            name=request.POST.get('name', ''),
            price=int(request.POST.get('price', '0') or 0),
            description=request.POST.get('description', ''),
            thumbnail=request.POST.get('thumbnail', ''),
            category=request.POST.get('category', 'jersey'),
            is_featured=(request.POST.get('is_featured') == 'on' or request.POST.get('is_featured') == 'true'),
            status=request.POST.get('status', 'available'),
        )
        product.save()
        return JsonResponse({'id': product.id}, status=201)
    except Exception as e:
        return JsonResponse({'detail': str(e)}, status=400)

@csrf_exempt
@require_POST
def update_product_ajax(request, id):
    try:
        product = get_object_or_404(Product, pk=id)
        product.name = request.POST.get('name', product.name)
        price_val = request.POST.get('price')
        if price_val is not None:
            try:
                product.price = int(price_val)
            except ValueError:
                pass
        product.description = request.POST.get('description', product.description)
        product.thumbnail = request.POST.get('thumbnail', product.thumbnail)
        product.category = request.POST.get('category', product.category)
        is_feat = request.POST.get('is_featured')
        if is_feat is not None:
            product.is_featured = (is_feat == 'on' or is_feat == 'true')
        status_val = request.POST.get('status')
        if status_val:
            product.status = status_val
        product.save()
        return JsonResponse({'updated': True})
    except Exception as e:
        return JsonResponse({'detail': str(e)}, status=400)

@csrf_exempt
@require_POST
def delete_product_ajax(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return HttpResponse(status=204)

def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form': form}
    return render(request, 'register.html', context)


def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
    else:
        form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse("main:login"))
    response.delete_cookie('last_login')
    return response

# AJAX Auth
@csrf_exempt
@require_POST
def login_ajax(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        resp = JsonResponse({'ok': True, 'username': user.username})
        resp.set_cookie('last_login', str(datetime.datetime.now()))
        return resp
    return JsonResponse({'ok': False, 'detail': 'Invalid credentials'}, status=400)

@csrf_exempt
@require_POST
def register_ajax(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        return JsonResponse({'ok': True}, status=201)
    return JsonResponse({'ok': False, 'errors': form.errors}, status=400)

@csrf_exempt
@require_POST
def logout_ajax(request):
    logout(request)
    resp = JsonResponse({'ok': True})
    resp.delete_cookie('last_login')
    return resp

def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "edit_product.html", context)


def new_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST)

        if form.is_valid():
            car_name = form.cleaned_data['name']
            car_brand = form.cleaned_data['brand']
            car_stock = form.cleaned_data['stock']
            return redirect("main:show_main")
    else:
        form = CarForm()
    return render(request, "create_card.html", {'form' : form})



        
        

    


        
        

            

