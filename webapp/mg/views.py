from django.db import models
from django.http import request
from django.http.response import Http404
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import redirect as rd
from allauth.socialaccount.models import SocialAccount
from .models import User,Doctor,forum
from .final import solve

def isDoctor(request):
    if  request.user.is_anonymous: return False
    return Doctor.objects.filter(usr=request.user).count()==1

def Index(request):
    to = 'patient' if not isDoctor(request) else 'doctor'
    return render(request,'index.html',{'to':to})

def InfoView(request):
    print(SocialAccount._meta.get_fields())
    print(request.user)
    print(SocialAccount.objects.filter(user=request.user)[0])
    return HttpResponse(SocialAccount.objects.filter(user=request.user)[0].extra_data)

def DoctorView(request):
    currentUser = request.user
    q = Doctor.objects.filter(usr=currentUser)
    if(len(q)==0):        
        POST = request.POST
        a  = SocialAccount.objects.get(user=currentUser)
        if POST:
            Doctor.objects.create(id=currentUser.id,phno=POST['phno'],pincode=POST['zip'],sp=POST['sp'],lno=POST['lno'],social=a,usr=currentUser)
            return DoctorDashboard(request)
        return render(request,'dr_form.html')
    else:
        return DoctorDashboard(request)

def DoctorDashboard(request):
    obj = Doctor.objects.get(id=request.user.id)
    if request.POST:
        if 'online' in request.POST.keys():  
            obj.online = True
            obj.save()
        elif 'offline' in request.POST.keys():          
            obj.online = False
            obj.save()    
    return render(request,'dr_dashboard.html',{'online':obj.online})

def PatientView(request):
    return render(request,'user_dashboard.html')

def RecommendView(request):
    ans,sym = None,None
    if request.POST:
        sym = request.POST['Symptoms']
        ans = solve(sym)[0:5]      
    #t = User.objects.filter(usr=request.user)
    # print('Length',len(t))
    
    return render(request,'results.html',{'ans':ans,'sym':sym})#{'names':names,'ids':ids,'pins':pins})

def DetailView(request):
    if not request.GET:
        names = []
        ids = []
        pins = []
        pics = []
        ph = []
        q = Doctor.objects.filter(online=True).select_related()
    
        for obj in q:
            print('Fileds',obj.social._meta.get_fields())       
            names.append(obj.social.extra_data['name'])
            ids.append(obj.id)
            pins.append(obj.pincode)
            pics.append(obj.social.extra_data['picture'])
            ph.append(obj.phno)
        return render(request,'calldoc.html',{'data':zip(ids,names,pins,pics,ph)})

    obj = Doctor.objects.get(id=request.GET['id'])
    dict = {
        'name':obj.social.extra_data['name'],
        'pin':obj.pincode,
        'sp':obj.sp,
        'ph':obj.phno,
        'lno':obj.lno,
        'hospital':obj.hospital
    }
    return render(request,'dr_details.html',dict)

def Forum(request):
    i1,i2=[],[]
    q1,q2=[],[]
    a2=[]
    un = forum.objects.filter(answer__exact='unanswerd')
    for ob in un:
        i1.append(ob.id)
        q1.append(ob.question)
    aa = forum.objects.exclude(answer__exact='unanswerd')
    for ob in aa:
        i2.append(ob.id)
        q2.append(ob.question)
        a2.append(ob.answer)
    return render(request,'forums.html',{'uns':zip(i1,q1),'ans':zip(i2,q2,a2),'doc':isDoctor(request)})

def CreateQuestion(request):
    if request.POST:
        q = request.POST['question']
        forum.objects.create(question = q)
        return rd('/forum')
    return render(request,'askquestion.html')
def GiveAnd(request):
    
    if  request.POST:
        i = request.POST['id']
        ans = request.POST['answer']
        obj = forum.objects.get(id=i)
        obj.answer=ans
        obj.save()
        return rd('/forum')
    if  request.GET:
        i = request.GET['id']
        return render(request,'getanswer.html',{'id':i})
    return rd('/forum')
'''
ManyToOneRel: socialaccount.socialtoken>, <django.db.models.fields.AutoField: id>, <django.db.models.fields.related.ForeignKey: user>, <django.db.models.fields.CharField: provider>, <django.db.models.fields.CharField: uid>, <django.db.models.fields.DateTimeField: last_login>, <django.db.models.fields.DateTimeField: date_joined>, <allauth.socialaccount.fields.JSONField: extra_data>
'''

