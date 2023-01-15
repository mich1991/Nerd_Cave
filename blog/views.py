from django.shortcuts import render
from django.views.generic import View, ListView
from .models import Post, Category
from django.contrib.auth.models import User


class HomePageView(View):
	def get(self, request):
		published_posts = Post.objects.filter(status='1')
		ps5_latest_posts = published_posts.filter(category__name='PS5').order_by('created_on')[:4]
		xbox_latest_posts = published_posts.filter(category__name='XBOX').order_by('created_on')[:4]
		switch_latest_posts = published_posts.filter(category__name='SWITCH').order_by('created_on')[:4]

		ctx = {
			'ps5': {
				'latest_post': ps5_latest_posts.first(),
				'recent_posts': ps5_latest_posts[1:]
			},
			'xbox': {
				'latest_post': xbox_latest_posts.first(),
				'recent_posts': xbox_latest_posts[1:]
			},
			'switch': {
				'latest_post': switch_latest_posts.first(),
				'recent_posts': switch_latest_posts[1:]
			},
		}
		return render(request, 'blog/index.html', ctx)


class PostListView(ListView):
	model = Post
	template_name = 'blog/post_list'
	paginate_by = 12

	def get_queryset(self, **kwargs):
		url_query = self.request.GET
		base_query = super().get_queryset().filter(status='1')
		if url_query.get('title'):
			base_query = base_query.filter(title__icontains=url_query.get('title'))
		if url_query.get('category'):
			base_query = base_query.filter(category=url_query.get('category'))
		if url_query.get('author'):
			base_query = base_query.filter(author__username__icontains=url_query.get('author'))
		return base_query

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['categories'] = Category.objects.all()
		context['form'] = {
			'title': self.request.GET.get('title') if self.request.GET.get('title') else '',
			'category': self.request.GET.get('category') if self.request.GET.get('category') else '',
			'author': self.request.GET.get('author') if self.request.GET.get('author') else ''
		}
		print(context['form'])
		return context


class PostDetailView(View):
	def get(self):
		pass


class PostLikeView(View):
	def get(self):
		pass


class AboutPageView(View):
	def get(self):
		pass


class ContactPageView(View):
	def get(self):
		pass