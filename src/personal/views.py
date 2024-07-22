from django.shortcuts import render

# Create your views here.

def home_screen_view(request):
    print(request.headers)
    return render(request, "personal/home.html", {})

def gallery_screen_view(request):
    return render(request, "personal/gallery.html", {})