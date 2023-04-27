from django.db import models


class Corso(models.Model):
    titolo = models.CharField(max_length=400)
    codice = models.CharField(max_length=20)
    data_inizio = models.DateField()
    data_fine = models.DateField()


    def numero_iscritti(self):
        return 'Nessuno'

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
    corso = models.ForeignKey(Corso, on_delete=models.PROTECT, related_name="moduli")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = 'Moduli'



class Materia(models.Model):
    nome = models.CharField(max_length=100)
    modulo = models.ForeignKey(Modulo, on_delete=models.PROTECT, related_name="materie")
    docente = models.ForeignKey(Persona, on_delete=models.PROTECT, null=True, blank=True, related_name='materie')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = 'Materie'


class Lezione(models.Model):

    TIPI_LEZIONE = (
        (None, 'Seleziona...'),
        ('T', 'Teoria'),
        ('P', 'Pratica'),
    )

    materia = models.ForeignKey(Materia, on_delete=models.PROTECT, related_name="lezioni")
    argomento = models.TextField(verbose_name="Di cosa avete parlato?", null=True, blank=True, help_text="Scrivi almeno 3 parole")
    data = models.DateField()
    online = models.BooleanField(default=False)
    tipologia = models.CharField(max_length=1, choices=TIPI_LEZIONE, null=True)
    ora_inizio = models.TimeField(null=True, blank=True)
    ora_fine = models.TimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.materia} del {self.data}'
    
    class Meta:
        verbose_name_plural = 'Lezioni'
        ordering = ['-data']


class Presenza(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.PROTECT, related_name="presenze")
    lezione = models.ForeignKey(Lezione, on_delete=models.PROTECT, related_name="presenze")

    def __str__(self):
        return f'{self.persona} - {self.lezione}'
    
    class Meta:
        verbose_name_plural = 'Presenze'
        ordering = ['persona', 'lezione']
        unique_together = ['persona', 'lezione']


class Iscrizione(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.PROTECT)
    corso = models.ForeignKey(Corso, on_delete=models.PROTECT, related_name="iscrizioni")
    data_iscrizione = models.DateField()
    data_ritiro = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.persona} - {self.corso}'
    
    class Meta:
        verbose_name_plural = 'Iscrizioni'
        ordering = ['persona', 'corso']