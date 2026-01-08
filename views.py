from django.shortcuts import render

# Create your views here.

def main (request):
    context = {}
    return render(request,'salama/index.html', context)

def header (request):
    context = {}
    return render(request,'salama/header.html', context)

def project (request):
    context = {}

    return render(request,'salama/project.html', context)
