from django.shortcuts import render,redirect
from django.http import HttpResponse
from hiapp.forms import hiform
from hiapp.models import hi

# Create your views here.
def h(request):
    if request.method=="POST":
        aa=hiform(request.POST)
    
        try:
            aa.save()
            return redirect("/bb")
        except:
            a="username is already existed"
            aa=hiform()
            return render(request,"aa.html",{"f":aa,"a":a})
        
    else:
        aa=hiform()
    return render(request,"aa.html",{"f":aa})
def hello(request):
    aaa=hi.objects.all()
    return render(request,"lion.html",{"aaa":aaa})
def edit(request,a):
    aa=hi.objects.get(username=a)
    return render(request,"edit.html",{"aa":aa})
def update(request,a):
    aa=hi.objects.get(username=a)  
    aaa=hiform(request.POST, instance=aa)  
    if aaa.is_valid():  
        aaa.save()  
        return redirect("bb")  
    return render(request, 'edit.html', {'aa':aa}) 
def delete(request,a):
    aa=hi.objects.get(username=a)
    aa.delete()
    return redirect("/bb")
