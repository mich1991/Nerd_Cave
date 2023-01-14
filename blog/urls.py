from django.urls import path
from .views import HomePageView, PostDetailView, PostListView, PostLikeView, AboutPageView, ContactPageView
urlpatterns = [
	path('', HomePageView.as_view(), name='home'),
	path('posts', PostListView.as_view(), name='posts_list'),
	path('posts/<slug:slug>', PostDetailView.as_view(), name='post_detail'),
	path('like/<slug:slug>', PostLikeView.as_view(), name='post_like'),
	path('about-us', AboutPageView.as_view(), name='about_us'),
	path('contact-us', ContactPageView.as_view(), name='contact_us')
]
