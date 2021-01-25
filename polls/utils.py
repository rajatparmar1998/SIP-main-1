from django.contrib.auth import logout
from django.shortcuts import render, redirect

# Create your views here.

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages



def not_sign_in(function):
	def wrap(request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect('home')
		else:
			return function(request, *args, **kwargs)
	return wrap



def is_sign_in(function):
	def wrap(request, *args, **kwargs):
		if request.user.is_authenticated:
			return function(request, *args, **kwargs)
		else:
			return redirect('signin')
	return wrap
