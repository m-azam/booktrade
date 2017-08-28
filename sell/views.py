from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import HttpResponseRedirect, HttpResponseRedirect
from django.urls import reverse
from .models import Book, Subject
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
number_of_books = 2
def index(request):
	sub_objs = Subject.objects.all().values('subject_name').distinct();
	return render(request, 'sell/index.html', {'sub_objs':sub_objs})

def postbook(request):
	return render(request, 'sell/post.html')

def postb(request):
	count = 0
	while number_of_books > 0:
		count = count + 1
		course = "course"
		sem = "sem"
		number = "number"
		subject = "subject" + str(count)
		bookname = "bookname" + str(count)
		price = "price" + str(count)
		global number_of_books
		try:
			course = request.POST[course]
		except (KeyError):
			return render(request, 'sell/post.html',{'errorc':'Select course'})
		try:
			sem = request.POST[sem]
		except (KeyError):
			return render(request, 'sell/post.html',{'errors':'Select sem'})
		number = request.POST[number]
		if len(number) == 0:
			return render(request, 'sell/post.html',{'errorn':'Enter a valid phone number'})
		if len(number) > 11:
			return render(request, 'sell/post.html',{'errorn':'Enter a valid phone number'})
		subject1 = request.POST[subject]
		if len(subject1) == 0:
			return render(request, 'sell/post.html',{'errors1':'Enter valid Subject!'})
		bookname1 = request.POST[bookname]
		if len(bookname1) == 0:
			return render(request, 'sell/post.html',{'errorbn1':'Enter valid Book name'})
		price1 = request.POST[price]
		if len(price1) == 0:
			return render(request, 'sell/post.html',{'errorp1':'Enter valid price'})
		q = Book(book_name = bookname1,book_course = course,book_sem = sem,book_sub = subject1,book_price = price1,book_pno=number)
		q.save()
		e = Subject(subject_name = subject1)
		e.save()
		number_of_books = number_of_books - 1
	return render(request, 'sell/post.html',{'successx':'Your Books were successfully submitted!'})
def ajaxsend(request):
	global number_of_books
	number_of_books = int(request.GET.get('number_of_books', None))
	data = {
	    'number_of_books': number_of_books
	}
	return JsonResponse(data)
def search(request):
	course = request.POST['selectmenu2']
	sem = request.POST['selectmenu1']	
	subd = request.POST['subject_autocomplete2']
	global book_objs
	book_objs = Book.objects.filter(book_course = course).filter(book_sem = sem).filter(book_sub = subd)
	paginator = Paginator(book_objs, 2)
	page = request.GET.get('page')
	try:
		books = paginator.page(page)
	except PageNotAnInteger:
		books = paginator.page(1)
	except EmptyPage:
		books = paginator.page(paginator.num_pages)
	if not book_objs:
		return render(request, 'sell/search.html', {'books':books, 'error':'None of the books match your search criteria.'})
	else:
		return render(request, 'sell/search.html', {'books':books})
def searchm(request):
	course = request.POST['selectmenu2m']
	sem = request.POST['selectmenu1m']	
	subd = request.POST['subject_autocomplete2m']
	global book_objs
	book_objs = Book.objects.filter(book_course = course).filter(book_sem = sem).filter(book_sub = subd)
	paginator = Paginator(book_objs, 2)
	page = request.GET.get('page')
	try:
		books = paginator.page(page)
	except PageNotAnInteger:
		books = paginator.page(1)
	except EmptyPage:
		books = paginator.page(paginator.num_pages)
	if not book_objs:
		return render(request, 'sell/search.html', {'books':books, 'error':'None of the books match your search criteria.'})
	else:
		return render(request, 'sell/search.html', {'books':books})
def searchx(request, page):
	paginator = Paginator(book_objs, 2)
	page = request.GET.get('page')
	try:
		books = paginator.page(page)
	except PageNotAnInteger:
		books = paginator.page(1)
	except EmptyPage:
		books = paginator.page(paginator.num_pages)
	return render(request, 'sell/search.html', {'books':books})




