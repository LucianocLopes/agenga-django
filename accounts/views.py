from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import ContatoForm


def login(request):
    if request.method != 'POST':
        return render(request, 'accounts/login.html')
    
    usuario = request.POST.get('usuario')
    senha = request.POST.get('password')

    if not usuario or not senha:
        messages.error(request, 'Usuário e Senha devem ser informados!')
        return render(request, 'accounts/login.html')
    
    user = auth.authenticate(request, username=usuario, password=senha)

    if not user:
        messages.error(request, 'Usuário ou Senha são inválidos!')
        return render(request, 'accounts/login.html')
    else:
        auth.login(request, user)
        messages.success(request, 'Login realizado com sucesso!')
        return redirect('dashboard')
    

def logout(request):
    if request.method != 'POST':
        auth.logout(request)
        messages.success(request, 'Seção encerrada!')
        request.POST
        return render(request, 'accounts/logout.html')


def cadastro(request):
    print(request.POST)
    if request.method != 'POST':

        return render(request, 'accounts/cadastro.html')
    
    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    email = request.POST.get('email')
    usuario = request.POST.get('usuario')
    senha = request.POST.get('password')
    senha2 = request.POST.get('password2')

    if not nome or not sobrenome or not email or not usuario or not senha or not senha2:
        messages.error(request, 'Todos os campos devem ser preenchidos!')
        return render(request, 'accounts/cadastro.html')
    
    try:
        validate_email(email)
    except:
        messages.error(request, 'Informe um endereço de e-mail válido!')
        return render(request, 'accounts/cadastro.html')
    
    if len(senha) < 8:
        messages.error(request, 'Senha deve conter, no mínimo 8 caracteres!')
        return render(request, 'accounts/cadastro.html')

    if senha2 != senha:        
        messages.error(request, 'As senhas digitadas devem ser iguais!')
        return render(request, 'accounts/cadastro.html')
    
    if User.objects.filter(username=usuario).exists():
        messages.error(request, 'Usuário já existe!')
        return render(request, 'accounts/cadastro.html')
    
    if User.objects.filter(email=email).exists():
        messages.error(request, 'Endereço de e-mail já existe!')
        return render(request, 'accounts/cadastro.html')
    
    messages.success(request, 'Usuário cadastrado com sucesso!')
    user = User.objects.create_user(username=usuario, password=senha, email=email, first_name=nome, last_name=sobrenome)
    user.save()
    return redirect('login')


@login_required(redirect_field_name='login')
def dashboard(request):
    if request.method != 'POST':
        form = ContatoForm
        return render(request, 'accounts/dashboard.html', {'form': form})

    form = ContatoForm(request.POST, request.FILES)

    if not form.is_valid():
        messages.error(request, 'Erro ao enviar o formulário!')
        form = ContatoForm(request.POST)
        return render(request, 'accounts/dashboard.html', {'form': form})
    
    biografia = request.POST.get('biografia')

    if len(biografia) < 6:
        messages.error(request, 'Biografia deve conter ao menos 6 caracteres!')
        form = ContatoForm(request.POST)
        return render(request, 'accounts/dashboard.html', {'form': form})
    
    form.save()
    messages.success(request, f'Contato {request.POST.get("nome")} salvo com sucesso!')
    return redirect('dashboard')