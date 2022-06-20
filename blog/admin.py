from django.contrib import admin
from blog.models import PagesModel, CommentModel
from modeltranslation.admin import TranslationAdmin


class PagesCustomAdmin(admin.ModelAdmin):
    list_display = ('title_uz', 'title_en', 'title_ru', 'created_date')

    class Meta:
        verbose_name = "Pages"


class NewsAdmin(PagesCustomAdmin, TranslationAdmin):
    pass

admin.site.register(PagesModel, NewsAdmin)


admin.site.register(CommentModel)

