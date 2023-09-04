from django.urls import path
from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.home),
    path('registrarCurso/', views.registrarCurso ),
    path('eliminacionCurso/<codigo>', views.eliminarCurso),
    path('edicionCurso/<codigo>', views.edicionCurso),
    path('editarCurso/', views.editarCurso)

]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
