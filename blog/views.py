from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from django.views.generic.edit import FormMixin
from blog.forms import PostForm, AuthUserForm, RegisterUserForm, CommentForm
from blog.middleware import get_current_user
from blog.models import Post, Comment
from django.template import Context, Template


class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'items'


class PostCreateView(CreateView):
    login_url = reverse_lazy('login_page')
    model = Post
    template_name = 'blog/post_create.html'
    context_object_name = 'items'
    form_class = PostForm
    success_url = reverse_lazy('post_list')


class PostDetailView(DetailView, FormMixin):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
    form_class = CommentForm

    def get_success_url(self, **kwargs):
        return reverse_lazy('post_detail', kwargs={'pk': self.get_object().id})

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.post = self.get_object()
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)


class PostDeleteView(DeleteView):
    model = Post
    context_object_name = 'post'
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('post_list')


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_edit.html'
    success_url = reverse_lazy('post_list')


class MyProjectLoginView(LoginView):
    template_name = 'blog/login.html'
    form_class = AuthUserForm
    success_url = reverse_lazy('post_list')

    def get_success_url(self):
        return self.success_url


class MyProjectLogoutView(LogoutView):
    next_page = reverse_lazy('post_list')


class RegisterUserView(CreateView):
    model = User
    form_class = RegisterUserForm
    template_name = 'blog/register.html'
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        form_valid = super().form_valid(form)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        auth_user = authenticate(username=username, password=password)
        login(self.request, auth_user)
        return form_valid


def update_comment_status(request, pk, type):
    item = Comment.objects.get(pk=pk)
    if type == 'public':
        item.status = True
        item.save()
        template = 'blog/comment_item.html'
        context = {'item': item, 'status_comment': 'Комментарий опубликован'}
        return render(request, template, context)

    elif type == 'delete':
        item.delete()
        return HttpResponse('''
                <div class="alert alert-success">Комментарий удален</div>
        ''')

    return HttpResponse('1')
