from django.http import HttpResponse
from django.shortcuts import render
from .models import Place
from .models import Name
# Create your views here.
def demo(request):
    obj=Place.objects.all()
    obj1=Name.objects.all()
    return render(request, "index.html",{'result':obj,'result2':obj1})


#def addition(request):
   # x = int(request.GET['num1'])
    #y = int(request.GET['num2'])
   # add = x + y
    #sub = x - y
   # mul = x * y

    #div = x / y

   # return render(request, "result.html", {'result': add,'difference': sub,'product': mul,'quotient':div})

