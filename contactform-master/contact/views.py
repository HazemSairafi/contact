from django.core.mail import send_mail
from django.template.loader import render_to_string 
from django.shortcuts import render, redirect
from .forms import RegisterForm, PostForm,ContactForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User, Group
from .models import *
from django.contrib.auth.decorators import user_passes_test







def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            content = form.cleaned_data['content']

            html = render_to_string('contact/emails/contactform.html', {
                'name': name,
                'email': email,
                'content': content
            })

            send_mail('The contact form subject', 'This is the message', 'hazemsairafi@gmail.com', ['hazemsairafi@gmail.com'], html_message=html)

            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'main/index.html', {
        'form': form
    })


@login_required(login_url="/login")
def home(request):
    posts = Post.objects.all()

    if request.method == "POST":
        post_id = request.POST.get("post-id")
        user_id = request.POST.get("user-id")

        if post_id:
            post = Post.objects.filter(id=post_id).first()
            if post and (post.author == request.user or request.user.has_perm("main.delete_post")):
                post.delete()
        elif user_id:
            user = User.objects.filter(id=user_id).first()
            if user and request.user.is_staff:
                try:
                    group = Group.objects.get(name='default')
                    group.user_set.remove(user)
                except:
                    pass

                try:
                    group = Group.objects.get(name='mod')
                    group.user_set.remove(user)
                except:
                    pass

    return render(request, 'main/home.html', {"posts": posts})

# @user_passes_test(lambda user: not user.is_banned)
@login_required(login_url="/login")
@permission_required("main.add_post", login_url="/login", raise_exception=True)
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("/home")
    else:
        form = PostForm()

    return render(request, 'main/create_post.html', {"form": form})


def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home')
    else:
        form = RegisterForm()

    return render(request, 'registration/sign_up.html', {"form": form})



def send_warning(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == 'POST':
        message = request.POST.get('message')
        warning_message = WarningMessage(user=user, message=message)
        warning_message.save()
        return redirect('warningsent')
    return render(request, 'main/warning.html', {'user': user})
    
def warning_sent(request):
    return render(request, 'main/warningsent.html')


def ban_admin(request, user_id):
    user = User.objects.get(id=user_id)
    user.is_banned = True
    user.save()
    return redirect('user_details', user_id=user_id)


@login_required
def ban_user(request, user_id):
    if not request.user.is_superuser:
        return redirect('home')
    banned_user = User.objects.get(id=user_id)
    ban = ban_user(by=request.user, user=banned_user)
    ban.save()
    return redirect('useruser')

