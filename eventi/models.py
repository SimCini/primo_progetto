from django.db import models

class Evento(models.Model):
    titolo = models.CharField(max_length=20)
    data = models.DateField(blank=True)
    descrizione = models.TextField()
    partecipanti = models.IntegerField(default=0,blank=True)
    
    def __str__(self):
        return self.titolo
 
    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventi"
