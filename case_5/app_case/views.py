from django.http import Http404
from django.shortcuts import get_object_or_404,render, redirect
from django.http import HttpResponse
from django.template import loader
# from .models import Tarefa
from .models import Question, Tarefa
from django.utils.dateparse import parse_datetime


def home(request):
    return render(request, "home.html")

def cadastro_usuarios(request):
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
        Tarefa.objects.create(titulo= titulo, materia=materia, descricao=descricao, prazo=prazo, status=status)
        # tarefa.save()
        # print(tarefa)
        
        tarefas = {
            'tarefas': Tarefa.objects.all()
        }
    
    return render(request, "home.html", tarefas )

def listagem_tarefas(request):
    tarefas = {
            'tarefas': Tarefa.objects.all()
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
            #tarefa.save()
            return redirect("listagem_tarefas")
        else:
            return render(request, "editar_tarefas.html", {'tarefa': tarefa, 'error': 'Preencha todos os campos.'})

    return render(request, "editar_tarefas.html", {'tarefa': tarefa})

def deletar_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, id=tarefa_id)
    
    if request.method == 'POST':
        tarefa.delete()
    
    return render(request, "listagem_tarefas")
# Exemplos 
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {
        "latest_question_list": latest_question_list,
    }
    return render(request, "index.html", context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "detail.html", {"question": question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
