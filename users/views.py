from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.views import View

from users.forms import UserLoginForm, UserRegisterForm
from users.models import CustomUser


class UserRegisterView(View):
    template_name = "users/register.html"
    form_class = UserRegisterForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            phone_number = form.cleaned_data["phone_number"]
            CustomUser.objects.create_user(email, phone_number, password)
            return redirect("users:login")
        return render(request, self.template_name, {"form": form})


class UserLoginView(View):
    template_name = "users/login.html"
    form_class = UserLoginForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                return redirect("core:home")
            else:
                messages.error(request, "Invalid email or password.", extra_tags="danger")
                return redirect("users:login")

        return render(request, self.template_name, {"form": form})
