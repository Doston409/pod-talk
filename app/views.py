from django.shortcuts import render

# Create your views here.

def login_page(request):
        return render(request, 'login.html')

def about_page(request):
    return render(request, 'about.html')


def contact_page(request):
    return render(request, 'contact.html')

def detail_page(request):
    return render(request, 'detail_page.html')

def listing_page(request):
    return render(request, 'listing_page.html')