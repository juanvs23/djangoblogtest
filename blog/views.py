from django.shortcuts import render

from website.views import pages

from .models import PostModel

import random

from slugify import slugify

# Create your views here.

def singleBlogView(request,slug):
    post = PostModel.objects.get(slug=slug)
    return render(request, "pages/single-blog.html",{
        "pages": pages,
        "pageData": {
            "title": post.title,
            "content": post.content,
            "author": post.author,
            "banner": post.image,
            "url": "/blog/archive/" + slug,
            "meta_description": post.description,
            "active": False
        }
    })

def blogView(request):
    posts = PostModel.objects.all()
    return render(request, "pages/blog.html",{
        "pages": pages,
        "pageData": pages[3],
        "posts": posts
    })

def createBlogView(request):
    post_title = "title"+str(random.randint(1, 100))
    the_slug = slugify(post_title)
    post = PostModel.objects.create(title=post_title , description="Description",slug=the_slug)
    return render(request, "pages/single-blog.html",{
        "pages": pages,
        "pageData": {
            "title": "Create a post",
            "url": "/blog/create",
            "meta_description": "Create a post Page",
            "active": False
        }
    })

def deletePost(request,id):
    post = PostModel.objects.get(id=id)
    post.delete()
    return render(request, "pages/single-blog.html",{
        "pages": pages,
        "pageData": {
            "title": "Delete a post",
            "url": "/blog/delete",
            "meta_description": "Delete a post Page",
            "active": False
        }
    })