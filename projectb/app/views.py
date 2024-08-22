from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def page1(request):
    return render(request,"page1.html")

def page2(request):
    return render(request,"page2.html")

def page3(request):
    return render(request,"page3.html")

def page4(request):
    return render(request,"page4.html")

def sum(request):
    return render(request,"sum.html")

def anssum(request):
    n1=int(request.POST['num1'])
    n2=int(request.POST['num2'])
    n3=n1+n2
    return render(request,"sum.html",{'result':n3})

def calculator(request):
    return render(request, 'calculator.html')

def calcu(request):
    if request.method == 'POST':
        expression = request.POST.get('input')
        try:
            result = eval(expression)
        except Exception as e:
            result = 'Error'
        return render(request, 'calculator.html', {'result': result})
    return HttpResponse(status=405)


