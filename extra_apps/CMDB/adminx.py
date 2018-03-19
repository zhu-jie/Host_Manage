import xadmin
from xadmin import views

from .models import Host,HostGroup

class BaseSettings(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = "Cnjie后台管理系统"
    site_footer = "Cnjie在线"
    menu_style = "accordion"


class HostAdmin(object):
    list_display = ['hostname','os_type','status']
    search_fields = ['hostname','os_type','status']
    list_fields = ['hostname','os_type','status']


xadmin.site.register(Host,HostAdmin)
