from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from payment.models import PaidUser
from datetime import date, timedelta
# Create your views here.
def paid_user(func):

    def wrapper(request,*args,**kwargs):
        p = PaidUser.objects.filter(user=request.user)
        if len(p) == 1:
            p = p[0]
            if p.expiry_date >= date.today():
                return func(request,*args,**kwargs)
            else:
                return redirect('user_payment')
        else:
            return redirect('user_payment')

    return wrapper


#@login_required(login_url= '/payment/user-upayment/')
def user_payment(request):
    p = PaidUser.objects.filter(user=request.user)
    msg = "Payment required to view this page"
    return render(request,'payment/user_payment.djhtml',{'msg':msg})



def user_upayment(request):
    if request.user.is_authenticated:
        return redirect('user_payment')
    else:
        return render(request, 'payment/user_upayment.djhtml', {})

@login_required
def user_payment_page(request):
    p = PaidUser.objects.get_or_create(user=request.user)[0]
    days_left = p.expiry_date-date.today()
    days_left = days_left.days
    print(days_left)
    if request.method =="GET" and days_left < 2:
        option = request.GET.get('option')
        print(option)
        if option == '0.6':
            p.expiry_date = date.today() + timedelta(days=183)
        elif option == "1":
            p.expiry_date = date.today() + timedelta(days=365)
        elif option == "2":
            p.expiry_date = date.today() + timedelta(days=365*2)
        elif option == "3":
            p.expiry_date = date.today() + timedelta(days=365*3)
        p.save()
        return render(request,'payment/Payment_option.djhtml',{'p':p} )
    else:
        print('here')
        p_msg ="Payment denied previous payment didnt expire. Payment will expire on " + str(p.expiry_date)
        return render(request, 'payment/Payment_option_denied.djhtml', {'p_msg': p_msg})
