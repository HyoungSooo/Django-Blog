from blog.urls import api as blog_api
from .api import api
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSitemap

sitemaps = {
    'posts': PostSitemap
}


api.add_router('/math/', blog_api)

urlpatterns = [
    path('', include('blog.urls', namespace='blog')),
    path('admin/', admin.site.urls),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitempas.views.sitemap'),
    path('markdownx/', include('markdownx.urls')),
    path("api/", api.urls)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
