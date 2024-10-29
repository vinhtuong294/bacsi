from django.contrib.admin import AdminSite

class CustomAdminSite(AdminSite):
    site_header = "c8admin"
    site_title = "Django site admin"
    index_title = "c8admin"
    logout_template = "comment8or/logged_out.html"

admin_site = CustomAdminSite(name='custom_admin')