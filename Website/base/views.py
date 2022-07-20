from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register(request):
    if request.method=='POST':

       form=UserCreationForm(request.POST)
       if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=UserCreationForm()
    return render(request,"register.html",{'form':form})
def home(request):
    return render(request,"home.html")
def projects(request):
    return render(request,"projects.html")
def contact(request):
    return render(request,"contact.html")
def gallery(request):
    return render(request,"gallery.html")
