from django.shortcuts import render, render_to_response, RequestContext

def home(request):
	return render(request, 'Fingeso/home.html',{})
