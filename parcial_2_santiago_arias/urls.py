from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from vacation_summer import views as vacation_summer_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('sites_vacations/', vacation_summer_views.list_sites_db, name='sites_vacations'),

    path('sites_vacations/save/', vacation_summer_views.save_site, name='save_site'),
    path('sites_vacations/form_save/', vacation_summer_views.form_go, name='form_save'),
    url(r'^sites_vacations/delete_data(?P<id>\d+)/$', vacation_summer_views.delete_data, name='delete_data'),
]
