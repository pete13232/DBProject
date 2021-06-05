from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.models import User
from .models import  Member

def unauthenticated_user(view_func):
	def wrapper_func(request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect('/')
		else:
			return view_func(request, *args, **kwargs)

	return wrapper_func

def allowed_users(allowed_roles=[]):
	def decorator(view_func):
		def wrapper_func(request, *args, **kwargs):

			role = None
			if request.user.role != None :
				role = request.user.role

			if role in allowed_roles:
				return view_func(request, *args, **kwargs)
			else:
				return HttpResponse('You are not authorized to view this page')
		return wrapper_func
	return decorator

def admin_only(view_func):
	def wrapper_function(request, *args, **kwargs):
		role = None
		if request.user.role != None:
			role = request.user.role

		if role != 'admin':
			return redirect('/')

		if role == 'admin':
			return view_func(request, *args, **kwargs)

	return wrapper_function