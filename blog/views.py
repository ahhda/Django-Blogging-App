from django.shortcuts import render
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login

# Create your views here.
from django.shortcuts import render,get_object_or_404
from blog.models import Post

def index(request):
	posts=Post.objects.filter(published=True)
	return render(request,'blog/index.html',{'posts':posts})

def post(request,slug):
	post=get_object_or_404(Post,slug=slug)
	return render(request,'blog/post.html',{'post':post})

def login_user(request):
	state = "Please log in below "
	username= password = ''
	if request.POST:
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				state="You're successfully logged in!"
			else:
				state="Your account is not active"
		else:
			state="Your username and/or password were incorrect"
	return render_to_response('blog/auth.html',{'state':state, 'username':username})