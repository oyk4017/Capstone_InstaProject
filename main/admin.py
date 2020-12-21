from django.contrib import admin
from .models import InsertDb #모델에서 resource를 불러온다

#출력할 resourceAdmin 클래스를 만든다.
class ResourceAdmin(admin.ModelAdmin):
    display = ('c_no')

#클래스를 어드민 사이트에 등록한다.
admin.site.register(InsertDb, ResourceAdmin)
# Register your models here.
