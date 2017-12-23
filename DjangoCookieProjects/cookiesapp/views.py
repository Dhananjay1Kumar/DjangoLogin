from django.shortcuts import render
from django.http import HttpResponse
def Input(request):
    return render(request,'Input.html')
def Add(request):
    x=int(request.POST['t1'])
    y=int(request.POST['t2'])
    z=str(x+y)
    resp=HttpResponse('Addition is successfull')
    resp.set_cookie('z',z,max_age=120)
    return resp
def Display(request):
    if 'z' in request.COOKIES:
        sum=request.COOKIES['z']
        return HttpResponse('sum of two numbers is :'+sum)
    else:
        return HttpResponse('Please enter values')

def test(request):
    return HttpResponse('hello Brother')
