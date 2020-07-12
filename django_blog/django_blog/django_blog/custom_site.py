from django.contrib.admin import AdminSite


class CustomSite(AdminSite):
    site_header = 'Django_blog'
    site_title = 'Django_blog管理后台'
    index_title = '首页'


custom_site = CustomSite(name='cus_admin')

