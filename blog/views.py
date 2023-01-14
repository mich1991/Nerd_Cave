from django.shortcuts import render
from django.views.generic import View
from .models import Post


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


class PostListView(View):
	def get(self):
		pass


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