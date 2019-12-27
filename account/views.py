from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

from account.models import Account, Notifications
from my_profile.models import UserProfile


# Create your views here.
def home(request):
    return render(request, "home.djhtml", {})


def login_page(request):
    if not request.user.is_authenticated:
        if request.method == 'GET':
            next = request.GET.get('next', default='/home')
            return render(request, "account/login.djhtml", {'next': next})
        else:
            username = request.POST.get('email')
            password = request.POST.get('pwd')
            next = request.POST.get('next')
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.success(request, "Login successful")
                    return redirect(next)
                else:
                    messages.error(request, "User not found")
                    return redirect('login')
            else:
                messages.error(request, "Authentication failed")
                return redirect('login')
    else:
        messages.error(request, "Already logged in")
        return redirect('home')


@login_required
def logout_page(request):
    logout(request)
    messages.success(request, "Logout successful")
    return redirect(home)


def registration_page(request):
    if request.method == 'GET':
        return render(request, "account/register.djhtml", {})
    else:
        a = Account()
        a.first_name = request.POST.get('first_name')
        a.last_name = request.POST.get('last_name')
        a.username = request.POST.get('email')
        a.email = request.POST.get('email')
        a.set_password(request.POST.get('password'))
        a.user_type = 'user'
        a.is_active = True
        a.is_staff = False
        a.is_superuser = False
        a.save()
        try:
            u = UserProfile()
            u.user = a
            u.save()
            messages.success(request, 'User registered.')
        except:
            a.delete()
            messages.error(request, 'Failed to register. Please try again')
        finally:
            return redirect(login_page)


def email_avalability(request):
    email = request.GET.get("email")
    lists = Account.objects.filter(username=email)
    if len(lists) == 1:
        return HttpResponse("false")
    else:
        return HttpResponse("true")

@login_required
def edit_details(request):
    a = Account.objects.get(pk=request.user.pk)
    if request.method =="GET":
        return render(request,'account/edit_details.djhtml',{'a': a})
    else:
        if request.POST.get('option') == "Update":
            a.first_name = request.POST.get('first_name')
            a.last_name = request.POST.get('last_name')
            a.save()
            messages.success(request, "details updated")
        elif request.POST.get('option') == "Change_password":
            if a.check_password(request.POST.get('old_password')):
                a.set_password(request.POST.get('password'))
                a.save()
                messages.success(request,"Password changed")
            else:
                messages.error(request, "Wrong password")
        return redirect('home')


@login_required
def notification(request):
    n = Notifications.objects.filter(user=request.user)
    n = n[::-1]
    return render(request,'account/notification.djhtml',{'n':n})

@login_required
def notification_count(request):
    n = Notifications.objects.filter(user=request.user)
    return HttpResponse(len(n))
