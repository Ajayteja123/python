from django.shortcuts import render, HttpResponse
from .models import home
# Create your views here.


def index(request):
    context = {
        "variable1": "this variable is variable1",
        "variable2": "this is variable2"
    }
    # return HttpResponse("this is homepage page")
    return render(request, 'njk.htm', context)


# def home(request):
#     return HttpResponse("this is home page")


def about(request):
    return HttpResponse("this is about page")


def service(request):
    return HttpResponse("this is service page")


def contact(request):
    return HttpResponse("this is contact page")


def createpost(request):
    if request.method == 'POST':
        instance_user = home()
        instance_user.name = request.POST['user_name']
        instance_user.age = request.POST['age']
        instance_user.save()
        return HttpResponse('register done')
