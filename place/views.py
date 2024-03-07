from django.shortcuts import render
from django.contrib.auth import authenticate, login ,  logout
from django.shortcuts import redirect
from django.contrib.auth.models import User

def homeView(request):
    
    return render(request, 'home.html')

def loginView(request):
    if request.user.is_authenticated :
        return redirect('home', )
    elif request.method == 'POST' :
        username_or_email = request.POST['username']
        password = request.POST['password']
        
     
        user = authenticate(request, username=username_or_email, password=password)
        
        if user is not None:
            try:
                user = User.objects.get(email=username_or_email,password=password)              
                user = authenticate(request, username=user.username, password=password) 
                
            
            except User.DoesNotExist:
                pass
            
        if user is not None:
            login(request, user)
            
            
            if request.user.groups.filter(name="VIPS").exists():
                print('vips')
                return redirect('vips')
        
            elif request.user.groups.filter(name="Clientes").exists():
                print('cliente')
                
                return redirect('GoToApp')
            
            else:
                return redirect('login')
            
            
        else:
            error_message = "Credenciais invalidas "
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')
    
    
    
def logoutView (request):
    logout(request)
    
    return redirect('login')
def cadastroView(request):
    
    return render(request, 'cadastro.html')

def goToAppView (request):
    
    return render(request, 'app.html') 

def vipsView (request):

    
    return render(request, 'vips.html') 

def cadClientesView (request):

    
    return render(request, 'cadastroCliente.html') 