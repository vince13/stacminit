from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth import authenticate, login, logout

from .models import Student, Talent
from .forms import UserRegisterForm, UserLoginForm, StudentRegistrationForm


def home(request):

    students = Student.objects.all()

    context = {"students": students}
    return render(request, "talent/home.html", context)


def about(request):

    context = {}
    return render(request, "talent/about.html", context)


def register(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = StudentRegistrationForm()
    return render(request, 'talent/register.html', {'form': form})


# User register
def register_view(request):
    form = UserRegisterForm()

    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("talent:login")

    context = {"form": form}
    return render(request, "talent/register.html", context)


# User login
def login_view(request):
    if request.method == "POST":
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("talent:home")

    else:
        form = UserLoginForm()

    context = {"form": form}
    return render(request, "talent/login.html", context)


# User logout
def logout_view(request):
    logout(request)
    return redirect("talent:login")


# Register student form
def new_student(request):
    form = StudentRegistrationForm()

    if request.method == "POST":
        form = StudentRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            student = form.save(commit=False)
            student.user = request.user
            student.save()
            return redirect("talent:home")

    context = {"form": form}
    return render(request, "talent/student_form.html", context)

