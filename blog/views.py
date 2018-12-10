from django.shortcuts import render
from django.http import HttpResponse

def posts_list(request):

	#----Посылаем файл по адресу в index.html через словарь---------------
	# f = open('D://1.txt', 'r'
	# 	# , encoding="utf-8"
	# 	)
	# string = f.read()
	# f.close()
	#---------------------------------------------------------------------

	x = ["Serg", "Anton", "Sasha", "Olya", "Igor", "Maxim"]
	n = {"names":x}#Если создать переменную и загрузить в нее словарь, то ее можно использовать далее
	return render(request, 'blog/index.html', context = n)#Context позволяет использовать переменную

