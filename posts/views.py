from django.shortcuts import render
from django.shortcuts import render, redirect
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from .models import Post
from moviepy.video.io.VideoFileClip import VideoFileClip

# Create your views here.

def upload(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('desc')
        video_file = request.FILES['file_video']

        # Save the video file to disk
        path = default_storage.save('videos/' + video_file.name, ContentFile(video_file.read()))

        # Create a new Video object
        video = Post.objects.create(
            title=title,
            discription=description,
            video_file=path,
            author=request.user
        )
        # Generate a thumbnail and save it to the Video object
        video_file_path = video.video_file.path
        thumbnail_path = 'thumbnails/' + video.video_file.name.split('/')[-1].split('.')[0] + '.jpg'

        # clip = VideoFileClip(video_file_path)
        # print(clip)
        # thumbnail = clip.resize(300, 300).to_image()
        # thumbnail.save(thumbnail_path)
        # clip.close()
        video.thumbnail = thumbnail_path
        video.save()
        return redirect('home')
    return render(request, 'upload.html')

def posts(request):
    posts = Post.objects.filter().values()
    return render(request, 'posts.html', {'posts': posts})

def myPosts(request):
    posts = Post.objects.filter(author=request.user.id).values()
    return render(request, 'posts.html', {'posts': posts})

def singlePost(request, id):
    post = Post.objects.get(id=id)
    print(post)
    return render(request, 'singlePost.html', {'post': post})