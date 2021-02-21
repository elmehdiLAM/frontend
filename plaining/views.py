from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect, get_object_or_404
from .forms import Personform, Coursform, Deplacementform
from .models import Person, Cours, Deplacement
from .helpers import invalidedatecourse, depassemaxhoraire, alreadyexist, invalideDeplacement, possiblemodules, \
    possibleyears, possibleevents, coursdata
from .personalexceptions import Exmaxhoraire, Exoccupe, Alreadyexist


def homePage(request):
    if request.user.is_authenticated:
        return render(request,
                      "../templates/homePage.html")
    else:
        return redirect('loginUser')


def loginUser(request):
    if request.method == "GET":
        return render(request,
                      "../templates/loginUser.html",
                      {'form': AuthenticationForm()})
    else:
        user = authenticate(request,
                            username=request.POST['username'],
                            password=request.POST['password'])
        if user is None:
            return render(request,
                          '../templates/loginuser.html',
                          {'form': AuthenticationForm(),
                           'error': 'Username and password did not match'})
        else:
            login(request, user)
            return redirect('homePage')


def logoutUser(request):
    if request.method == "POST":
        logout(request)
        print("logout from current account")
        return redirect('homePage')
    else:
        return redirect('homePage')


def listPerson(request):
    if request.user.is_authenticated:
        listperson = Person.objects.all()
        return render(request,
                      '../templates/listPerson.html',
                      {'persons': listperson})
    else:
        return redirect('loginUser')


def Profil(request, CIN):
    if request.user.is_authenticated:
        profil = Person.objects.get(pk=CIN)
        deplacements = Deplacement.objects.filter(person=profil)
        cours = Cours.objects.filter(person=profil)
        return render(request,
                      '../templates/profil.html',
                      {'profil': profil,
                       'cours': cours,
                       'deplacements': deplacements})
    else:
        return redirect('loginUser')


