from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.conf import settings
from django.http import JsonResponse

# Create your views here.
def home(request):
    return render(request,'index.html')



# Create your views here.


def send_email_from_app(mobile_no=None,name=None, email=None,address=None,contact_person_name=None,message=None,time=None,template=None):
    print(email)
    data =  { 'email': email, 'name':name,'mobile_no':mobile_no,'address':address,'contact_person_name':contact_person_name,
                    'message':message,'time':time}

    email_html_template = get_template(template).render(data)
    receiver_email = email
    email_msg = EmailMessage('Dits Intelligence - Enquiry Details',
                                email_html_template,
                                settings.EMAIL_HOST_USER,
                                [receiver_email],
                                [settings.EMAIL_HOST_USER],
                                reply_to=[settings.EMAIL_HOST_USER]
                                )
    email_msg.content_subtype = 'html'
    email_msg.send(fail_silently=False)

def restaurant(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        contact_person_name = request.POST.get('contact_person_name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        mobile_no = request.POST.get('mobile_no')
        print('check mobile no and email------------------',settings.EMAIL_HOST_USER)
        
        
       
        send_email_from_app(mobile_no,name, email,address,contact_person_name,message,time=None,template = 'enquiry_mail.html')
        val=0
        return redirect('thankyou')
    else:
        return render(request, 'index.html')


def thankyou(request):
    return render(request,'thankyou.html')
 

def schedule_demo(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        contact_person_name = request.POST.get('contact_person_name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        mobile_no = request.POST.get('mobile_no')
        time=request.POST.get('time')
        print('check mobile no and email------------------',settings.EMAIL_HOST_USER)
        
        
       
        send_email_from_app(mobile_no,name, email,address,contact_person_name,message,time,template = 'enquiry_mail.html')
        val=0
        return redirect('thankyou')
    else:
        return render(request, 'index.html')

def contact_us(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('subject')
        # subject = request.POST.get('subject')
        email = request.POST.get('email')
        message = request.POST.get('message')
        mobile_no = None
        time=None
        contact_person_name=None
        print('check mobile no and email------------------',settings.EMAIL_HOST_USER)
        
        
       
        send_email_from_app(mobile_no,name, email,address,contact_person_name,message,time,template = 'enquiry_mail.html')
        val=0
        return redirect('thankyou')
    else:
        return render(request, 'index.html')
