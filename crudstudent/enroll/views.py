from.models import User
from django.shortcuts import render
from enroll.forms import StudentRegistration
from django.http import HttpResponseRedirect

#Create your views here.
#adding and retrieving data
def add_show(request):
    if request.method =='POST':
        fm= StudentRegistration(request.POST)
        if fm.is_valid():
            nm= fm.cleaned_data['name']
            em= fm.cleaned_data['email']
            pw= fm.cleaned_data['password']
            reg= User(name=nm, email=em, password=pw)
            reg.save()
            fm= StudentRegistration()
    else:
        fm =StudentRegistration()
    stud =User.objects.all()
    return render(request,'enroll/add.html',{'form': fm,'stu':stud})
#edit and update function
def update_data(request,id):
    if request.method =='POST':
        pi= User.objects.get(pk=id)
        fm= StudentRegistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi= User.objects.get(pk=id)
        fm =StudentRegistration(instance=pi)
    return render(request,'enroll/update.html',{'form':fm})
#delete function
def delete_data(request,id):
    if request.method == 'POST':
        pi= User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')