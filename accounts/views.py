from django.shortcuts import render, HttpResponseRedirect
from .forms import RegistrationForm
from django.views import View
from django.contrib.auth import get_user_model

# Create your views here.
User = get_user_model()


class UserRegistrationView(View):
  def get(self, request):
    registration_form = RegistrationForm()
    context = {
      "registration_form": registration_form
    }
    return render(request, "registration_form.html", context=context)

  def post(self, request):
    registration_form = RegistrationForm(request.POST)
    if registration_form.is_valid():
      username = registration_form.cleaned_data.get("username")
      password = registration_form.cleaned_data.get("password")
      email = registration_form.cleaned_data.get("email")
      new_user = User.objects.create_user(username=username, email=email)
      new_user.set_password(password)
      new_user.save()
      return HttpResponseRedirect("/login")

    else:
      context = {
        "registration_form": registration_form
      }
      return render(request, "registration_form.html", context=context)
