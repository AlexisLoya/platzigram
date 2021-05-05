"""Post views"""
# Django
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
# Utilities
from datetime import datetime
# Models
from posts.models import Post
# Forms
from posts.forms import PostForm
old_posts = [
    {
        'title': 'Whatsapp 2',
        'user': {
            'name': 'Alexis Loya',
            'nickname': '@LasterLG117',
            'picture': 'https://pbs.twimg.com/profile_images/1107499827917656064/OotAmKIk_400x400.png',

        },
        'timestamp': datetime.now().strftime('%b %dth, %y - %H:%M hrs'),
        'photo': 'https://pbs.twimg.com/media/EseKu3PW8AApkdC?format=png&name=360x360',
    },
    {
        'title': 'SuperLiga Mx',
        'user': {
            'name': 'Ayanami',
            'nickname': '@asuukkka',
            'picture': 'https://pbs.twimg.com/profile_images/1285349343860580352/DBkB35Pn_400x400.jpg',
        },
        'timestamp': datetime.now().strftime('%b %dth, %y - %H:%M hrs'),
        'photo': 'https://pbs.twimg.com/media/EzhGcdFWEAIryC2?format=jpg&name=large',
    },
    {
        'title': 'he volvido a tuiter',
        'user': {
            'name': 'eoto002',
            'nickname': '@eoto002',
            'picture': 'https://pbs.twimg.com/profile_images/1366519767310467072/uWNnFGYh_400x400.jpg',
        },
        'timestamp': datetime.now().strftime('%b %dth, %y - %H:%M hrs'),
        'photo': 'https://pbs.twimg.com/media/EzilSBiUUAE0D_X?format=jpg&name=900x900',
    },
    {
        'title': 'Cocina cocina',
        'user': {
            'name': 'Asuka Daily',
            'nickname': '@asuka_dailycl',
            'picture': 'https://pbs.twimg.com/profile_images/1011999448971579392/wFuXbWyE_400x400.jpg',
        },
        'timestamp': datetime.now().strftime('%b %dth, %y - %H:%M hrs'),
        'photo': 'https://pbs.twimg.com/media/EziHKetXoAA2vai?format=png&name=900x900',
    }
]


class PostFeedView(LoginRequiredMixin, ListView):
    """Return all published posts"""

    template_name = 'posts/feed.html'
    model = Post
    ordering = ('-created')
    paginate_by = 5
    context_object_name = 'posts'


class PostDetailView(LoginRequiredMixin, DetailView):
    """Post detail """
    template_name = 'posts/detail.html'
    slug_field = 'id'
    slug_url_kwarg = 'post_id'
    queryset = Post.objects.all()


class CreatePostview(LoginRequiredMixin, CreateView):
    """Create a new post"""
    template_name = 'posts/new.html'
    form_class = PostForm
    success_url = reverse_lazy('posts:feed')

    def get_context_data(self, **kwargs):
        """Add user an profile to context"""
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['profile'] = self.request.user.profile
        return context


@login_required
def list_post(request):
    posts = (Post.objects.all().order_by('-created'))
    return render(request, 'posts/feed.html', {'posts': posts})


# @login_required
# def create_post(request):
#     """Create a new post view"""
#     if request.method == 'POST':
#         form = PostForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('posts:feed')
#     else:
#         form = PostForm()

#     return render(
#         request=request,
#         template_name='posts/new.html',
#         context={
#             'form':form,
#             'user':request.user,
#             'profile':request.user.profile
#         }
#     )
