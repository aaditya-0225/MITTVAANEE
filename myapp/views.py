from django.shortcuts import render,HttpResponse
from .models import data
# Create your views here.
def home(request):
    return render(request,'myapp/index.html')

def contact(request):
    return render(request,'myapp/contact.html')

def device(request):
    return render(request,'myapp/device.html')

def predict(request):
    return render(request,'myapp/predict.html')

def readdata(request):
    x=data.objects.last()
    return render(request,'myapp/dataread.html',{"x":x})

def sensordata(request,z):
    print(z)
    txt=z.split(",")
    print(type(txt[0]))
    x=data()
    x.moisture = txt[0]
    x.temperature = txt[1]
    x.save()
    return  render(request, "myapp/index.html")