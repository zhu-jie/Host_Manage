from django.conf.urls import url,include
from django.contrib import admin
import xadmin

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^xadmin/', xadmin.site.urls),
]
