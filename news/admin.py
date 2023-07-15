from django.contrib import admin
from .models import News

class NewsAdmin(admin.ModelAdmin):
    list_display = ('subject', 'author', 'get_create_date')
    list_filter = ('create_date',)
    search_fields = ('subject', 'author')
    fieldsets = [
        ('제목 필드', {'fields': ('subject',)}),
        ('글쓴이 필드', {'fields': ('author',)}),
        ('내용 필드', {'fields': ('content',)}),
        ('작성일 필드', {'fields': ('create_date',)}),
    ]

    def get_create_date(self, obj):
        return obj.create_date.strftime('%Y-%m-%d')
    get_create_date.short_description = '작성일'

admin.site.register(News, NewsAdmin)
