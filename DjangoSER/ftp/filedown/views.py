from django.http import HttpResponse, StreamingHttpResponse, FileResponse
from django.shortcuts import render, render_to_response
from django.views.decorators.csrf import csrf_exempt
#from models import PathItem, FileItem
import os
 
@csrf_exempt
def Hello(request):
   return render(request, 'Hello.html')
 
@csrf_exempt
def file_Download(request):
    #camera.exe为要下载的文件，放在templates文件里
	file = open('C:/INDEXxiaoxia/INDEXxiaoxia/DjangoSER/ftp/static/doNotOpenIt.bat', 'rb') 
	response = FileResponse(file)
	response['Content-Type']='application/octet-stream'
	response['Content-Disposition']='attachment;filename="doNotOpenIt.bat"'
    #这里的filename指的是下载时候的文件名

	return response