#-*-coding:utf-8-*-
from django.shortcuts import render,HttpResponse,render_to_response,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User,Group 
from core.models import Group_info,Suggestion,User_info
from django.contrib.auth import *
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
#from django.template import RequestContext
#from django.template import RequestContext
# Create your views here.

def index(request):
	return render(request,'index.html')

def register(request):
	if request.method == 'POST':
		username = request.POST.get('username',None)
		password = request.POST.get('password',None)
		email = request.POST.get('email',None)
		user=User.objects.create_user(username=username,password=password,email=email)
		
		
		status = {'register_info':user}
		return render_to_response('user.html',status)    #change user.html content
	else:
		return render(request,'signin.html')
def login_views(request):
	
	if request.method == 'POST':
	
		username = request.POST.get('username',None)
		password = request.POST.get('password',None)
		user = authenticate(username=username,password=password)
		status = {'login_info':user}
		if user is not None:
			login(request,user)
			return render_to_response('user.html',status)  
		else:
			status = {'info':'username or password is wrong'}
			return render_to_response('login.html',status)   
	else:
		return render(request,'login.html')

@csrf_exempt		
@login_required	
def user_center(request):
	status={'info':'','information':''}          #the class has already yuyue
	user=request.user
	a=User.objects.get(username=user)
	data=a.group_info_set.all()
	#print data.subject
	status['info']=data
	
	data2=a.user_info_set.all()
	print data
	print data2
	status['information']=data2
	return render_to_response('user.html',status)

@csrf_exempt	
@login_required
def change_info(request):
	if request.method == 'POST':
		gender=request.POST.get('gender',None)
		city=request.POST.get('city',None)
		school=request.POST.get('school',None)
		birthday=request.POST.get('birthday',None)
		email=request.POST.get('email',None)
		
		information={'change_result':''}
		
		
		user=request.user
		a=User.objects.get(username=user)
		data=a.user_info_set.all()
		if data.count()==1:
			#change
			data.update(gender=gender,city=city,school=school,birthday=birthday,email=email)
			
			
		else:
			#create and connect
			info=User_info.objects.create(gender=gender,city=city,school=school,birthday=birthday,email=email)
			info.users_info.add(a)
		information['change_result']='change success'
		return render_to_response('user.html',information)
	
@csrf_exempt	
@login_required
def class_info(request):
	status={'info':''}
	data=Group_info.objects.all()
	status['info']=data
	
	return render_to_response('class.html',status)
@csrf_exempt
@login_required
def appoint(request):
	status={'info':''}
	user=request.user
	
	items=Group_info.objects.all()
	for item in items:
		if request.POST.has_key(item.teacher):
			status['info']=item
	a=User.objects.get(username=user)
	b=status['info']
	b.groups_info.add(a)
	sta={'appoint_info':'successfully appointed!'}
	return render_to_response('class.html',sta)
	
@csrf_exempt	
@login_required
def teacher_list(request):
	status={'info':''}
	data = Group_info.objects.all()
	status['info']=data
	return render_to_response('teacher.html',status)  

@csrf_exempt	
@login_required	
def suggestion(request):
	if request.method == 'POST':
		sug=request.POST.get('suggestion',None)
		Suggestion.objects.create(suggestion=sug)
		status={'info':'多谢您的宝贵意见，我们一定会更加努力！'}
		return render_to_Response('suggestion',status)
	else:
		return render(request,'suggestion.html')

