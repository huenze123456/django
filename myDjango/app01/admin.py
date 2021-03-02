from django.contrib import admin
from app01.models import Test01

# Register your models here.
# 啊啊啊啊啊啊啊啊啊
class Test01Admin(admin.ModelAdmin):
    list_display = ['name','age','tel']


# 注册模型类
admin.site.register(Test01,Test01Admin)
