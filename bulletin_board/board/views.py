from django.views import generic

from .models import Post, User
from .forms import PostCreateForm


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
