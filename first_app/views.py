from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, webpage, AccessRecord, TestUsers
from . import forms
from first_app.forms import NewUser
# Create your views here.

def index(request): 

	webpage_list = AccessRecord.objects.order_by('date')
	date_dict = {'access_records': webpage_list}

	myDict = { 'insert_me' : "Hello, Apple, inc is hiring me"}
	return render(request, 'first_app/index.html',context=date_dict )

def help(request):
	myHelpDict = { 'help_me' : "this is cry for an help"}
	return render(request, 'first_app/help.html', context=myHelpDict)

def form_name_view(request):
	form = forms.FormName()

	if request.method == 'POST':
		form = forms.FormName(request.POST)

		if form.is_valid():
			#DO SOMETHING CODE
			print("Validation Success!")
			print("Name: "+form.cleaned_data['name'])
			print("Email: "+form.cleaned_data['email'])
			print("Text: "+form.cleaned_data['text'])

	return render(request,'first_app/form.html', {'form':form})

def users(request):
	form = NewUser()

	if request.method == "POST":
		form = NewUser(request.POST)

		if form.is_valid():
			print("submit Success!")
			print("Name: "+form.cleaned_data['firstName'])
			print("Email: "+form.cleaned_data['email'])
			print("Text: "+form.cleaned_data['lastName'])
			form.save(commit=True)
			return index(request)
		else:
			print('ERROR FORM INVALID')

	return render(request, 'first_app/users.html', {'form':form})








