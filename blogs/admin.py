from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

class UserModelAdmin(UserAdmin):
    icon_name = "account_circle"
    list_display = ['username','email','rol_id',]
    list_filter = ['rol_id']

    fieldsets = UserAdmin.fieldsets + (
        ('Información Adicional', {
            'fields': ('rol',),
        }),
    )

class BlogPostAdmin(admin.ModelAdmin):
    icon_name = 'card_travel'
    list_display = ['title', 'author_id','content',]
    list_filter = ['title', 'author_id', 'created_at']

class CommentAdmin(admin.ModelAdmin):
    icon_name = 'card_travel'
    list_display = ['post', 'author_id','content',]
    list_filter = ['post', 'author_id', 'created_at']

class TagAdmin(admin.ModelAdmin):
    icon_name = 'card_travel'
    list_display = ['name',]
    list_filter = ['name']


admin.site.register(User, UserModelAdmin)
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Tag, TagAdmin)
