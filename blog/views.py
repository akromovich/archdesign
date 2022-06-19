from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Post,Work,Articles,Contacts,News,Aboutcomp
from .forms import ArticlesForm,ContactsForm


def index(request):
	work = Work.objects.all()
	context = {
		"works":work
	}
	return render(request,'blog/index.html',context)


def about(request):
	work = Work.objects.all()
	about = Aboutcomp.objects.all()[:2]
	context = {
		"works":work,
		'abouts':about
	}
	return render(request,'blog/about.html',context)

def contacts(request):
	form = ContactsForm()
	error = ''
	if request.method == 'POST':
		form = ContactsForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('contacts')
		else:
			error = "Форма была неверной"
	context = {
		'error': error,
		'form': form
	}
	return render(request,'blog/contact.html',context)

def news(request):
	newsi = News.objects.all().order_by('-date')[:10]
	context = {
		'news':newsi,
	}
	return render(request,'blog/news.html',context)

def project(request,pk):
	art = Articles.objects.all()
	error = ''
	if request.method == 'POST':
		form = ArticlesForm(request.POST)
		if form.is_valid():
			form.save()

		else:
			error = "Форма была неверной"

	post = Post.objects.get(id=pk)
	form  =ArticlesForm()
	context = {
		'forms':form,
		"all_posts":post,
		'error':error,
		'arts':art
	}
	return render(request,'blog/project.html',context)

def projects(request):
	posts = Post.objects.all()
	pipi = Post.objects.all()[:3]
	context = {
		'posts':posts,
		'pipis':pipi
	}
	return render(request,'blog/projects.html',context)

def services(request):
	return render(request,'blog/services.html')

def projects(request):
	posts = Post.objects.all()
	pipi = Post.objects.all()[:3]
	context = {
		'posts':posts,
		'pipis':pipi
	}
	return render(request,'blog/projects.html',context)
