from django.db import models
from helpers.models import BaseModel
from author.models import Author

# Create your models here.
CREATED = "created"
MODERATION = "moderation"
PUBLISHED = "published"
POST_STATUS = (
    (CREATED, "created"),
    (MODERATION, "moderation"),
    (PUBLISHED, "published"),
)


class Category(BaseModel):
    title = models.CharField(max_length=128)
    slug = models.CharField(max_length=128, unique=True)
    icon = models.FileField(upload_to="category/")
    post_count = models.IntegerField(default=0)


class Tag(BaseModel):
    title = models.CharField(max_length=128)
    slug = models.CharField(max_length=128, unique=True)


class Post(BaseModel):
    title = models.CharField(max_length=128, verbose_name='Nomi')
    slug = models.CharField(max_length=128, unique=True)
    content = models.TextField()
    sub_content = models.CharField(max_length=128)
    image = models.ImageField(upload_to="post/", null=True)

    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name='posts')
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, related_name='posts')
    tags = models.ManyToManyField(Tag, related_name='posts')

    published_date = models.DateField(null=True)
    status = models.CharField(max_length=15, choices=POST_STATUS)
    read_min = models.IntegerField(default=0)
    views_count = models.PositiveIntegerField(default=0)

    is_popular = models.BooleanField(default=False)
