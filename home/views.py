from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import Subscribers
from .helpers import otp_generator
from django.contrib import messages
from django.http import JsonResponse
from .form import *
from django.contrib.auth import logout
from django.conf import settings
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def logout_view(request):
    logout(request)
    return redirect("/")

def homepage(request):
    blogs = BlogModel.objects.order_by("-views")
    context = {'blogs': blogs}

    return render(request, 'home.html', context)

def loginpage(request):
    if request.user.is_authenticated:
        return redirect("/user_panel/")
    else:
        return render(request, 'login.html')


def subscribe(request):
    
    global username
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        email = email.lower()
        if Subscribers.objects.filter(email=email).first():
            messages.warning(request, "The provided email has already subscribed!")
        else:
            OTP = otp_generator()
            print('OTP sent in gmail is:',OTP)
            subs = Subscribers.objects.create(
                username=username, email=email
            )
            subs.email_token = OTP
            subs.save()

            email = [email]
            print(email)
            send_mail(
                f'Hi {username}, Your OTP is {OTP}',
                f'Your otp is {OTP}',
                settings.EMAIL_HOST_USER,
                email,
            )
            return redirect(f'/email_token/{username}/')

    return render(request, 'subscribe.html')

def email_token(request, username):
    context = {"username": username}
    
    if request.method == 'POST':
        userotp = Subscribers.objects.filter(username=username).first()
        userotp = userotp.email_token
        givenotp = request.POST.get('OTP')
        if userotp == givenotp:
            obj = Subscribers.objects.filter(username=username).first()
            obj.is_verified = True
            obj.save()
            messages.success(request, 'Email has been verified!')
            email = obj.email
            username = obj.username
            send_mail(
                "Email has been verified!",
                f"Hey {username}, your email has been verified and from now on you shall be updated with Blogs on this email!",
                settings.EMAIL_HOST_USER,
                [email],
            )
            return redirect('/')
        else:
            messages.warning(request, "Invalid OTP please make sure that you type your OTP correctly, If it doesn't fixes your problem then click on resend OTP.")
        

    return render(request, 'email_token.html', context)

def resend_otp(request, username):
    OTP = otp_generator()
    obj = Subscribers.objects.filter(username=username).first()
    obj.email_token = OTP
    obj.save()
    email = [obj.email]

    send_mail(
        f'Hi {username}, Your OTP is {OTP}',
        f'Your otp is {OTP}',
        settings.EMAIL_HOST_USER,
        email,
    )
    messages.success(request, "New OTP has been sent to the provided email.")
    return redirect(f"/email_token/{username}")

@never_cache
def blog_detail(request, slug):
    context = {}
    try:
      blog_obj = BlogModel.objects.filter(slug = slug).first()
      blog_obj.views = blog_obj.views + 1
      blog_obj.save()
      context['blog_obj'] = blog_obj
      context['blogs'] = BlogModel.objects.exclude(slug=slug)
      context['blogs'] = context['blogs'].filter(genre=blog_obj.genre)
      context['views'] = blog_obj.views
    except Exception as e:
        print(e)
    return render(request, 'blog_detail.html', context)

def update_blog(request, slug):
    context = {'form': BlogForm}
    try:

        blog_obj = BlogModel.objects.get(slug=slug)

        if blog_obj.user != request.user:
            return redirect('/')

        initial_dict = {'content': blog_obj.content}
        form = BlogForm(initial=initial_dict)
        if request.method == 'POST':
            form = BlogForm(request.POST)
            print(request.FILES)
            image = request.FILES['image']
            title = request.POST.get('title')
            genre = request.POST.get('flexRadioDefault')
            genre = str(genre)

            if form.is_valid():
                content = form.cleaned_data['content']

            blog_obj.title, blog_obj.image, blog_obj.genre, blog_obj.content = title, image, genre, content
            blog_obj.save()

        context['blog_obj'] = blog_obj
        context['form'] = form
    except Exception as e:
        print(e)

    return render(request, 'update_blog.html', context)

  
def user_panel(request):
    context = {}

    try:
        blog_objs = BlogModel.objects.filter(user=request.user)
        context['blog_objs'] = blog_objs
    except Exception as e:
        print(e)

    print(context)
    return render(request, 'user_panel.html', context)

def add_blog(request):
    context = {'form': BlogForm}
    try:
        if request.method == 'POST':
            form = BlogForm(request.POST)
            print(request.FILES)
            image = request.FILES.get('image', '')
            title = request.POST.get('title')
            user = request.user
            genre = request.POST.get('flexRadioDefault')
            genre = str(genre)

            if form.is_valid():
                print('Valid')
                content = form.cleaned_data['content']

            blog_obj = BlogModel.objects.create(
                user=user, title=title,
                content=content, image=image, genre=genre,  
            )

            subscribers = Subscribers.objects.all()
            subscribers = subscribers.filter(is_verified=True)
            for subs in subscribers:
                html_content = render_to_string('email_template.html', {
                    'image':image,
                    'title':title,
                    'content':content,
                    })
                email = EmailMultiAlternatives(
                    subject=f"New Blog: {title}",
                    body=f"Hi {subs.username}, We have a new blog for you.",
                    from_email=settings.EMAIL_HOST_USER,
                    to=[subs.email],
                )
                email.attach_alternative(html_content, "text/html")
                email.send()
                print(f'sent mail to {subs.email}')

            return redirect('/user_panel/')
    except Exception as e:
        print(e)

    return render(request, 'add_blog.html', context)

def delete_blog(request, id):
    try:
        blog_obj = BlogModel.objects.get(id=id)

        if blog_obj.user == request.user:
            blog_obj.delete()

    except Exception as e:
        print(e)

    return redirect('/user_panel/')

