from django.shortcuts import render, redirect
from django.contrib import messages
from django.core import serializers
from .models import User
import hashlib, json

# Vistas
def index(request):
    
    if request.method == 'POST':
        nickname = request.POST['nickname'].lower()
        password = request.POST['password'].lower()

        password_hash = hashlib.sha256(password.encode('UTF-8')).hexdigest()
        user = User.objects.filter(nickname=nickname, password__iexact=password_hash, status=1).first()
        
        if not user:
            messages.add_message(request, messages.ERROR, "Usuario o credenciales invalidas.")         
        else:
            # messages.add_message(request, messages.INFO, "Usuario encontrado")     
            user_json = serializers.serialize('json', [user], ensure_ascii=False)            
            request.session['userlogin'] = user_json
            return redirect('home')
               
    return render(request, 'index.html', {})

def home(request):
    try:
        _user = request.session['userlogin']
        if not _user:
            return redirect('index')
        
        user = json.loads(_user)[0]
        context = {
            "user": user
        }
        return render(request, 'home.html', context)
    except Exception as ex:
        return redirect('index')

def logout(request):    
    try:
        del request.session['userlogin']
    except Exception as ex:
        pass
    
    return redirect('index')
    