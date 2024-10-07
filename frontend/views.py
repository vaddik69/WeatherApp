from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.shortcuts import render
import requests
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import City
from .forms import CityForm, UserRegistrationForm


def index(request, *args, **kwargs):
    return render(request, 'frontend/index.html')


def index1(request):
    appid = '3a64cbd21be993bf4c792f5dd2ceb364'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid

    str_request = str(request)
    lines = str_request.split('\r\n')
    _, method, path = lines[0].split()
    print("request:", request)
    path = path[:-3][1:]
    print(method, path, _)

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()

    all_cities = []

    for city in cities:
        res = requests.get(url.format(city.name)).json()
        city_info = {
            'city': city.name,
            'temp': res["main"]["temp"],
            'icon': res["weather"][0]["icon"],
        }
        all_cities.append(city_info)

    context = {'all_info': all_cities,
               'form': form,
               }

    return render(request, 'frontend/index.html', context)


@login_required
def profile_view(request):
    return render(request, 'frontend/weather/profile.html')


def register(request):
    pass_error = ''
    if request.method == 'POST':
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        user_form = UserRegistrationForm(request.POST)

        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()

            print("done")
            return render(request, 'frontend/weather/profile.html', {'new_user': new_user})
        else:
            if password == password2:
                pass_error = ('The password must contain uppercase and lowercase Latin letters, numbers and be no '
                              'shorter than 8 characters.')
            else:
                pass_error = 'Passwords dont match.'
    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'user_form': user_form, 'pass_error': pass_error})


def get_csrf(request):
    response = JsonResponse({'detail': 'CSRF cookie set'})
    response['X-CSRFToken'] = get_token(request)
    return response


