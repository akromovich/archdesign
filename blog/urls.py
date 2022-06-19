from django.conf.urls.i18n import i18n_patterns
from django.urls import path
from . import views



urlpatterns = [
	path('',views.index,name='index'),
	path('about/',views.about,name='about'),
	path('contacts/',views.contacts,name='contacts'),
	path('news/',views.news,name='news'),
	path('projects/',views.projects,name='projects'),
	path('services/',views.services,name='services'),
	path('post/<int:pk>/',views.project,name='project'),
]








