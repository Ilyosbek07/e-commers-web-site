from modeltranslation.translator import TranslationOptions, register

from posts.models import PostModel


@register(PostModel)
class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)
