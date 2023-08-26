from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy

from .models import Post, Comment, Suggested
from .forms import PostForm, CommentForm, SuggestedForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class BlogHome(ListView):
    model = Post
    context_object_name = 'posts'
    extra_context = []

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['pinned'] = Post.objects.filter(published_date__isnull=False, is_pinned=True)
        context_data['all'] = Post.objects.filter(published_date__isnull=False, is_pinned=False).order_by(
            '-published_date')
        return context_data


class PostDetail(DetailView):
    model = Post
    extra_context = []


class PostAdd(CreateView):
    form_class = PostForm
    template_name = 'blog/post_edit.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostEdit(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_edit.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class BlogDrafts(ListView):
    model = Post
    template_name = 'blog/post_draft_list.html'
    context_object_name = 'posts'
    extra_context = []

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('-created_date')


@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)


@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('home')


def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})


@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)


@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk)


def suggest_news(request):
    if request.method == "POST":
        form = SuggestedForm(request.POST)
        if form.is_valid():
            news = form.save(commit=False)
            news.save()
            return redirect('home')
    else:
        form = SuggestedForm()
    return render(request, 'blog/suggest_news.html', {'form': form})


@login_required
def suggested_list(request):
    newses = Suggested.objects.all()
    return render(request, 'blog/suggested_list.html', {'newses': newses})


# class RegisterUser(CreateView):
#     form_class = RegisterUserForm
#     template_name = 'registration/register.html'
#     success_url = reverse_lazy('login')

@login_required
def post_pin(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.pin()
    return redirect('home')


@login_required
def post_unpin(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.unpin()
    return redirect('home')
