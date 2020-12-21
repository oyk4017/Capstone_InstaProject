#main 서브앱의 urls
#서브앱의 urls는 같은 위치의 view.py의 함수로 연결을 담당 (path)
#같은 위치의 view.py를 식별 못하면 import

# from django.contrib import admin
# from django.urls import path, include
# from main import views

# urlpatterns = [
#     path('', views.home, name='home'),
# ]

from django.urls.conf import path
from main import views 

from django.conf.urls.static import static
from django.conf import settings

app_name= 'main' # app_name은 해당 앱에 별칭을 부여함. (별칭 사용은 코드를 줄이기위함)

urlpatterns=[

    path('',views.get,name='get'),

    # url뒤에 index가 붙으면 views의 index함수를 호출하라는 뜻. name='index'는 별칭을 부여함.
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)