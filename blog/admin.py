from django.contrib import admin
from .models import *

admin.site.register(Category)
admin.site.register(Entry)
admin.site.register(Comments)


def make_published(modeladmin, request, queryset):
    queryset.update(status='published')


make_published.short_description = "Mark selected stories as published"


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'create_date', 'status')
    prepopulated_fields = {'slug': ('title',)}
    actions = [make_published]
