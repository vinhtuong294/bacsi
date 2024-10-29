"""
from django.contrib.admin import AdminSite
from reviews.models import (Publisher, Contributor, Book,
BookContributor, Review)
class BookrAdminSite(AdminSite):
    title_header = 'Bookr Admin'
    site_header = 'Bookr administration'
    index_title = 'Bookr site admin'
admin_site = BookrAdminSite(name='bookr')
# Register your models here.
admin_site.register(Publisher)
admin_site.register(Contributor)
admin_site.register(Book)
admin_site.register(BookContributor)
admin_site.register(Review)
"""

# Register your models here.
"""
from django.contrib import admin
from reviews.models import (Publisher, Contributor, Book, BookContributor, Review, BookAdmin)
# Register your models here.
admin.site.register(Publisher)
admin.site.register(Contributor)
admin.site.register(Book, BookAdmin)
admin.site.register(BookContributor)
admin.site.register(Review)
"""
from django.contrib import admin
from .models import Contributor


class ContributorAdmin(admin.ModelAdmin):
    # Hiển thị 2 cột: Last Names và First Names trong danh sách contributor
    list_display = ('last_names', 'first_names')

    # Cho phép tìm kiếm theo Last Names và First Names, sử dụng __startswith cho Last Names
    search_fields = ('last_names__startswith', 'first_names')

    # Thêm bộ lọc theo Last Names ở cạnh phải
    list_filter = ('last_names',)


admin.site.register(Contributor, ContributorAdmin)