def createPerson(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            return render(request,
                          '../templates/createPerson.html',
                          {'form': Personform()})
        else:
            try:
                form = Personform(request.POST)
                newperspon = form.save()
                # cheking if the person alredy exist
                # print("cheking ")
                # print(alreadyexist(newperspon.CIN))
                # if alreadyexist(newperspon.CIN):
                #    print("diidugknoshdo")
                #    raise Alreadyexist
                # print('fzhdp fzgfo gzfzp fzyfz ')
                # newperspon.save()
                print("new person added saccufly")
                return redirect('listPerson')
            except Exception as e:
                if e.__class__.__name__ == "ValueError":
                    return render(request,
                                  '../templates/createPerson.html',
                                  {'form': Personform(),
                                   'error': "deja exist"})
                if e.__class__.__name__ == "Alreadyexist":
                    return render(request,
                                  '../templates/createPerson.html',
                                  {'form': Personform(),
                                   'error': "deja exist"})
    else:
        return redirect('loginUser')


def addCours(request, CIN):
    if request.user.is_authenticated:
        profil = get_object_or_404(Person, pk=CIN)
        if request.method == 'GET':
            return render(request,
                          '../templates/addcours.html',
                          {'form': Coursform(),
                           'person': profil})
        else:
            try:
                form = Coursform(request.POST)
                newCours = form.save(commit=False)
                newCours.person = profil
                cours = Cours.objects.filter(person=profil,
                                             date__year=newCours.date.year,
                                             date__month=newCours.date.month)
                deplacement = Deplacement.objects.filter(person=profil)
                returned_value = invalidedatecourse(cours, deplacement, newCours.date)
                if returned_value is True:
                    raise Exoccupe
                maxh = depassemaxhoraire(cours, newCours)
                if maxh is True:
                    raise Exmaxhoraire
                print(" cours added")
                newCours.save()
                return redirect('Profil', CIN=profil.CIN)
            except ValueError:
                return render(request,
                              '../templates/addcours.html',
                              {'form': Coursform(),
                               'person': profil,
                               'error': ' verifier les donnees encore une fois '})
            except Exoccupe:
                return render(request,
                              '../templates/addcours.html',
                              {'form': Coursform(),
                               'person': profil,
                               'error': f' {profil.nom} {profil.prenom} deja occupé a cette date '})
            except Exmaxhoraire:
                return render(request,
                              '../templates/addcours.html',
                              {'form': Coursform(),
                               'person': profil,
                               'error': f' {profil.nom} {profil.prenom} a ateint le maximaum horraire '})
    else:
        return redirect('loginUser')


def addDeplacement(request, CIN):
    if request.user.is_authenticated:
        profil = get_object_or_404(Person, pk=CIN)
        if request.method == 'GET':
            return render(request,
                          '../templates/adddeplacement.html',
                          {'form': Deplacementform(),
                           'person': profil})
        else:
            try:
                form = Deplacementform(request.POST)
                newdeplacement = form.save(commit=False)
                newdeplacement.person = profil
                # function for cheking
                deplacement = Deplacement.objects.filter(person=profil)
                cours = Cours.objects.filter(person=profil)
                returned_value = invalideDeplacement(newdeplacement, cours, deplacement)
                if returned_value is True:
                    raise Exoccupe
                newdeplacement.save()
                print(profil)
                print(newdeplacement)
                print("new deplacementadded saccufly")
                return redirect('Profil', CIN=profil.CIN)
            except ValueError:
                return render(request,
                              '../templates/adddeplacement.html',
                              {'form': Deplacementform(),
                               'person': profil,
                               'error': "quelque chose ca marche pas, verifier"})
            except Exoccupe:
                return render(request,
                              '../templates/adddeplacement.html',
                              {'form': Deplacementform(),
                               'person': profil,
                               'error': f' {profil.nom} {profil.prenom} deja occupé a cette dure '})
    else:
        return redirect('loginUser')


def updateProfil(request, CIN):
    if request.user.is_authenticated:
        profil = Person.objects.get(CIN=CIN)
        if request.method == 'GET':
            form = Personform(instance=profil)
            return render(request,
                          '../templates/updateprofil.html',
                          {'form': form,
                           'profil': profil})
        else:
            try:
                form = Personform(request.POST, instance=profil)
                form.save()
                print(" person updated saccufly")
                return redirect('Profil', CIN=profil.CIN)
            except ValueError:
                return render(request,
                              '../templates/updateprofil.html',
                              {'form': Personform(instance=profil),
                               'error': "quelque chose ca marche pas, verifier"})
    else:
        return redirect('loginUser')


def updateCours(request, id):
    if request.user.is_authenticated:
        cours = Cours.objects.get(pk=id)
        if request.method == 'GET':
            form = Coursform(instance=cours)
            return render(request,
                          '../templates/updatecours.html',
                          {'form': form})
        else:
            try:
                form = Coursform(request.POST, instance=cours)
                form.save()
                print(" Cours updated saccufly")
                return redirect('Profil', CIN=cours.person.CIN)
            except ValueError:
                return render(request,
                              '../templates/updatecours.html',
                              {'form': Coursform(instance=cours),
                               'error': "quelque chose ca marche pas, verifier"})
    else:
        return redirect('loginUser')


def updateDeplacement(request, id):
    if request.user.is_authenticated:
        deplacement = Deplacement.objects.get(pk=id)
        if request.method == 'GET':
            form = Deplacementform(instance=deplacement)
            return render(request,
                          '../templates/updatedeplacement.html',
                          {'form': form})
        else:
            try:
                form = Coursform(request.POST, instance=deplacement)
                form.save()
                print(" deplacement updated saccufly")
                return redirect('Profil', CIN=deplacement.person.CIN)
            except ValueError:
                return render(request,
                              '../templates/updatedeplacement.html',
                              {'form': Deplacementform(instance=deplacement),
                               'error': "quelque chose ca marche pas, verifier"})
    else:
        return redirect('loginUser')


def removeProfil(request, CIN):
    if request.user.is_authenticated:
        if request.method == 'POST':
            profil = Person.objects.get(pk=CIN)
            print(f" person {profil.nom} {profil.prenom} has deleted")
            profil.delete()
            return redirect('listPerson')
    else:
        return redirect('loginUser')


def removeCours(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            cours = Cours.objects.get(pk=id)
            # popup for confirmation
            cours.delete()
            return redirect('Profil', CIN=cours.person.CIN)
    else:
        return redirect('loginUser')


def removeDeplacement(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            deplacement = Deplacement.objects.get(pk=id)
            # popup for confirmation
            deplacement.delete()
            return redirect('Profil', CIN=deplacement.person.CIN)
    else:
        return redirect('loginUser')


def etatSommes(request, CIN):
    if request.user.is_authenticated:
        if request.method == 'GET':
            years = possibleyears(CIN)
            events = possibleevents(CIN)
            modules = possiblemodules(CIN)
            return render(request,
                          '../templates/etatSommes.html',
                          {'years': years,
                           'events': events,
                           'moduls': modules,
                           'CIN': CIN})


def ficheCours(request, CIN):
    if request.method == 'POST':
        profil = Person.objects.get(pk=CIN)
        year = request.POST.get("year")
        module = request.POST.get("module")
        event = request.POST.get("event")
        if event is None:
            data = coursdata(year, module)
            print(data)
            print(data[0].date.year)
            return render(request,
                          '../templates/ficheCours.html',
                          {'year': year,
                           'module': module})
        else:
            return render(request,
                          '../templates/ficheCours.html',
                          {'event': event})
