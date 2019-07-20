from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

import jobs.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', jobs.views.homepage, name='home'),
    path('jobs/<int:job_id>', jobs.views.detail, name='detail'),
    path('', include('django_prometheus.urls')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
