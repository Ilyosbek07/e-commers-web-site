from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils.translation import ugettext_lazy as _


class AuthorModel(models.Model):
    name = models.CharField(max_length=50, verbose_name=_('name'))
    avatar = models.ImageField(upload_to='authors', verbose_name=_('avatar'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('author')
        verbose_name_plural = _('authors')


class PostTagModel(models.Model):
    title = models.CharField(max_length=20, verbose_name=_('title'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('tag')
        verbose_name_plural = _('tags')


class PostModel(models.Model):
    title = models.CharField(max_length=30, verbose_name=_('title'))
    image = models.ImageField(upload_to='post-image', verbose_name=_('image'))
    banner = models.ImageField(upload_to='banner', verbose_name=_('banner'))
    content = RichTextUploadingField(null=True, verbose_name=_('content'))
    author = models.ForeignKey(
        AuthorModel,
        on_delete=models.PROTECT,
        related_name='posts', verbose_name=_('author')
    )
    tags = models.ManyToManyField(
        PostTagModel,
        related_name='posts', verbose_name=_('tags')
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.title

    def get_comments(self):
        return self.comment.order_by('-created_at')

    def get_prev(self):
        return self.get_previous_by_created_at()

    def get_next(self):
        return self.get_next_by_created_at()

    class Meta:
        verbose_name = _('post')
        verbose_name_plural = _('posts')


class TeamModel(models.Model):
    name = models.CharField(max_length=25, verbose_name=_('name'))
    job = models.CharField(max_length=55, verbose_name=_('job'))
    image = models.ImageField(null=True, verbose_name=_('image'))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('team')
        verbose_name_plural = _('teams')


class PartnersModel(models.Model):
    title = models.CharField(max_length=20, verbose_name=_('title'))
    image = models.FileField(null=True, verbose_name=_('image'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('partner')
        verbose_name_plural = _('partners')


class CommentModel(models.Model):
    post = models.ForeignKey(
        PostModel,
        related_name='comment',
        on_delete=models.CASCADE,
        verbose_name=_('post')
    )
    name = models.CharField(max_length=255, verbose_name=_('name'))
    email = models.EmailField(verbose_name=_('email'))
    phone = models.CharField(
        max_length=25, null=True, blank=True,
        verbose_name=_('phone'))
    comment = models.TextField(verbose_name=_('comment'))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('comment')
        verbose_name_plural = _('comments')
