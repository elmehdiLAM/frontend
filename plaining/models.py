from datetime import timedelta
from django.db import models
from django.utils import timezone


class Person(models.Model):
    statue_choice = [("PES", "PES"),
                     ("PH", "PH"),
                     ("PA", "PA"),
                     ("MA", "MA"),
                     ("Assist", "Assist"),
                     ("AP/prep", "AP/prep"), ]
    etat_choice = [("INT", "Interne"),
                   ("EXT", "Externe"), ]
    sexe_choice = [("MAS", "Masculin"),
                   ("FEM", "Feminin"), ]
    CIN = models.CharField(primary_key=True,
                           max_length=20)
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    email = models.EmailField(default="")
    numPhone = models.CharField(max_length=16)
    statue = models.CharField(choices=statue_choice,
                              default="DOC",
                              max_length=10)
    etat = models.CharField(choices=etat_choice,
                            default="EXT",
                            max_length=10)
    sexe = models.CharField(choices=sexe_choice,
                            default="",
                            max_length=10)
    maxHoraireMois = models.PositiveIntegerField(default=20)
    maxHoraireJour = models.IntegerField(blank=True,
                                         null=True)

    def __str__(self):
        return self.CIN + self.nom + self.prenom


class Cours(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    etablisement = models.CharField(default="FSR", max_length=100)
    date = models.DateField()
    nombreheure = models.PositiveIntegerField(default=3)
    date_ajout = models.TimeField(auto_now=True)
    module = models.CharField(max_length=100, default='module')

    def __str__(self):
        return self.person.__str__() + self.date.__str__()


class Deplacement(models.Model):
    type_depalcement_choice = [("NAT", "National"), ("INT", "International"), ]

    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    type_deplacement = models.TextField(default="NAT", max_length=100, choices=type_depalcement_choice)
    self_veicule = models.BooleanField(default=False)
    date_depart = models.DateField(default=timezone.datetime.today())
    date_retour = models.DateField(default=timezone.datetime.today() + timedelta(days=1))
    evenement = models.CharField(max_length=300, default=' ')
    depenseEstimeJour = models.DecimalField(decimal_places=2, max_digits=10, default=500)
    description = models.TextField(max_length=500, default='description')
    kilometrage = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.person.__str__() + self.type_deplacement
