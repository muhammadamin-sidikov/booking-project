from django.contrib import admin
from .models import Field

@admin.register(Field)
class FieldAdmin(admin.ModelAdmin):
    list_display = ('name', 'joylashuv', 'narx')
    search_fields = ('name', 'joylashuv')

