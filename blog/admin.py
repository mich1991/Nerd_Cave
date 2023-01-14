from django.contrib import admin
from .models import Post, Category, Comment
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
	prepopulated_fields = {'slug': ('title',)}
	summernote_fields = ('content')
	list_filter = ('category', 'author', 'created_on',)
	list_display = ('title', 'category', 'author', 'created_on',)


admin.site.register(Category)
admin.site.register(Comment)