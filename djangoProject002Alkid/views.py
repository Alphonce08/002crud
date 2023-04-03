from django.shortcuts import render, redirect
from .models import Student

def displayindex(request):
    return render(request, "index.html")
def insertData(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phonenumber = request.POST.get('phonenumber')

        query = Student(name=name, email=email, phonenumber=phonenumber)
        query.save()
        return redirect("/")
    return render(request, "index.html")

def index(request):
    data = Student.objects.all()
    context = {"data": data}
    return render(request, "index.html", context)