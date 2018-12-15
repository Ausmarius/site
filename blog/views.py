from django.shortcuts import render
from django.http import HttpResponse
from . models import Post

def posts_list(request):

	#----Посылаем файл по адресу в index.html через словарь---------------
	# f = open('D://1.txt', 'r'
	# 	# , encoding="utf-8"
	# 	)
	# string = f.read()
	# f.close()
	#---------------------------------------------------------------------

	# x = ["Serg", "Anton", "Sasha", "Olya", "Igor", "Maxim"]
	# n = {"names":x}#Если создать переменную и загрузить в нее словарь, то ее можно использовать далее
	# return render(request, 'blog/index.html', context = n)#Context позволяет использовать переменную

	posts = Post.objects.all()
	return render(request, 'blog/index.html', context = {'posts': posts})



def post_detail(request, slug):
	post = Post.objects.get(slug__iexact=slug)	
	return render(request, 'blog/post_detail.html', context = {'post': post})