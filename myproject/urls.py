from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from myproject import settings
from portifolio import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portifolio.urls')),
    path(r'accounts/login/',  views.logar_usuario, name="logar_usuario"),
    path('internacao/', include('internacao.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

