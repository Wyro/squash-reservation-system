from django.shortcuts import render
from basic_app.forms import UserForm, UserProfileInfoForm

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from basic_app.models import CourtEvent


# Create your views here.
def index(request):
    return render(request, 'basic_app/index.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def special(request):
    return HttpResponse("You are logged in, nice!")

def register(request):

    registered = False

    if request.method == "POST":
        user_form = UserForm(data = request.POST)
        profile_form = UserProfileInfoForm(data = request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit = False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True

        else:
            print(user_form.errors,profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'basic_app/registration.html',{'user_form':user_form, 'profile_form':profile_form, 'registered':registered})


def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("Someone tried to login and failed")
            print("Username: {} and password {}".format(username,password))
            return HttpResponse("invalid login details supplied!")
    else:
        return render(request, 'basic_app/login.html',{})

#def reservation(request):
#    return render(request, 'basic_app/reservation.html')

def reservation(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        selected_day = request.POST.get('selected_day')
        selected_time = request.POST.get('selected_time')

        event1 = CourtEvent(name = username, event_day = selected_day, event_time = selected_time)
        event1.save()
        return HttpResponseRedirect(reverse('index'))

    else:
        events_list = CourtEvent.objects.all()
        my_dict = {
        'events_list':events_list,
        }

        def give_me_wyros_records():
            return events_list.filter('name'=="Wyro")

        eight=events_list.filter(event_time="8:00")
        if eight == True:
            my_dict.update('eight',eight)

        nine = events_list.filter(event_time="9:00")
        if nine == True:
            my_dict.update('nine',nine)

        ten = events_list.filter(event_time="10:00")
        if ten == True:
            my_dict.update('ten',ten)

        eleven = events_list.filter(event_time="11:00")
        if eleven == True:
            my_dict.update('eleven',eleven)

        twelve = events_list.filter(event_time="12:00")
        if twelve == True:
            my_dict.update('twelve',twelve)

        thirteen = events_list.filter(event_time="13:00")
        if thirteen == True:
            my_dict.update('thirteen',thirteen)

        fourteen = events_list.filter(event_time="14:00")
        if fourteen == True:
            my_dict.update('fourteen',fourteen)

        fifteen = events_list.filter(event_time="15:00")
        if fifteen == True:
            my_dict.update('fifteen',fifteen)

        return render(request, 'basic_app/reservation.html',my_dict)
