from django.contrib import admin
from .models import DocumentType, LostDocument

admin.site.register(DocumentType)
admin.site.register(LostDocument)
