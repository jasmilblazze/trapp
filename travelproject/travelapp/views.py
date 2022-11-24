from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def demo(request):
    name="USER"
    return render(request,"index.html",{'obj':name})
def addition(request):
    first=int(request.GET['num1'])
    second=int(request.GET['num2'])
    res=first+second
    mul=first*second
    div=first/second
    sub=first-second
    return render(request,"result.html",{'result':res,'multiplication':mul,'division':div,'subtraction':sub})

