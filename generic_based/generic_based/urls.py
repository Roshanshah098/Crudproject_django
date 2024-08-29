from django.contrib import admin  
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from enrollin import views  # Import your views module from enrollin app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('enrollin/', include('enrollin.urls')),  # Include the URLs from the enrollin app
    #path('', views.add_show, name='home'),
    path("api-auth/", include("rest_framework.urls"))
    # Define the root path to point to a view
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

