import imp
from operator import imod
from modeltranslation.translator import register, TranslationOptions
from blog.models import PagesModel

@register(PagesModel)
class PagesModelTranslation(TranslationOptions):
    fields = ('title', 'body')
