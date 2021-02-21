from datetime import datetime, timedelta
from .models import Person, Cours, Deplacement
import  pandas as pd


kilometrage_tarifs = {'6 ou moins': 1.2,
                      '7 a 9': 1.75,
                      '10 ou plus': 2.3}
horraire_sup_tarifs = {"PES": 300,
                       "PH": 230,
                       "PA": 180,
                       "MA": 150,
                       "Assist": 120,
                       "AP/prep": 50}


def daymatchlist1(cours, instancedate):
    for c in cours:
        if c.date == instancedate:
            return True
    return False


def daymatchlist2(deplacement, instancedate):
    for dep in deplacement:
        if dep.date_depart <= instancedate <= dep.date_retour:
            return True
    return False


def invalidedatecourse(cours, deplacements, instancedate):
    return daymatchlist1(cours, instancedate) or daymatchlist2(deplacements, instancedate)


def invalideDeplacement(instance, cours, deplacement):
    delta = instance.date_retour - instance.date_depart
    days = [instance.date_depart + timedelta(days=j) for j in range(delta.days + 1)]
    for day in days:
        if invalidedatecourse(cours, deplacement, day):
            return True
    return False


def depassemaxhoraire(cours, instance):
    total = instance.nombreheure
    for c in cours:
        total += c.nombreheure
    return total > Person.objects.get(pk=instance.person.CIN).maxHoraireMois


def alreadyexist(cin):
    p = Person.objects.get(pk=cin)
    if p is None:
        return False
    return True


def possiblemodules(cin):
    profil = Person.objects.get(pk=cin)
    cours = Cours.objects.filter(person=profil)
    moduls = [m.module for m in cours]
    return list(set(moduls))


def possibleyears(cin):
    profil = Person.objects.get(pk=cin)
    cours = Cours.objects.filter(person=profil)
    dates = [m.date.year for m in cours]
    return list(set(dates))


def possibleevents(cin):
    profil = Person.objects.get(pk=cin)
    deplacement = Deplacement.objects.filter(person=profil)
    events = [m.evenement for m in deplacement]
    return events


def coursdata(year, module):
    return None
