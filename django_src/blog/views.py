from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.models import User

from .models import Post
from .forms import PostModelForm
from .forms import PostForm

# Post 삭제
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')

# Post 수정
def post_edit(request, pk):
    # DB에서 해당 pk와 매칭되는 Post 객체를 가져온다.
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        # 수정처리
        form = PostModelForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = User.objects.get(username=request.user.username)
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        # 수정하기 전에 데이터 읽어옴
        form = PostModelForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form':form})

# Post 등록
def post_new(request):
    if request.method == 'POST':
        # input Form data and save request
        # form = PostModelForm(request.POST)
        form = PostForm(request.POST)
        # Form data is valid
        if form.is_valid():
            print(form.cleaned_data)
            post = Post.objects.create(author=User.objects.get(username=request.user.username), published_date=timezone.now(),title=form.cleaned_data['title'], text=form.cleaned_data['text'])
            # title, text filed value call
            # post = form.save(commit=False)
            # post.author = User.objects.get(username=request.user.username)
            # post.published_date = timezone.now()
            # insert DB
            # post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        #등록 Form 보여준다.
        form = PostModelForm()
    return render(request, 'blog/post_edit.html', {'form':form})


# Post 상세조회
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post':post})


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

