from django.urls import path
from . import views

urlpatterns = [
	path('', views.HomePageView.as_view(), name='home'),
	path('posts', views.PostListView.as_view(), name='posts_list'),
	path('posts/<slug:slug>', views.PostDetailView.as_view(), name='post_detail'),
	path('like/<slug:slug>', views.PostLikeView.as_view(), name='post_like'),
	path('about-us', views.AboutPageView.as_view(), name='about_us'),
	path('contact-us', views.ContactPageView.as_view(), name='contact_us'),
	path('author-panel', views.AuthorPostListView.as_view(), name='author_post_list'),
	path('author-panel/add', views.AuthorAddPostView.as_view(), name='author_add_post'),
	path('author-panel/edit/<int:pk>', views.AuthorEditPostView.as_view(), name='author_edit_post'),
	path('author-panel/delete/<int:pk>', views.AuthorEditPostView.as_view(), name='author_delete_post')
]
