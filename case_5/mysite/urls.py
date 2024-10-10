"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from app_case import views

urlpatterns = [
    path("app_case/", include("app_case.urls")),
    path('admin/', admin.site.urls),
    path("", views.home, name="home"),
    path("cadastro_usuarios", views.cadastro_usuarios, name="cadastro_usuarios"),
    
    path("cadastro_tarefas/", views.cadastro_tarefas, name="cadastro_tarefas"),
    
    path("cadastrar_tarefas/", views.cadastrar_tarefa, name="cadastrar_tarefa"),

    path("listagem_tarefas/", views.listagem_tarefas, name="listagem_tarefas"),
    
    path("editar_tarefas/<int:tarefa_id>/", views.editar_tarefa, name="editar_tarefa"),
    
    path("deletar_tarefa/<int:tarefa_id>/", views.deletar_tarefa, name="deletar_tarefa"),
    
    path("specifics/<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
