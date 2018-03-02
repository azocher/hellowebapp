from django.contrib import admin

# import models
from collection.models import Thing

# set up automated slug creation
class ThingAdmin(admin.ModelAdmin):
    model = Thing
    list_display = ('name', 'description',)
    prepopulated_fields = {'slug': ('name',)}

# register models
admin.site.register(Thing, ThingAdmin)
