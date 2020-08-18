from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import CommentForm
from django.contrib import messages
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# Create your views here.


def home(request):
    posts = Post.objects.all()
    commentform = CommentForm()
    context = {
        'title': 'home Page',
        'posts': posts,
        'commentform': commentform
    }

    return render(request, 'mysite/home.html', context=context)


def comments(request, pk):
    target_post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        commentform = CommentForm(data=request.POST)
        if commentform.is_valid():
            new_comment = commentform.save(commit=False)
            new_comment.author = request.user
            new_comment.post = target_post
            new_comment.save()
            messages.success(request, "Comment Created")
            return redirect('mysite-home')
    return redirect("mysite-home")


def about(request):
    return render(request, 'mysite/about.html', {'title': 'About page'})


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        return True if post.author == self.request.user else False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        return True if post.author == self.request.user else False
