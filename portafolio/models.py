from django.db import models

# Create your models here.

class Project(models.Model):
    tittle = models.CharField(max_length=200, verbose_name = "Titulo")
    description = models.TextField(verbose_name = "Descripcion")
    image = models.ImageField(verbose_name = "Imagen", upload_to = "projects")
    created = models.DateTimeField(auto_now_add=True, verbose_name = "Fecha de Creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name = "Fecha de Edicion")

    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        ordering = ["-created"]

    def __str__(self):
        return self.tittle    

class Players(models.Model):
    id = models.IntegerField(primary_key=True)
    player = models.TextField()  # Field name made lowercase.
    position = models.TextField()  # Field name made lowercase.
    games = models.IntegerField(blank=True, null=True, default='')  # Field name made lowercase.
    win_rate = models.TextField()  # Field name made lowercase.
    kda = models.TextField()  # Field name made lowercase.
    avg_kills = models.TextField()  # Field name made lowercase.
    avg_deaths = models.TextField()  # Field name made lowercase.
    avg_assists = models.TextField()  # Field name made lowercase.
    csm = models.TextField()  # Field name made lowercase.
    gpm = models.IntegerField(blank=True, null=True, default='')  # Field name made lowercase.
    dmg = models.TextField()  # Field name made lowercase.
    avg_dpm = models.IntegerField(blank=True, null=True, default='')  # Field name made lowercase.
    vspm = models.TextField()  # Field name made lowercase.
    avg_wpm = models.TextField()  # Field name made lowercase.
    avg_wcpm = models.TextField()  # Field name made lowercase.
    avg_vwpm = models.TextField()  # Field name made lowercase.
    gd15 = models.IntegerField(blank=True, null=True, default='')  # Field name made lowercase.
    csd15 = models.IntegerField(blank=True, null=True, default='')  # Field name made lowercase.
    xpd15 = models.IntegerField(blank=True, null=True, default='')  # Field name made lowercase.
    fb = models.TextField()  # Field name made lowercase.
    fb_victim = models.TextField()  # Field name made lowercase.
    penta_kills = models.IntegerField(blank=True, null=True, default='')  # Field name made lowercase.
    solo_kills = models.IntegerField(blank=True, null=True, default='')  # Field name made lowercase.
    

    class Meta:
        verbose_name = "jugador"
        verbose_name_plural = "jugadores"
        #ordering = ["-created"]

    def __str__(self):
        return self.player
    