from django import forms
from .models import Person, Cours, Deplacement


class Personform(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['CIN',
                  'nom',
                  'prenom',
                  'email',
                  'numPhone',
                  'statue',
                  'etat',
                  'sexe',
                  'maxHoraireMois',
                  'maxHoraireJour']


class Coursform(forms.ModelForm):
    class Meta:
        model = Cours
        fields = ['etablisement',
                  'date',
                  'nombreheure',
                  'module']


class Deplacementform(forms.ModelForm):
    class Meta:
        model = Deplacement
        fields = ['type_deplacement',
                  'self_veicule',
                  'date_depart',
                  'date_retour',
                  'evenement',
                  'kilometrage',
                  'depenseEstimeJour',
                  'description']


