from django.shortcuts import render,redirect
from .models import Employee
from faker import Faker
import random

# Create your views here.

def ShowEmp_view(request):
    data = Employee.objects.all()
    template_name ="empapp/showdata.html"
    context = {'obj':data}
    return render(request, template_name, context)

def FakerData(request):
    template_name ='empapp/showdata.html'
    fake=Faker()
    for i in range(10):
        emp = Employee()

        emp.eid=random.randint(0,999)
        emp.name=fake.name()
        emp.address=fake.address()
        emp.email=fake.email()
       

        emp.save()
    return redirect('showdata_url')