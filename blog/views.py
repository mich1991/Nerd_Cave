from django.contrib.auth.decorators import user_passes_test, login_required
from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.generic import View, ListView, DeleteView, TemplateView
from django.utils.text import slugify
from .models import Post, Category
from .forms import CommentForm, ContactForm, PostForm

# Grants access only for staff members
decorators = [user_passes_test(lambda u: u.is_staff, login_url='home',)]


class HomePageView(View):
	def get(self, request):
		published_posts = Post.objects.filter(status='1')
		ps5_latest_posts = published_posts.filter(category__name='PS5').order_by('-created_on')[:4]
		xbox_latest_posts = published_posts.filter(category__name='XBOX').order_by('-created_on')[:4]
		switch_latest_posts = published_posts.filter(category__name='SWITCH').order_by('-created_on')[:4]

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
	template_name = 'blog/post_list.html'
	paginate_by = 12

	def get_queryset(self, **kwargs):
		url_query = self.request.GET
		base_query = super().get_queryset().filter(status='1')
		if url_query.get('title'):
			base_query = base_query.filter(title__icontains=url_query.get('title'))
		if url_query.get('category'):
			base_query = base_query.filter(category__name=url_query.get('category'))
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
		return context


class PostDetailView(View):

	def get(self, request, slug):
		queryset = Post.objects.filter(status=1)
		post = get_object_or_404(queryset, slug=slug)
		comments = post.comments.order_by("-created_on")
		liked = False
		if post.likes.filter(id=self.request.user.id).exists():
			liked = True

		ctx = {
			'post': post,
			'comments': comments,
			'comment_form': CommentForm(),
			'liked': liked
		}
		return render(request, 'blog/post_detail.html', ctx)

	def post(self, request, slug):

		post = get_object_or_404(Post, slug=slug)
		comments = post.comments.order_by("-created_on")
		liked = False
		if post.likes.filter(id=self.request.user.id).exists():
			liked = True

		comment_form = CommentForm(data=request.POST)
		if comment_form.is_valid():
			comment_form.instance.user = request.user
			comment = comment_form.save(commit=False)
			comment.post = post
			comment.save()
			comment_form = CommentForm()
		else:
			comment_form = CommentForm()

		ctx = {
				'post': post,
				'comments': comments,
				'comment_form': comment_form,
				'liked': liked
		}
		return render(request, 'blog/post_detail.html', ctx)


class ContactPageView(View):
	def get(self, request):
		form = ContactForm()
		ctx = {'form': form}
		return render(request, 'blog/contact.html', ctx)

	def post(self, request):
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save()
			form = ContactForm()
			ctx = {
				'form': form,
				'success': True
				}
			return render(request, 'blog/contact.html', ctx)
		ctx = {'form': form}
		return render(request, 'blog/contact.html', ctx)


class AboutPageView(TemplateView):
	template_name = 'blog/about.html'


@method_decorator(login_required, name='dispatch')
class PostLikeView(View):
	"""
	Likes only works for log in user, if not logged in would be redirected by decorator
	"""
	def post(self, request, slug):
		post = get_object_or_404(Post, slug=slug)

		if post.likes.filter(id=request.user.id).exists():
			post.likes.remove(request.user)
		else:
			post.likes.add(request.user)
		return HttpResponseRedirect(reverse('post_detail', args=[slug]))


@method_decorator(decorators, name='dispatch')
class AuthorPostListView(ListView):
	"""GET List of posts that's belongs to an author"""
	model = Post
	template_name = 'blog/author/author_post_list.html'
	paginate_by = 10

	def get_queryset(self, **kwargs):
		url_query = self.request.GET
		base_query = super().get_queryset().filter(author=self.request.user)
		if self.request.user.is_superuser:
			base_query = super().get_queryset().filter()
		if url_query.get('title'):
			base_query = base_query.filter(title__icontains=url_query.get('title'))
		if url_query.get('category'):
			base_query = base_query.filter(category__name=url_query.get('category'))
		return base_query

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['categories'] = Category.objects.all()
		context['form'] = {
			'title': self.request.GET.get('title') if self.request.GET.get('title') else '',
			'category': self.request.GET.get('category') if self.request.GET.get('category') else '',
		}
		return context


@method_decorator(user_passes_test(lambda u: u.is_staff, login_url='home',), name='dispatch')
class AuthorAddPostView(View):
	def get(self, request):
		ctx = {
			'form': PostForm()
		}
		return render(request, 'blog/author/author_add_post.html', ctx)

	def post(self, request):
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			post = form.save(commit=False)
			post.slug = slugify(post.title)
			post.author = request.user
			post.save()
			form = PostForm()
			ctx = {
				'form': form,
				'success': True
			}
			return render(request, 'blog/author/author_add_post.html', ctx)
		ctx = {'form': form}
		return render(request, 'blog/author/author_add_post.html', ctx)


@method_decorator(user_passes_test(lambda u: u.is_staff, login_url='home',), name='dispatch')
class AuthorEditPostView(View):
	def get(self, request, pk):
		post = Post.objects.get(pk=pk)
		ctx = {
			'form': PostForm(instance=post),
			'edit': True,
		}
		return render(request, 'blog/author/author_add_post.html', ctx)

	def post(self, request, pk):
		post_instance = Post.objects.get(pk=pk)
		form = PostForm(request.POST, request.FILES, instance=post_instance)
		if form.is_valid():
			post = form.save(commit=False)
			post.slug = slugify(post.title)
			post.author = request.user
			post.save()
			ctx = {
				'form': form,
				'success': True,
				'edit': True,
			}
			return render(request, 'blog/author/author_add_post.html', ctx)
		ctx = {
			'form': form,
			'edit': True,
		}
		return render(request, 'blog/author/author_add_post.html', ctx)


@method_decorator(user_passes_test(lambda u: u.is_staff, login_url='/',), name='dispatch')
class AuthorDeletePostView(DeleteView):
	template_name = 'blog/author/author_delete_post.html'

	def get_object(self):
		pk = self.kwargs.get('pk')
		author_post = Post.objects.filter(author=self.request.user)
		return get_object_or_404(author_post, pk=pk)

	def get_success_url(self):
		return reverse('author_post_list')
