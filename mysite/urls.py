"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from mysite.views import HomeView,UserCreateView,UserCreateDoneTV #user 뷰 for auth 추가
from django.conf import settings # photo app 위한 추가
from django.conf.urls.static import static #photo app 위한 추가
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')), #auth 위해  추가
    path('accounts/register/', UserCreateView.as_view(), name='register'), #auth register위해  추가
    path('accounts/register/done/', UserCreateDoneTV.as_view(), name='register_done'), #auth register->done  추가
    # shkim
    path('', HomeView.as_view(), name='home'),
    path('bookmark/', include('bookmark.urls')),
    path('blog/', include('blog.urls')),
    path('namecard/',include('namecard.urls')), #namecard url 추가
    path('student/',include('student.urls')), #student url 추가
    path('photo/',include('photo.urls')), # photo url 추가
    path('sugang/',include('sugang.urls')), # sugang url 추가
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) ##

