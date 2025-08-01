from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# topic es el tema del problema los usuarios no van a poder crear 
# problemas ni temas solo soluciones ya despues podemos crear eso pero 
# centremos todo en la estructura
class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    


# aquí veras que topic es perteneciente al topic de arriba 
# ya tendriamos lo basico que necesitariamos para el problema descripción...
class Problem(models.Model): 
    level = models.CharField(max_length=50, default='Easy')
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=300)
    description = models.TextField(null=True,blank=True)
    solvers = models.ManyToManyField(User, related_name='solvers', blank=True)

    def __str__(self):
        return self.title

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    body = models.TextField(null=True,blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta: 
        ordering = ['-updated', '-created']
    
    def __str__(self):
        return self.body[0:50]
# La solución es sencilla nada fuera de lo común esta ligada al usuario y al problema
# para despues poder filtrar por esos dos campos
class Solution(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta: 
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.body[0:20]
