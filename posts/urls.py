"""posts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
#from django.urls import path, include
from django.urls.conf import path, include
#from main import views

#app_name= 'main' #app_name 해당 앱에 별칭을 부여함. (별칭 사용은 코드를 줄이기 위함)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    #path('', views.get,name='get'),
    #url 뒤에 index가 붙으면 views의 index함수를 호출하라는 뜻. name='index'는 별칭을 부여함.
]
