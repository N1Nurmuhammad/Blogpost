
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', include('blog.urls', 'main_app')),
    path('i18n/', include('django.conf.urls.i18n')),
    # rest
    path('api/blog/', include('blog.api.urls')),
    path('api/accounts/', include('accounts.api.urls'))
]

urlpatterns += i18n_patterns(
    path('main/', include('blog.urls')),
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)