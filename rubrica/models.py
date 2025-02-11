from django.db import models

class Contatto(models.Model):
    nome = models.CharField(max_length=25)
    telefono = models.CharField(max_length=10)
    email = models.CharField(max_length=20, blank=True)
    
    def __str__(self):
        return self.nome
 
    class Meta:
        verbose_name = "Contatto"
        verbose_name_plural = "Contatti"