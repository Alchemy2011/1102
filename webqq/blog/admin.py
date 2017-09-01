# coding:utf-8
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from models import *
# Register your models here.

class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'is_superuser')
    list_filter = ('is_superuser',)
    fieldsets = ( # 编辑的时候字段
        ('基本', {'fields': ('username','password','nick','avatar','friend')}),
        ('权限', {'fields': ('is_superuser','is_staff','is_active','groups', 'user_permissions')}),
    )
    add_fieldsets = ( # 添加记录的时候字段
    (None, {
        'classes': ('wide',),
        'fields': ('username', 'password1', 'password2','friend','is_staff','is_active','is_superuser')}
        ),
    )
admin.site.register(User,UserAdmin)
