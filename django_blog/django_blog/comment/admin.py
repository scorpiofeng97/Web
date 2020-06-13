from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('target','content','nickname','website','created_time')



