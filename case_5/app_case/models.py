from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Tarefa(models.Model):
    titulo = models.CharField(max_length=100)
    materia = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)
    prazo = models.DateField()
    status = models.CharField(max_length=100)
    usuario= models.ForeignKey(User, on_delete=models.CASCADE, default=1)


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    # def __str__(self):
    #     return self.question_text
    # def was_published_recently(self):
    #     return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
