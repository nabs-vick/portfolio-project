from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')
def reach(request):
    return render(request,'reach.html')
def front(request):
    return render(request,'front.html')
def about(request):
    return render(request,'about.html')
def home(request):
    return render(request,'home.html')
def add(request):
    var1 = int(request.POST['num1'])
    var2 = int(request.POST['num2'])
    res = var1 + var2
    return render(request,'add.html',{'results': res})