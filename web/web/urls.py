from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^web/', include('OneADay.urls', namespace="web")),
    url(r'^admin/', include(admin.site.urls)),
]