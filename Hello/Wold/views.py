from django.shortcuts import render

from django.http import JsonResponse, HttpResponse
import json
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate

def login(request):
    username = request.GET.get('user')
    password = request.GET.get('pwd')
    print request
    print 'username', username, 'password', password

    user = authenticate(username=username, password=password)
    if user is not None:
        # the password verified for the user
        if user.is_active:
            print("User is valid, active and authenticated")
        else:
            print("The password is valid, but the account has been disabled!")
        return JsonResponse({'status': 0, 'msg': 'successful login'})
    else:
        # the authentication system was unable to verify the username and password
        print("The username and password were incorrect.")
        return JsonResponse({'status': 1, 'msg': 'The username and password were incorrect.'})

@login_required
def show(request):
    pass