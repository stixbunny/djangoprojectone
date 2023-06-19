"""
URL configuration for djangoprojectone project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from venta import views as venta_views
from edificio import views as edificio_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', venta_views.inicio , name='index'),
    path('edificios/', edificio_views.edificio , name='properties'),
    path('edificios/entretenimiento/<int:property_id>', edificio_views.detail_ent, name="detail_ent"),
    path('edificios/industrial/<int:property_id>', edificio_views.detail_ind, name="detail_ind"),
    path('edificios/residencial/<int:property_id>', edificio_views.detail_res, name="detail_res"),
    path('contacto/', venta_views.contacto , name='contact'),
    path('acerca/', venta_views.acerca , name='about'),
]
