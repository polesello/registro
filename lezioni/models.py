from django.db import models


class Corso(models.Model):
    titolo = models.CharField(max_length=400)
    codice = models.CharField(max_length=20)
    data_inizio = models.DateField()
    data_fine = models.DateField()

    def __str__(self):
        return self.titolo
    
    class Meta:
        verbose_name_plural = 'Corsi'
        ordering = ['-data_inizio']



class Persona(models.Model):
    nome = models.CharField(max_length=200)
    cognome = models.CharField(max_length=200)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.nome + ' ' + self.cognome
    
    class Meta:
        verbose_name_plural = 'Persone'
        ordering = ['cognome', 'nome']


class Modulo(models.Model):
    nome = models.CharField(max_length=100)
    corso = models.ForeignKey(Corso, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = 'Moduli'



class Materia(models.Model):
    nome = models.CharField(max_length=100)
    modulo = models.ForeignKey(Modulo, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = 'Materie'


class Lezione(models.Model):
    materia = models.ForeignKey(Materia, on_delete=models.PROTECT)
    argomento = models.TextField(null=True, blank=True)
    data = models.DateField()

    def __str__(self):
        return f'{self.materia} del {self.data}'
    
    class Meta:
        verbose_name_plural = 'Lezioni'
        ordering = ['-data']


class Presenza(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.PROTECT)
    lezione = models.ForeignKey(Lezione, on_delete=models.PROTECT)
    presente = models.BooleanField()

    def __str__(self):
        return f'{self.persona} - {self.lezione} - {self.presente}'
    
    class Meta:
        verbose_name_plural = 'Presenze'
        ordering = ['persona', 'lezione']