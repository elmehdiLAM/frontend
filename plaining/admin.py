from django.contrib import admin
from .models import Person, Cours, Deplacement


class PlainingAdmin(admin.ModelAdmin):
    readonly_fields = ('date_ajout',)


admin.site.register(Person)
admin.site.register(Cours, PlainingAdmin)
admin.site.register(Deplacement)


