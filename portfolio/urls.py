from django.contrib import admin
from django.urls import path
import jobs.views  # import app views # Function view example
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', jobs.views.homepage, name='home'),
    path('jobs/<int:job_id>', jobs.views.detail, name='detail'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
