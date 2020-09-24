from django.contrib import admin
from django.urls import path,include
from django.conf import settings # new
from django.conf.urls.static import static # new
from portfolio import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('blog/',include('blog.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)