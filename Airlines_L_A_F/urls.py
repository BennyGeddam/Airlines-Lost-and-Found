from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

# main urls:
      # admin url
          # main app (spot_items) urls
            # registerer (sub) urls
                  # Airport staff (sub) urls
                      # media files in development
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('spot_items.urls')),
    path('registerer/', include('registerer.urls')),
    path('airport_staff/', include('airport_staff.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
