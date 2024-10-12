from django.http import Http404
from django.shortcuts import get_object_or_404,render, redirect
from django.http import HttpResponse
from django.template import loader
# from .models import Tarefa
from .models import Question, Tarefa
from django.utils.dateparse import parse_datetime
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth import logout



def home(request):
    return render(request, "home.html")

def cadastro_usuarios(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if email and username and password1 and password2:
            user = User.objects.create_user(username=username, email=email, password=password1)
            print(f'Usuário {user.username} criado com sucesso!')  
            return redirect("login")

    return render(request, "cadastro_usuarios.html")

def cadastro_tarefas(request):
    

    return render(request, "cadastro_tarefas.html")

def cadastrar_tarefa(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        materia = request.POST.get('materia')
        descricao = request.POST.get('descricao')
        prazo = request.POST.get('prazo')
        status = request.POST.get('status')
        usuario = request.user
        Tarefa.objects.create(titulo= titulo, materia=materia, descricao=descricao, prazo=prazo, status=status, usuario=usuario)
        # tarefa.save()
        # print(tarefa)
        
        tarefas = {
            'tarefas': Tarefa.objects.all()
        }
    
    return render(request, "home.html", tarefas )

def listagem_tarefas(request):
    tarefasEncontradas = Tarefa.objects.filter(usuario=request.user)
    tarefas = {
            'tarefas': tarefasEncontradas
        }
    
    return render(request, "listagem_tarefas.html", tarefas )

def editar_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, id=tarefa_id)
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        materia = request.POST.get('materia')
        descricao = request.POST.get('descricao')
        prazo = request.POST.get('prazo')
        status = request.POST.get('status')

        if titulo and materia and descricao and prazo and status:
            prazo = parse_datetime(prazo)  # Converte a string de data e hora para um objeto datetime
            tarefa.titulo = titulo
            tarefa.materia = materia
            tarefa.descricao = descricao
            tarefa.prazo = prazo
            tarefa.status = status
            tarefa.save()
            return redirect("listagem_tarefas")
        else:
            return render(request, "editar_tarefas.html", {'tarefa': tarefa, 'error': 'Preencha todos os campos.'})

    return render(request, "editar_tarefas.html", {'tarefa': tarefa})

def deletar_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, id=tarefa_id)
    
    if request.method == 'POST':
        tarefa.delete()
        return redirect("listagem_tarefas")
    
    return render(request, "deletar_tarefa.html", {'tarefa': tarefa})
# Exemplos 


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "detail.html", {"question": question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def login_usuario(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        email = request.POST.get('email')
        senha = request.POST.get('password')
        
        user = User.objects.filter(email=email).get()
        
        print (user.username)
        print (senha)
        user = authenticate(username=user.username, password=senha)
        print(user)
        if user:
            login(request, user)
            return redirect('home')
        return HttpResponse("usuário ou senha inválidos.")
    
        
def logout_usuario(request):
    logout(request)  # Faz logout do usuário
    # messages.success(request, "Você foi desconectado com sucesso!")  # Mensagem de sucesso
    return redirect('login')