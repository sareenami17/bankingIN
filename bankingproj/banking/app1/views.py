from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.decorators import login_required
from app1.decorators import signin_required
from django.utils.decorators import method_decorator

from django.views.generic import CreateView

from app2.models import District, Branch
from app1 import forms
from django.shortcuts import render, redirect
from .forms import AccountForm
from app2.models import Account, Material


def home(request):
    return render(request, "home.html")


class SignUpView(View):
    def get(self, request, *args, **kwargs):
        form = forms.RegistrationForm()
        return render(request, "registration.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = forms.RegistrationForm(request.POST)  # user send cheyyunna data vechu form inisilize cheythu
        if form.is_valid():  # no error in form
            form.save()  # normal orm query password not # ed
            username = form.cleaned_data.get('username')  # form.cleaned data vechu user-ne create cheyyan paranju
            return redirect("login")
        else:
            return render(request, "registration.html", {"form": form})


class LoginView(View):
    def get(self, request, *args, **kwargs):
        form = forms.LoginForm()
        return render(request, "login.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            uname = form.cleaned_data.get("username")
            pwd = form.cleaned_data.get("password")
            user = authenticate(request, username=uname, password=pwd)  # return a user if the credentials are valid
            if user:
                login(request,
                      user)  # user undekill user nte session ivide muthal start cheyyanam.evide oke request.user call cheytho avide oke login cheytha user ne kittum
                if (request.user.is_superuser):  # if admin ?
                    return redirect("adminhome")
                else:
                    messages.success(request, "login success")  # if normal user
                    print("login success")
                    return redirect("home")

            else:
                messages.error(request, "Invalid username or password")
                print("invalid credentials")
                return render(request, "login.html", {"form": form})

@method_decorator(signin_required,name="dispatch")
class SignOutView(View):
    def get(self, request, *args, **kwargs):
        print(request.user.is_authenticated)
        # if request.user.is_authenticated:
        logout(request)
        return redirect("login")

    # Assuming you have already defined the Application model and ApplicationForm
    # in your models.py and forms.py files, respectively.

    # def application_view(request):
    #     if request.method == 'POST':
    #         form = ApplicationForm(request.POST)
    #         if form.is_valid():
    #             # Create an instance of the Application model but don't save it yet
    #             application_instance = form.save(commit=False)
    #
    #             # You can perform any additional processing or modifications to the application_instance here
    #             # For example, you might want to set some fields before saving the instance.
    #
    #             # Save the form data to the database
    #             application_instance.save()
    #
    #             # Redirect to a success page or another view
    #             return redirect('home')
    #     else:
    #         form = ApplicationForm()
    #
    #     return render(request, 'application.html', {'form': form})
    # views.py

@signin_required
def cascading_dropdown(request):
    districts = District.objects.all()
    materials = Material.objects.all()

    if request.method == 'POST':
        name = request.POST['name']
        dob = request.POST['dob']
        age = int(request.POST['age'])
        gender = request.POST['gender']
        phone_number = request.POST['phone_number']
        email = request.POST['email']
        address = request.POST['address']
        district_id = int(request.POST['district'])
        branch_id = int(request.POST['branch'])
        account_type = request.POST['account_type']
        materials_provide = request.POST.getlist('materials_provide')

        district = District.objects.get(pk=district_id)
        branch = Branch.objects.get(pk=branch_id)

        account = Account.objects.create(
            name=name,
            dob=dob,
            age=age,
            gender=gender,
            phone_number=phone_number,
            email=email,
            address=address,
            district=district,
            branch=branch,
            account_type=account_type
        )
        account.materials_provide.set(materials_provide)

        # Process the form data here, for example, save it to the database
        return redirect('success_page')  # Redirect to a success page after form submission

    return render(request, 'account_form.html', {'districts': districts, 'materials': materials})


def get_branches(request, district_id):
    branches = Branch.objects.filter(district_id=district_id).values('id', 'name')
    return JsonResponse(list(branches), safe=False)


# views.py


""" def account_form_view(request):
    districts = District.objects.all()
    materials = Material.objects.all()
    branch = Branch.objects.all()

    if request.method == 'POST':
        name = request.POST['name']
        dob = request.POST['dob']
        age = int(request.POST['age'])
        gender = request.POST['gender']
        phone_number = request.POST['phone_number']
        email = request.POST['email']
        address = request.POST['address']
        district_id = int(request.POST['district'])
        branch_id = int(request.POST['branch'])
        account_type = request.POST['account_type']
        materials_provide = request.POST.getlist('materials_provide')

        district = District.objects.get(pk=district_id)
        branch = Branch.objects.get(pk=branch_id)

        account = Account.objects.create(
            name=name,
            dob=dob,
            age=age,
            gender=gender,
            phone_number=phone_number,
            email=email,
            address=address,
            district=district,
            branch=branch,
            account_type=account_type
        )
        account.materials_provide.set(materials_provide)

        # Process the form data here, for example, save it to the database
        return redirect('success_page')  # Redirect to a success page after form submission

    return render(request, 'account_form.html', {'districts': districts, 'materials': materials}, {'branch': branch})

"""


def success_page_view(request):
    return render(request, 'success_page.html')
