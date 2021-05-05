"""platzigram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
# Django
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

# Platzigram
from platzigram import views as local_views

#view media
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    #
    path('hello-word/', local_views.hello_word, name='hello_world'),
    path('sorted/', local_views.sort_integers, name='sort'),
    path('hi/<str:name>/<int:age>', local_views.say_hi, name='hi'),
    #posts paths
    path('', include(('posts.urls','posts'), namespace='posts')),
    #user paths
    path('users/', include(('users.urls','users'),namespace='users'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
