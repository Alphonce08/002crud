from django.shortcuts import render,redirect

def displayindex(request):
    return render(request, "index.html")

def insertData(request):
    return render(request, "index.html")