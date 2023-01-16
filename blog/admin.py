from django.contrib import admin
from .models import Post, Category, Comment, Contact
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
	prepopulated_fields = {'slug': ('title',)}
	summernote_fields = ('content')
	list_filter = ('category', 'author', 'created_on', 'status')
	list_display = ('title', 'category', 'author', 'created_on',)
	search_fields = ['title', 'content']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
	list_filter = ('user', 'post')
	list_display = ('user', 'text', 'post')
	search_fields = ['text', 'user_name', 'email']


@admin.register(Contact)
class CommentAdmin(admin.ModelAdmin):
	list_filter = ('name', 'email', 'date')
	list_display = ('name', 'email', 'message', 'date')
	search_fields = ['name', 'email', 'message']


admin.site.register(Category)