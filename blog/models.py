from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=256, verbose_name='Name')
    birthday = models.DateField(verbose_name='Birthdate')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'AuthorS'


class Article(models.Model):
    title = models.CharField(max_length=1024, verbose_name='Title')
    text = models.TextField(verbose_name='Text', default="")
    date_create = models.DateField(auto_now_add=True, verbose_name='Create date')
    author = models.ForeignKey('Author', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'ArticleS'
