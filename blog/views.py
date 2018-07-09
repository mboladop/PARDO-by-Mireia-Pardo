#from django.shortcuts import render, redirect, get_object_or_404
#from django.http import HttpResponse
#from .models import Post
#from .forms import BlogPostForm
#
## Create your views here.
#def get_posts(request):
#    posts = Post.objects.all()
#    return render(request, "posts/blog-posts.html", {'posts': posts})
#    
#def post_detail(request, pk):
#    post= get_object_or_404(Post, pk=pk)
#    post.views += 1
#    post.save()
#    return render(request, 'posts/postdetail.html', {'post':post})
#    
#def create_or_edit_post(request, pk=None):
#    """
#    Create a view that allows us to create
#    or edit a post depending if the Post ID
#    is null or not
#    """
#    post = get_object_or_404(Post, pk=pk) if pk else None
#    if request.method == "POST":
#        form = BlogPostForm(request.POST, request.FILES, instance=post)
#        if form.is_valid():
#            post = form.save()
#            return redirect(post_detail, post.pk)
#    else:
#        form = BlogPostForm(instance=post)
#    return render(request, 'posts/blog-posts-form.html', {'form': form})