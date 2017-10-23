from django.shortcuts import render,redirect, HttpResponse
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):# the index function is called when root is visited
    if 'unique_id' not in request.session:
       request.session['unique_id']=""
    if 'count' not in request.session:
       request.session['count'] = 0
    return render(request,'wordGenerate/index.html')

def generate(request):
    unique_id = get_random_string(length=14)
    print "in generate"
    request.session['count']+=1
    print request.session['count']
    request.session['unique_id'] = unique_id
    # return render(request, "random_word/index.html",request.session['count'])    
    return redirect('/')

def reset(request):
    del request.session['count']
    del request.session['unique_id']
    return redirect('/')

