from django.views import generic
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse

from .models import Post, User, Response
from .forms import PostCreateForm, ResponseCreateForm


class PostList(generic.ListView):
    model = Post
    ordering = '-created'
    template_name = 'board/post_list.html'
    context_object_name = 'post_list'


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'board/post_detail.html'


class PostCreate(generic.CreateView):
    model = Post
    template_name = 'board/post_edit.html'
    form_class = PostCreateForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = User.objects.get(id=self.request.user.id)
        self.object.save()
        result = super().form_valid(form)
        return result


class PostUpdate(generic.UpdateView):
    model = Post
    template_name = 'board/post_edit.html'
    form_class = PostCreateForm


class ResponseList(generic.ListView):
    model = Response
    template_name = 'board/response_list.html'
    context_object_name = 'response_list'
    ordering = '-created'


class ResponseDetail(generic.DetailView):
    model = Response
    template_name = 'board/response_detail.html'


class ResponseCreate(generic.CreateView):
    model = Response
    template_name = 'board/response_create.html'
    form_class = ResponseCreateForm
    success_url = '/success/'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = User.objects.get(id=self.request.user.id)
        self.object.post = Post.objects.get(id=self.kwargs['pk'])
        self.object.save()
        result = super().form_valid(form)
        return result


class SuccessView(generic.TemplateView):
    template_name = 'board/success.html'


def accept_response(request, pk):
    response = Response.objects.get(pk=pk)
    response.status = 'A'
    response.save()
    return HttpResponseRedirect(reverse('response_list'))


def deny_response(request, pk):
    response = Response.objects.get(pk=pk)
    response.status = 'D'
    response.save()
    return HttpResponseRedirect(reverse('response_list'))
