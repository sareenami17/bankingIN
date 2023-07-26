from django.shortcuts import redirect
from django.contrib import messages

def signin_required(fn):  # ullil oru fn(view) arugument
    def wrapper(request, *args, **kwargs):  # oru inner fn
        if not request.user.is_authenticated:
            messages.error(request,"You must login")
            return redirect("login")
        else:
            return fn(request, *args, **kwargs)  # aaa fn lottu bypass cheyyam

    return wrapper
