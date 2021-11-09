from django.contrib import admin

from posts.models import PostTagModel, AuthorModel, PostModel, PartnersModel, TeamModel, CommentModel


@admin.register(AuthorModel)
class AuthorModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name']


@admin.register(PostTagModel)
class PostTagModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title']


@admin.register(PartnersModel)
class PartnerModelAdmin(admin.ModelAdmin):
    list_filter = ['created_at']
    list_display = ['title', 'image', 'created_at']
    search_fields = ['name']


@admin.register(TeamModel)
class TeamModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name', 'job']


@admin.register(PostModel)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_at']
    list_filter = ['author', 'tags', 'created_at']
    search_fields = ['title']
    autocomplete_fields = ['author', 'tags']

@admin.register(CommentModel)
class CommentModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name', 'email']
