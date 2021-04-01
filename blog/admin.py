from django.contrib import admin
from .models import *

admin.site.register(Category)
admin.site.register(Entry)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'create_date')
    prepopulated_fields = {'slug': ('title',)}
