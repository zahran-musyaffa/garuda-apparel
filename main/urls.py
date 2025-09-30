from django.urls import path
from main.views import show_main, create_product, show_product, show_json, show_xml, show_json_by_id, show_xml_by_id, delete_product, register, login_user, logout_user, edit_product, new_car

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product/', create_product, name='create_product'),
    path('product/<str:id>/', show_product, name='show_product'),
    path('product/<str:id>/delete', delete_product, name='delete_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('product/<int:id>/edit/', edit_product, name='edit_product'),
    path('cars/new/', new_car, name='new_car')
]