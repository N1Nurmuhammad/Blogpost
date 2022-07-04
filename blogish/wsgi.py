from whitenoise import WhiteNoise
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blogish.settings')

application = get_wsgi_application()

application = WhiteNoise(application, root="/static")
application.add_files("static")
#  prefix="more-files/"