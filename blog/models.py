from django.db import models

# Create your models here.

class Posts(models.Model):
    id_post = models.AutoField(primary_key=True)
    autor = models.CharField(max_length = 20)
    titulo = models.CharField(max_length=255)
    data = models.DateTimeField('Post Date')
    semestre = models.IntegerField('Semestre')
    discplina = models.CharField(max_length=50)
    mensagem = models.TextField()

    def __str__(self):
        return self.titulo