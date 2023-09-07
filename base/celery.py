from __future__ import absolute_import, unicode_literals

import os

from celery import Celery
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "base.settings.dev")


app = Celery("base")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.conf.enable_utc = True
app.conf.update(timezone=getattr(settings, "TIME_ZONE"))


app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    pass
