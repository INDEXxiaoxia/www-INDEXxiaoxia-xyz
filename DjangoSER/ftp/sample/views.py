from django.shortcuts import render
import os
from .models import  FileItem,PathItem
# Create your views here.

def index(request):
    current = 'C:/INDEXxiaoxia/INDEXxiaoxia/DjangoSER/fileDI/'
    context_dic = {}
    context_dic['current'] = current
    ps = os.listdir(current)
    path = []
    file = []
    for n in ps:
        v = os.path.join(current, n)
        if os.path.isdir(v):
            p = PathItem(n, current)
            path.append(p)
        else:
            f = FileItem(n, current)
            file.append(f)
 
    context_dic['path'] = path
    context_dic['file'] = file
    return render(request, 'index.html', context_dic)
 
def show_folder(request, url):
    current = url
    context_dic = {}
    context_dic['current'] = current
    ps = os.listdir(current)
    path = []
    file = []
    for n in ps:
        v = os.path.join(current, n)
        if os.path.isdir(v):
            p = PathItem(n, current)
            path.append(p)
        else:
            f = FileItem(n, current)
            file.append(f)
 
    # context_dic['parent'] = os.path.pardir(url)
    context_dic['path'] = path
    context_dic['file'] = file
    return  render(request, 'index.html', context_dic)