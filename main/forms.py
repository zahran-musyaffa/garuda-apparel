from django.forms import ModelForm
from main.models import News

class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ["name", "price", "description", "thumbnail", "category", "is_featured"]     