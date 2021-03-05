from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import StaffForm, PrincipalUserForm, UserForm
from .models import Staff, Principal, Role

# Welcome Page
def index(request):
  return render(request, 'index.html')

# Dashboard
@login_required
def dashboard(request):
  staffs = Staff.objects.all()
  principals = Principal.objects.all()
  roles = Role.objects.all()
  context = {'staffs': staffs, 'principals':principals, "roles":roles}
  return render(request, 'dashboard.html', context)

# Register principal
def register(request):
  if request.method == "POST":
    form = UserForm(request.POST)
    principalForm = PrincipalUserForm(request.POST)

    if form.is_valid() and principalForm.is_valid():
      user = form.save()

      princip = principalForm.save(commit=False)

      princip.user = user

      princip.save()

      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password1')
      user = authenticate(username=username, password=password)
      login(request, user)

      return redirect('dashboard')
    else:
      print("Form is not valid")
  else:
    form = UserForm()
    principalForm = PrincipalUserForm()
  
  context = {'form': form, 'principalForm': principalForm}
  return render(request, 'register.html', context)

# Log in Principal
def loginUser(request):
  if request.method == "POST":
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(username=username, password=password)
    login(request, user)
    print('logging user!!!')
    return redirect('dashboard')
  return render(request, 'login.html')

# Log out user
def logoutUser(request):
  logout(request)
  return redirect('staff_login')

# Register as a staff
def staff_register(request):
  if request.method == "POST":
    form = UserForm(request.POST)
    staffForm = StaffForm(request.POST)

    if form.is_valid() and staffForm.is_valid():
      user = form.save()

      staff = staffForm.save(commit=False)

      staff.user = user

      staff.save()

      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password1')
      user = authenticate(username=username, password=password)
      login(request, user)

      return redirect('dashboard')
    else:
      print("Form is not valid")
  else:
    form = UserForm()
    staffForm = StaffForm()
  
  context = {'form': form, 'staffForm': staffForm}
  return render(request, 'teacher_register.html', context)

# Log in as staff
def staff_login(request):
  if request.method == "POST":
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(username=username, password=password)
    login(request, user)
    print('logging user!!!')
    return redirect('dashboard')
  return render(request, 'teacher_login.html')