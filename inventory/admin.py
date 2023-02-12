from django.contrib import admin

from .models import storage_location, storage_container, storage_item

# Register your models here.
admin.site.register(storage_location)

admin.site.register(storage_container)

admin.site.register(storage_item)