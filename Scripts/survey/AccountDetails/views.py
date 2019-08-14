from django.shortcuts import render
from django.contrib.auth import(authenticate,get_user_model,login,logout)
from .forms import UserForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Workers
def index(request):
    return render(request,"home.html",{})

def index1(request):
	return render(request,"ward.html",{})

def index2(request):
	return render(request,"district.html",{})

def index3(request):
	return render(request,"state.html",{})

def index4(request):
	return render(request,"central.html",{})

def get_data(request):
    objects = Workers.objects.all()
    context = {
    'obj':objects
    }
    return render(request,'Workers.html',context)

@login_required
def special(request):
    # Remember to also set login url in settings.py!
    # LOGIN_URL = '/basic_app/user_login/'
    return HttpResponse("You are logged in. Nice!")

@login_required
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return HttpResponseRedirect(reverse('index'))

def register(request):

    registered = False

    if request.method == 'POST':

        # Get info from "both" forms
        # It appears as one form to the user on the .html page
        user_form = UserForm(data=request.POST)

        # Check to see both forms are valid
        if user_form.is_valid():

            # Save User Form to Database
            user = user_form.save()

            # Hash the password
            user.set_password(user.password)

            # Update with Hashed password
            user.save()

            # Now we deal with the extra info

            # Registration Successful!
            registered = True

        else:
            # One of the forms was invalid if this else gets called.
            print(user_form.errors)

    else:
        # Was not an HTTP post so we just render the forms as blank.
        user_form = UserForm()
       

    # This is the render and context dictionary to feed
    # back to the registration.html file page.
    return render(request,'AccountDetails/signup.html',
                          {'user_form':user_form,
                           'registered':registered})

def user_login(request):

    if request.method == 'POST':
        # First get the username and password supplied
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Django's built-in authentication function:
        user = authenticate(username=email, password=password)

        # If we have a user
        if user:
            #Check it the account is active
            if user.is_active:
                # Log the user in.
                login(request,user)
                # Send the user back to some page.
                # In this case their homepage.
                print(request.user.level)
                if request.user.level==1:
                	return render(request, 'ward.html', {})
                elif request.user.level==2:
                	return render(request, 'district.html', {})
                elif request.user.level==3:
                	return render(request, 'state.html', {})
                else:
                	return render(request, 'central.html', {})
            else:
                # If account is not active:
                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used email: {} and password: {}".format(email,password))
            return HttpResponse("Invalid login details supplied.")

    else:
        #Nothing has been provided for username or password.
        return render(request, 'AccountDetails/login.html', {})
