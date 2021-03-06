
"""champaksite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from bookslab import views as vw
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
	path("img/", views.getImage),
	path("prevnext/", views.prevnext),
path("hello/", views.hello),
path("weather/", views.weather),
path("add/",views.add),
path("sum/",views.sum),
path("loops/",views.loop),
path("", views.index),
path("many", vw.many),
path("update", vw.update),
path("insert", vw.insert),
path("all", vw.all),
path("find/", vw.find),
path("delete/", vw.delete),
 path('bookimage/', views.book_image_view),
 path('success', views.success),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)