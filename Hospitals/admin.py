from django.contrib import admin
from django.apps import apps


# Register your models here.
app = apps.get_app_config('Hospitals')

for mname, model in app.models.items():
    admin.site.register(model)

