import os
import sys
sys.path.append('/home/sipp11/projects')
sys.path.append('/home/sipp11/projects/osqa')

os.environ["DJANGO_SETTINGS_MODULE"] = "osqa.settings"

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

