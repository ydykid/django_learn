from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField('title', max_length=256)

    content = models.TextField('content', blank=True, null=True)

    category = models.CharField('category', max_length=50, blank=True)

    pub_date = models.DateTimeField('publish-time',
        auto_now_add=True, editable=True)
    update_date = models.DateTimeField('update-time',
        auto_now=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-pub_date']
