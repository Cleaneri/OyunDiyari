import os
import sys
from django.conf import settings
from django.core.management import execute_from_command_line
from django.http import HttpResponse
from django.urls import path
from django.db import models

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

if not settings.configured:
    settings.configure(
        DEBUG=True,
        SECRET_KEY="downhub-yeni-gizli-anahtar",
        ROOT_URLCONF=__name__,
        ALLOWED_HOSTS=["*"],
        DATABASES={
            "default": {
                "ENGINE": "django.db.backends.sqlite3",
                "NAME": os.path.join(BASE_DIR, "db.sqlite3"), # Doğrudan ana klasörde oluşturuyoruz
            }
        },
        INSTALLED_APPS=["__main__"],
    )

class IndirmeLinki(models.Model):
    baslik = models.CharField(max_length=200)
    url = models.URLField()

    class Meta:
        app_label = '__main__'

def ana_sayfa(request):
    try:
        linkler = IndirmeLinki.objects.all()
    except Exception:
        linkler = []
        
    html = "<h1>DownHub Canli ve Ucretsiz!</h1><ul>"
    for link in linkler:
        html += f"<li>{link.baslik}: {link.url}</li>"
    html += "</ul>"
    return HttpResponse(html)

urlpatterns = [
    path("", ana_sayfa),
]

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

if __name__ == "__main__":
    execute_from_command_line(sys.argv)
