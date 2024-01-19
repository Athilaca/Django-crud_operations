from django.shortcuts import redirect,render
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.views.decorators.cache import cache_control
from django.contrib.auth.models import User
from . forms import updateform


# Create your views here.
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def home(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return redirect(admin)
        return render(request,'home.html')
    return redirect(perform_login)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def perform_login(request):
   
    if request.user.is_authenticated: 
        return redirect(home)
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        

        myuser = authenticate(username=username,password=password)

        if myuser is not None:
            login(request,myuser)
            return redirect(home)
        else:
            messages.error(request,'invalid username or password')
            
    return render(request,'login.html')


def user_logout(request):
    if request.user.is_authenticated: 
        logout(request)
    return redirect(perform_login)


def perform_signup(request):
    if request.method=='POST':
         
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")
        confirmpassword=request.POST.get("confirmpassword")


        if password!=confirmpassword:
            messages.warning(request,'password is incorrect')
            return redirect('/signup')
        
        try:
            if User.objects.get(username=username):
                messages.info(request,'username is taken')
                return redirect('/signup')
                
        except:
            pass    

        try:
            if User.objects.get(email=email):
                messages.info(request,'email is taken')
                return redirect('/signup')
        except:
            pass    

        myuser=User.objects.create_user(username,email,password)
        myuser.save()
        messages.success(request,'signup is successful please login!')

        return redirect(perform_login)
    return render(request,'signup.html')

def admin(request):
    if not request.user.is_superuser:
        return redirect(home)

    if "q" in request.GET:
        search= request.GET['q']
        data=User.objects.filter(username__icontains=search)
    else:    
      data=User.objects.all()
  
    return render(request,'admin.html',{'data':data})
   

    
       


def add_user(request):
   if request.user.is_superuser: 
     if request.method=='POST': 
        
        username=request.POST.get("username")
       
        email=request.POST.get("email")
        password=request.POST.get("password")
    
        myuser=User.objects.create_user(username,email,password)
        myuser.save()
        return redirect(admin)
     return render(request,'add.html')
   else:
    return redirect(perform_login)
        



def delete(request,id):
    if request.user.is_superuser:
        dele=User.objects.get(id=id)
        if dele.is_superuser:
            return redirect(admin)
        else:
          dele.delete()
        return redirect(admin)

def update(request,id):
    if request.user.is_superuser:
        data=User.objects.get(id=id)
        form=updateform(instance=data)
        if request.method=="POST":
            form=updateform(request.POST,instance=data)
            if form.is_valid:
                form.save()
                return redirect(admin)
    return render(request,'update.html',{'form':form})
   

   
def admin_logout(request):
    if request.user.is_superuser:
         logout(request)
    return redirect('login')

