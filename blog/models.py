from django.db import models


class Author(models.Model):
    name = models.CharField(default='', max_length=256, verbose_name='Name')
    email = models.EmailField(default='', verbose_name='Email')
    password = models.CharField(default='', max_length=256, verbose_name='Password')
    birthday = models.DateField(verbose_name='Birthdate')
    avatar = models.ImageField(default='img/default.jpg', verbose_name='Avatar')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'


class QuestionManager(models.Manager):
    def find_id(self, quest_id):
        return self.get(id=quest_id)

    def find_tag(self, quest_tag):
        return self.filter(tags__contains=quest_tag)


class Question(models.Model):
    title = models.CharField(max_length=1024, verbose_name='Title')
    text = models.TextField(verbose_name='Text', default="")
    date_create = models.DateField(auto_now_add=True, verbose_name='Create date')
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    tags = models.CharField(max_length=1024, verbose_name='Tags')
    objects = QuestionManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'


class AnswerManager(models.Manager):
    def find_id(self, ans_id):
        return self.get(id=ans_id)


class Answer(models.Model):
    text = models.TextField(verbose_name='Text', default="")
    date_create = models.DateField(auto_now_add=True, verbose_name='Create date')
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    objects = AnswerManager()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Answer'
        verbose_name_plural = 'Answers'
