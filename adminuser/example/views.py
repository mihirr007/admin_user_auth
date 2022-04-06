
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .models import Person
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .forms import loginForm, usrChange
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.cache import cache_control
from django.contrib.auth import logout

from .forms import usrForm
# Create your views here.

# posts = [
#     {
#         'author': 'dhruvs',
#         'title': 'Blog Post 1',
#         'content': 'First post content',
#         'date_posted': '01/01/2022'
#     },  
#     {
#         'author': 'mr',
#         'title': 'Blog Post 2',
#         'content': 'Second post content',
#         'date_posted': '07/03/2022'
#     }
# ]

# def home(request):
#     context = {
#         'posts': posts
#     }
#     return render(request, 'home.html', context)

# @csrf_exempt
# def login(request):
    
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         users = auth.authenticate(username=username, password=password)

#         if users is not None:
#             if users.is_superuser == True:
#                 auser = get_user_model()
#                 ausers = list(auser.objects.all().values())
#                 # print(ausers)
#                 a =[]
#                 for i in ausers:
#                     values = i.values()
#                     values_list = list(values)
#                     usersofad = values_list[4] + ',  '
                    
#                     a.append(usersofad)
#                 return HttpResponse(a)
#             auth.login(request,users)
#             return render(request, 'dashboard.html',posts)

#         else:
#             messages.info(request, 'invalid credentials')
#             return redirect('login')
        

#     else:
#         return render(request,'login.html')

# def logout(request):
#     auth.logout(request)
#     return render(request,'login.html')


# def register(request):

#     if request.method == 'POST':
#         first_name = request.POST.get('first_name')
#         last_name = request.POST.get('last_name')
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         email = request.POST.get('email')
#         is_superuser = request.POST.get('admin')
#         if is_superuser == 'on':
#             is_superuser = True
#             auser = get_user_model()
#             ausers = list(auser.objects.all().values())



#             a =[]
#             for i in ausers:
#                 values = i.values()
#                 values_list = list(values)
#                 usersofad = values_list[4] + ',  '
                
#                 a.append(usersofad)
                
#             users = User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name, email=email, is_superuser =is_superuser )
#             users.save();
#             print('user created')
#             return HttpResponse(a)
#         else:
#             is_superuser = False

#         return  render(request, 'dashboard.html')


#     else:
#         return render(request, 'register.html')


#############################################################

#     return render(request, 'register.html')




# def base(request):
#     return render(request, 'base.html')
     
 
# def user_login(request):
    
#     if request.method == "POST":
#         username = request.POST.get('username')
#         password = request.POST.get('password')
        
            
#         try:
#             user = Authentication.usrObjects.get(username=username,password=password)
#             user.save()
#             print(user)
#             if user is not None:               
#                 return render(request, 'dashboard.html', {})
#             else:
#                 print("Someone tried to login and failed.")
#                 print("They used username: {} and password: {}".format(username,password))
    
#                 return redirect('/')
#         except Exception as identifier:
#             return redirect('/')
     
#     else:
#         return render(request, 'base.html')




#########################################################




def user_list(request,id=0):
    
    if 'user' in request.session:  #check whether user is logged or not 
       
        if request.method == 'GET':  
            context = {'user_list' : Person.objects.all()}   #getting list of users
            return render(request, 'usr_list.html', context)
        else:
            form = usrForm(request.POST)
            if form.is_valid():                 # post method after updating details of users
                form.save()
            context = {'user_list' : Person.objects.all()}
        
        return render(request, "usr_list.html", context)
    
    else:
        return redirect('login')
        



def user_form(request, id=0):
    if 'user' in request.session:
        
        if request.method == "GET":
            if id == 0:
                print('reg1')
                form = usrForm(initial={'password': 123})  # register - view
                
            else:
                print('up1')
                auser = Person.objects.get(pk=id)
                form = usrForm(instance=auser) #update - view
                
            return render(request, "usr_form.html",{'form': form})

        else:
            if id == 0:
                print('reg2')
                form = usrForm(request.POST , initial={'password': 123}) # register - data send
                if form.is_valid():
                    username=form.cleaned_data.get('username')
                    email=form.cleaned_data.get('email')
                    i = Person.objects.filter(username=username).exists()
                    j = Person.objects.filter(email=email).exists()
                    if i is True:
                        messages.error(request, 'Username is taken')
                        return redirect('register')
                    elif j is True:
                        messages.error(request, 'Email already exists')
                        return redirect('register')
            else:
                
                auser = Person.objects.get(pk=id) #update - data send
                form = usrForm(request.POST,instance=auser)
                if form.is_valid():
                    username=form.cleaned_data.get('username')
                    email=form.cleaned_data.get('email')
                    i = Person.objects.filter(username=username).exists()
                    j = Person.objects.filter(email=email).exists()
                    if i is True:
                        messages.error(request, 'Username is taken')
                        
                    elif j is True:
                        messages.error(request, 'Email already exists')
                        
                    
            if form.is_valid():
                form.save()

            
                
            return redirect('list')
    else:
        return redirect('login')


 
def user_delete(request,id):
    if 'user' in request.session:  #check whether user is logged or not
        auser = Person.objects.get(pk=id)
        auser.delete()         #delete user
        return redirect('list')
    else:
        return redirect('login')


def user_login(request):
    
    form = loginForm()
    if request.method == 'POST':
        form = loginForm(data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')         # cleaned_data automatically converts data to the appropriate type like IntegerField to integer
            password=form.cleaned_data.get('password')
            i = Person.objects.filter(username=username,password=password).exists()
            user = {'user_list' : Person.objects.filter(username=username,password=password)}
            
            
            
            if i == True:
                j = Person.objects.filter(username=username, position_id = 1).exists()
                if j == True:
                    request.session['user'] = username
                    return redirect('list')
                request.session['user'] = username
                return render(request,"usr_wlc.html", user )
            else:
                messages.error(request, 'Invalid username or password!')
            
                
    context = {'form':form}
    return render(request,'usr_login.html',context)


def user_detail(request,id):
    if 'user' in request.session:     
        auser = Person.objects.get(pk=id)            # after updating details of User like  change password
        form = usrChange(request.POST,instance=auser)    
        if form.is_valid():
            form.save()
        logout(request)
        return redirect('login')
    else:
        return redirect('login')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def user_logout(request):

    request.session.clear()
  
    logout(request)
    return redirect('/')



def user_change(request,id):
    if 'user' in request.session:
        auser = Person.objects.get(pk=id) #update
        form = usrChange(request.POST,instance=auser)
        
        return render(request, "usr_chnge.html",{'form': form}) 
    else:
        return redirect('login')




















































    

    
        
    
# def user_chnged_list(request):
#     if 'user' in request.session:
#         form = usrForm(request.POST)
#         if form.is_valid():
#             form.save()
#         context = {'user_list' : Person.objects.all()}
        
#         return render(request, "usr_list.html", context) 
#     else:
#         return redirect('login')      










# def user_login(request):
#     if request.method == "POST":  
#         fm = AuthenticationForm(request=request, data=request.POST)  
#         print(fm.is_valid()) 
#         print('####533')
#         print(fm.data)
#         print(fm.errors)     
#         if fm.is_valid():
            
#             uname =fm.cleaned_data['username']
#             upass =fm.cleaned_data['password']
#             user = authenticate(username=uname, password=upass)
#             if user is not None:
#                 login(request,user)
#                 return redirect('list')
#     else:
#         fm = AuthenticationForm()
#     return render(request, "usr_login.html",{'form':fm})
