from django.urls import path
from main.views import show_main, create_news, show_news, show_json, show_xml, show_json_by_id, show_xml_by_id, delete_news

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-news/', create_news, name='create_news'),
    path('news/<str:id>/', show_news, name='show_news'),
    path('news/<str:id>/delete/', delete_news, name='delete_news'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
]