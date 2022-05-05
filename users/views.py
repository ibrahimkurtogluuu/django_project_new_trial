from django.shortcuts import render, redirect #redirect is for after submitting request redirect to another page # from django.contrib.auth.forms import UserCreationForm     since we dont use it we deleted.
from django.contrib import messages # this is one time alert. flash messages. when refresh the page messages wont show up.
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm # we have added forms. after importing this changed below UserCreationForm statement with UserRegisterForm.
# Create your views here. form is a class.
from django.contrib.auth.decorators import login_required
def register(request):
    if request.method == 'POST': #POST is for writing data, submits data to be processed (e.g. from an HTML form) to the identified resource.
        form = UserRegisterForm(request.POST) # instead UserCreationForm, changed after importing UserRegisterForm
        if form.is_valid():
            form.save()  # this is actually for creating a user.
            username = form.cleaned_data.get('username') # form was converted into dictionary so that the python can understand it.
            # messages.success(request, f'Account created for {username}!')
            messages.success(request, f'You are registered. Now you are able to log in.')
            return redirect('login') # we change the redirected page as login. we redirected but we havent updated our template to actually show the flashed messages yet. so go to blog/base.html. put related code above block content code.
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form }) # second form is instance.first is just a variable. # instead UserCreationForm, changed after importing UserRegisterForm, used for creating a new user that can use our web application. It has three fields: username, password1, and password2
# and then create a template that uses this form. such as blog.html, about.html ...
# in users app, create Templates directory, in it users dir., in it register.html

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user) # N4
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile) # N4
        if u_form.is_valid() and p_form.is_valid(): # N4
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
# N4
    else:
        u_form = UserUpdateForm(instance=request.user) # N4
        p_form = ProfileUpdateForm(instance=request.user.profile) # N4
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)

# N4
# to add forms we need to import first
# and add in profile function.
# open profile.html template and print out these forms
# N4
