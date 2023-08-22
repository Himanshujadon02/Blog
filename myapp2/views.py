from django.shortcuts import render,HttpResponse
from .models import *

# Create your views here.
def home(request):
#    data={
#        'title':'Home page',
#      'clist':['php','python','react'],
#      'number':[10,20,30,40,50],
#     'student_details':[
#        {'name':'himanshu','phone_no':972080},
#        ]
#    }
    popularBlogs = Popular_blogs.objects.all()
    
    context = {'popularBLOGS':popularBlogs,'name':'Mr.Himanshu',
    
    }
    return render(request,"home.html",context)


def about(request):
    return render(request,'about.html')

def contact(request):

    if request.method == "POST":
        cname = request.POST["fullname"]
        cphonenumber = request.POST['phone']
        caddress = request.POST["address"]
        cemail = request.POST["email"]
        cmessage = request.POST['message']

    
        print(cname, cphonenumber, caddress, cemail, cmessage)
        # if len(cname) > 1 and len(cphonenumber) == 10 and len(caddress) < 50 and len(cemail) < 15 and len(cmessage) < 50 :
        #     contactobj =  Contactustb(name=cname,phone=cphonenumber,address=caddress,email=cemail,message=cmessage)
        #     contactobj.save()
        # else:
        #     return HttpResponse('filled valid data')
    return render(request,'contact.html')

def blogs(request):
    regularBlogs=Regular_blogs.objects.all()
    context = {'regularBLOGS':regularBlogs,}
    return render(request,"blogs.html",context)
    #return render(request,'blogs.html',{'viewBlog2':view_block2})

def contactdetails(request,contactid):
    return HttpResponse(contactid)

def view_block(request,pk):    #pk-primary keys

    viewBlog=Popular_blogs.objects.get(pk=pk)  

    return render(request,'viewBlog.html',{'viewBlog':viewBlog})

def view_block2(request,pk):    #pk-primary keys

    viewBlog2=Regular_blogs.objects.get(pk=pk)  

    return render(request,'viewBlog2.html',{'viewBlog2':viewBlog2})