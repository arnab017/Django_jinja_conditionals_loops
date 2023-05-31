from django.shortcuts import render

# Create your views here.

def jinja_conditionals(request):
    d1 = {
        'a' : 10,
        'b' : 20,
        'c' : 30,
    }
    return render(request,'jinja_conditionals.html',d1)

def jinja_loops(request):
    d2 = {
        'name' : 'JINJA',
    }
    return render(request,'jinja_loops.html',d2)

