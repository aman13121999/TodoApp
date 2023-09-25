from django.shortcuts import render,redirect
from django.http import HttpRequest
from django.contrib.auth import authenticate,login as loginuser,logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from TODOapp.forms import TodoForm
from TODOapp.models import Todo
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='login')
def home(request):
    if request.user.is_authenticated:
        user=request.user
        form=TodoForm()
        todos=Todo.objects.filter(user=user).order_by('priority')
        return render(request,'TODOapp/index.html',{'form':form,'todos':todos})
    else:
        return redirect('login')



def login(request):
    if request.method=='GET':
        form=AuthenticationForm()
        context={'form':form}
        return render(request,'TODOapp/login.html',context=context)
    else:
        form=AuthenticationForm(data=request.POST)
        
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user is not None :
                loginuser(request,user)
                return redirect('home')
            print("Authenticated",user)
            
        else:
            context={'form':form}
            return render(request,'TODOapp/login.html',context=context)
            
        
    
def signup(request):
    if request.method=='GET':
        form=UserCreationForm()
        context={
        "form":form
    }
        return render(request,'TODOapp/signup.html',context=context)

    else:
           
            form=UserCreationForm(request.POST)
            context={"form":form}
            if form.is_valid():
                user=form.save()
                if user is not None:
                    return redirect('login')
                    
            else:
                return render(request,'TODOapp/signup.html',context=context)


@login_required(login_url='login')            # type: ignore
def add_todo(request):
    if request.user.is_authenticated:
        user=request.user
        print(user)
        form=TodoForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            todo=form.save(commit=False)
            todo.user=user
            todo.save()
            print(todo)
            return redirect('home')
        else:
            return render(request,'TODOapp/index.html',{'form':form})
        
    
             
def signout(request):
    logout(request)
    return redirect('login')

def delete_todo(request,id):
    print(id)
    Todo.objects.get(pk=id).delete()
    return redirect('home')

def change_status(request,id,status):
    
    toto= Todo.objects.get(pk=id)
    toto.status=status
    toto.save()
    return redirect('home')
    


