from django.db import models


# Create your models here.


class AuthorModel(models.Model):
    first_name = models.CharField(max_length=250, unique=False)
    last_name = models.CharField(max_length=250, unique=False)
    status = models.BooleanField(default=True)
    avatar = models.ImageField(max_length=250, null=True, unique=False)
    email = models.EmailField(max_length=250, unique=True)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name, self.last_name, self.status, self.created_at, self.updated_at

class CategoryModel(models.Model):
    name = models.CharField(max_length=250, unique=True)
    status = models.BooleanField(default=True)
    image = models.ImageField(max_length=250, unique=False)
    description = models.TextField(default="")
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id

class PostModel(models.Model):
    author = models.ForeignKey(AuthorModel,on_delete=models.DO_NOTHING)
    category = models.ForeignKey(CategoryModel, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=250, unique=True)
    content = models.TextField(default="")
    description = models.TextField(max_length=250, unique=False,default="")
    image = models.ImageField(max_length=250, unique=False, null=True, blank=True)
    slug = models.SlugField(max_length=250, unique=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title, self.slug, self.status, self.created_at, self.updated_at, self.description
    

