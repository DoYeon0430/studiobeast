from django.contrib import admin
from .models import News

class NewsAdmin(admin.ModelAdmin):
    list_display = ('subject', 'author', 'create_date')
    list_filter = ('create_date',)
    search_fields = ('subject', 'author')
    fieldsets = [
        ('제목 필드', {'fields': ('subject',)}),
        ('글쓴이 필드', {'fields': ('author',)}),
        ('내용 필드', {'fields': ('content',)}),
        ('작성일 필드', {'fields': ('create_date',)}),
    ]

admin.site.register(News, NewsAdmin)
