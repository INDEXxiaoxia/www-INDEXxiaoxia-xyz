from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
def indexadd(request):
    return render(request, 'ajaxtest.html')
    
def add(request):
    a = request.GET['a']
    b = request.GET['b']
    a = int(a)
    b = int(b)
    return HttpResponse(str(a+b))
def ajax_list(request):
    a = range(100)
    a=list(a)
    return JsonResponse(a, safe=False)

def ajax_dict(request):
    name_dict = {'twz': 'Love python and Django', 'zqxt': 'I am teaching Django'}
    return JsonResponse(name_dict)