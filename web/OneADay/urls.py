from django.conf.urls import url

from OneADay.templates.views import auth_views, account_views


urlpatterns = [
	url(r'^$', account_views.index, name='index'),
	url(r'^register/', auth_views.register, name='register'),
	url(r'^login/', auth_views.login_user, name='login'),
	url(r'^logout/', auth_views.logout_user, name='logout'),
	url(r'^add-interest/', account_views.add_interest),
	url(r'^remove-interest/', account_views.remove_interest)
]