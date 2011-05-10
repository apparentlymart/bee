from django.contrib import admin

from bee.models import *


admin.site.register(Image)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'slug', 'created')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)


class AuthorSiteAdmin(admin.ModelAdmin):
    list_display = ('author', 'site')

admin.site.register(AuthorSite, AuthorSiteAdmin)


class TemplateAdmin(admin.ModelAdmin):
    list_display = ('author', 'purpose')

admin.site.register(Template, TemplateAdmin)
