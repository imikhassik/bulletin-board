from django.views import generic

from .models import Post


class PostList(generic.ListView):
    model = Post
    ordering = '-created'
    template_name = 'board/post_list.html'
    context_object_name = 'post_list'
