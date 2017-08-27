from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import AnonymousUser
from .forms import UserForm,LoginForm,CredentialForm
from django.views.generic import View



'''
class UserFormView(View):
    form_class = UserForm
    template_name = 'registration_form.html'

    #display the blank form
    def get(self,request):
        form = self.form_class(None)
        return render(request,self.template_name,{'form':form})

    #process form data
    def post(self,request):
        form = self.form_class(request.Post)

        if form.is_valid():

            user = form.save(commit=False)

            #cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            #returns User objects if Credentials are correct
            user = authenticate(username=username,password=password)

            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('home.html')


        return render(request,self.template_name,{'form':form})
'''

def home(request):
    if not request.user.is_anonymous():
            return redirect('/dashboard')
    return redirect('/login')


def dashboard_config(request):
    title = 'Dashboard'
    page_title = 'Welcome '+request.user.username+' to the dashboard'
    context = {
	    "heading": page_title,
        "title" : title,
    }
    return render(request,"home.html",context)

def fleet_request(request):
    title = 'Fleet Spot Instance Request'
    form = CredentialForm(request.POST or None)
    IamFleetRole = request.POST.get('IamFleetRole', '')
    TargetCapacity = request.POST.get('TargetCapacity', '')
    InstanceType = request.POST.get('InstanceType', '')
    SubnetId = request.POST.get('SubnetId', '')
    spotPrice = request.POST.get('spotPrice', '')
    ValidUntil = request.POST.get('time_of_expiration', '')

    context = {
	    "title": title,
	    "form" : form
    }
    return render(request,"configure.html",context)

def loginUser(request):
    title ='Please Log in'
    form = LoginForm(request.POST or None)
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = authenticate(username = username, password = password)

    if user is not None:
        login(request, user)
        return redirect('/dashboard')
    context = {
	    "title": title,
		"form" : form
    }

    return render(request,"login.html",context)

def signup(request):
    title ='Sign Up'

    form = UserForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect('/')
    context = {
	    "title": title,
		"form" : form
    }

    return render(request,"registration_form.html",context)

