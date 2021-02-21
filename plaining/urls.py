from django.urls import path
from . import views

urlpatterns = [
    # auth
    path('login/', views.loginUser, name='loginUser'),
    path('logout/', views.logoutUser, name='logoutUser'),
    # route
    path('createPerson/', views.createPerson, name='createPerson'),
    path('listPerson/', views.listPerson, name='listPerson'),
    path('', views.homePage, name='homePage'),
    path('Profil/<str:CIN>', views.Profil, name='Profil'),
    path('updateProfil/<str:CIN>', views.updateProfil, name='updateProfil'),
    path('removeProfil/<str:CIN>', views.removeProfil, name='removeProfil'),
    path('addCours/<str:CIN>', views.addCours, name='addCours'),
    path('etatSommes/<str:CIN>', views.etatSommes, name='etatSommes'),
    path('addDeplacement/<str:CIN>', views.addDeplacement, name='addDeplacement'),
    path('updateCours/<int:id>', views.updateCours, name='updateCours'),
    path('updateDeplacement/<int:id>', views.updateDeplacement, name='updateDeplacemenet'),
    path('removeCours/<int:id>', views.removeCours, name='removeCours'),
    path('removeDeplacement/<int:id>', views.removeDeplacement, name='removeDeplacement'),
    path('ficheCours/<str:CIN>', views.ficheCours, name='ficheCours'),

]
