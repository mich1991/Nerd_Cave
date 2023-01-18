from .models import Comment, Contact, Post
from django import forms
from django_summernote.widgets import SummernoteWidget


class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('text',)


class ContactForm(forms.ModelForm):
	class Meta:
		model = Contact
		fields = ('name', 'email', 'message')


class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		# exclude = ('likes', 'author', 'slug',)
		exclude = ('likes',)
		widgets = {
			'content': SummernoteWidget(),
		}
