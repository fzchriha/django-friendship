from django.urls import path, re_path
from .views import (
	users_list, 
	profile_view, 
	send_friend_request, 
	cancel_friend_request,
	accept_friend_request,
	delete_friend_request,
	profile
	)

urlpatterns = [
	path('', users_list, name='list'),
	path('(?P<pk>\d+)/', profile_view, name='profile_view'),
    re_path(r'^profile$', profile),
    re_path(r'^friend-request/send/(?P<id>[\w-]+)/$', send_friend_request),
    re_path(r'^friend-request/cancel/(?P<id>[\w-]+)/$', cancel_friend_request),
    re_path(r'^friend-request/accept/(?P<id>[\w-]+)/$', accept_friend_request),
    re_path(r'^friend-request/delete/(?P<id>[\w-]+)/$', delete_friend_request),
]
