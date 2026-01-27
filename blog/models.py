import uuid
from django.db import models

from users.models import BlogUser
from django.utils import timezone


# Create your models here.
class Post(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable=False)
    user = models.ForeignKey(BlogUser, on_delete = models.CASCADE)
    title = models.CharField(max_length = 600)
    content = models.TextField()
    likes = models.ManyToManyField(BlogUser, related_name="post_likes")
    # post.add(user)
    # post.save()
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title