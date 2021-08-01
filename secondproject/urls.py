from django.contrib import admin
from django.urls import path, re_path
from django.urls.conf import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', include('q_and_a.urls')),
    path('blog/', include('blog.urls')),
    path('profiles/', include('profiles.urls')),
    path('froala_editor/',include('froala_editor.urls')),
    path('community/', include('community.urls')),
    path('tutorials/', include('tutorials.urls')),
    # re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)