from audioop import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render


def home(request):
	title = "my Chat"
	return render(request,'pages/main.html',{"title":title})

def chat(request):
	if request.method != "POST":
		return HttpResponseRedirect(reverse('index'))
	else:
		title = "Chat Room"
		username = request.POST.get('username')
		return render(request,'pages/chat.html',{"title":title,"username":username})