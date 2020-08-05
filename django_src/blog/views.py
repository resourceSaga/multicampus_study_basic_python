from django.shortcuts import render
from django.http import HttpResponse
# from django.contrib.auth.models import User

from blog.models import Post
from django.utils import timezone
# Post 목록
def post_list(request):

    # name = 'Django'
    # return HttpResponse(
    #     '''
        # <h2>Post List</h2>
        # <p>
        #     웰컴 {name}!!!
        # <br>
        #     {content}
        # </p>
        # '''.format(name=name, content=request.user)
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})
    # )

