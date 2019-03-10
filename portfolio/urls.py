from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import jobs.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', jobs.views.home, name='home'),
    path('blog/', include('blog.urls')),    #wszystkie url co w blogu będą zaczynać się od blog/
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#z pliku settings.py żeby móc otwierać media które są w folderze media i które mają url /media/
#tak jak jest napisane w settings (co moglibyśmy zmienić)
