from django.shortcuts import get_object_or_404, render
from django.views import generic, View
from django.conf import settings
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import permission_required

from .forms import CommentForm
from .models import Post


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 3


# class PostDetail(generic.DetailView):
#     model = Post
#     template_name = 'post_detail.html'


def post_detail(request, slug):
    template_name = "post_detail.html"
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True).order_by("-created_on")
    new_comment = None
    # Comment posted
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(
        request,
        template_name,
        {
            "post": post,
            "comments": comments,
            "new_comment": new_comment,
            "comment_form": comment_form,
        },
    )

@login_required
@permission_required('blog.can_mark_returned')
@permission_required('blog.can_edit')
def my_view(request):
     if not request.user.email.endswith('@example.com'):
        return redirect('/login/?next=%s' % request.path)

class MyView(LoginRequiredMixin, View):
    permission_required = 'blog.can_mark_returned'
    # Or multiple permissions
    permission_required = ('blog.can_mark_returned', 'blog.can_edit')
    # Note that 'blog.can_edit' is just an example
    # the blog application doesn't have such permission!