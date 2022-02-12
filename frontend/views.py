from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib import messages
import requests

# Create your views here.

def render_login(request):
    return render(request, "login.html")

def perform_login(request):
    if request.method != "POST":
        return HttpResponse("Method not Allowed")
    else:
        username = request.POST.get("username")
        password = request.POST.get("password")
        user_obj = authenticate(request, username=username, password=password)
        if user_obj is not None:
            login(request, user_obj)
            return HttpResponseRedirect(reverse("render_home"))
        else:
            messages.error(request, "Username or Password is Invalid!")
            return HttpResponseRedirect("/")        
            
def render_home(request):
    return render(request, "dashboard/base.html")

def show_users(request):
    res=requests.get('http://127.0.0.1:8000/api/user-list/').json()
    return render(request,'dashboard/pages/users.html',{'response':res})

def render_signup(request):
    return render(request, "dashboard/modals/add_user.html")

def perform_logout(request):
    logout(request)
    return HttpResponseRedirect("/")

#VIEW FROM DATABASE
# def test_display(request):
#     book = book.objects.all()[0]
#     return render_to_response('display.html', {'book': book})
# Then your template can look like this:

# <ul>
#   <li>{{ book.title }}</li>
#   <li>{{ book.author }}</li>
# </ul>


def perform_register(request):
    full_name = request.POST.get('full_name')
    data = {
            'full_name': full_name
    }
    # JsonResponse(data)
    return JsonResponse(data)

# def render_success(request):
#     return render(request, "welcome/success.html")

# def error_404(request, exception):
#     return render(request,"error/404.html")
# def error_500(request, exception):
#     return render(request,"error/500.html")
# ERROR 500 CATCHER