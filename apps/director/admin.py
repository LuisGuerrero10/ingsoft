from django.contrib import admin
from apps.director.models import Estudiante, Convocatoria, Proveedor, Asistente, Duenos_cafeteria, Director


admin.site.register(Estudiante)
admin.site.register(Convocatoria)
admin.site.register(Proveedor)
admin.site.register(Asistente)
admin.site.register(Director)
admin.site.register(Duenos_cafeteria)