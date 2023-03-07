from django.shortcuts import render
import pyqrcode
import os


# Create your views here.
url=None
ui=None
def h(request):
    global ui
    if ui!=None:
       os.remove(ui)
    if request.method=='POST':
        
        url=request.POST['url']
      
        u=pyqrcode.create(url)
        u.svg(f'static/{url}.svg',scale=8)
        ui=f'static/{url}.svg'   
    return render(request,'h.html',{'p':ui})





