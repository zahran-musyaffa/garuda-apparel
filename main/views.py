from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Zahran Musyaffa Ramadhan Mulya',
        'npm': '2406365401',
        'class': 'PBP KKI'
    }

    return render(request, "main.html", context)