from django.db import models

class Corso(models.Model):
    titolo = models.CharField(max_length=40)
    descrizione = models.TextField(max_length=100)
    data_inizio = models.DateField()
    data_fine = models.DateField()
    posti_disponibili = models.IntegerField(default=0,blank=True)
    
    def __str__(self):
        return self.titolo
 
    class Meta:
        verbose_name = "Corso"
        verbose_name_plural = "Corsi"
