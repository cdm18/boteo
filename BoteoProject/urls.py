"""
URL configuration for BoteoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from facturacion import views
from publicaciones.views import community_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('', include('main.urls')),  #  principal
    path('spaces/', include('sports_spaces.urls')),
    path('my_areas/', include('areas.urls')),
    path('billing/', views.gestion_pagos, name='gestion_pagos'),
    path('billing/crear_factura/', views.crear_factura, name='crear_factura'),
    path('eliminar_pago/<int:id>/', views.eliminar_pago, name='eliminar_pago'),
    path('billing/marcar_pagado/<int:id>/', views.marcar_pagado, name='marcar_pagado'),
    path('community/', community_view, name='community'),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)