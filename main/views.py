from django.shortcuts import render, redirect, get_object_or_404
from main.forms import NewsForm
from main.models import News
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse



# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get('filter',"all")
    if filter_type == "all":
        product_list = News.objects.all()
    else:
        product_list = News.objects.filter(user=request.user)

    context = {
        'name': 'Zahran Musyaffa Ramadhan Mulya',
        'npm': '2406365401',
        'class': 'PBP KKI',
        'product_list': product_list,
        'last_login': request.COOKIES.get('last_login', 'Not Found'),
    }
    
    return render(request, "main.html", context)

@login_required(login_url='/login')
def create_product(request):
    form = NewsForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product_entry = form.save(commit=False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product.html", context)

@login_required(login_url='/login')
def show_product(request, id):
    product = get_object_or_404(News, pk=id)
    product.increment_views()

    context = {
        'product': product
    }

    return render(request, "product_detail.html", context)

def show_xml(request):
    news_list = News.objects.all()
    xml_data = serializers.serialize("xml", news_list)
    return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    news_list = News.objects.all()
    json_data = serializers.serialize("json", news_list)
    return HttpResponse(json_data, content_type="application/json")


def show_xml_by_id(request, news_id):
    try:    
        data = News.objects.filter(pk=news_id)
        xml_data = serializers.serialize("xml", data)
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
    except News.DoesNotExist:
        return HttpResponse(status=404)

def show_json_by_id(request, news_id):
    try:    
        data = News.objects.filter(pk=news_id)
        json_data = serializers.serialize("json", data)
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    except News.DoesNotExist:
        return HttpResponse(status=404)

def delete_product(request, id):
    news = get_object_or_404(News, pk=id)
    if request.method == "POST":
        news.delete()
    return redirect('main:show_main')

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
   