from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from home.models import semester_info
from .models import *
from django.db.models import Q
# Create your views here.
def home(request):
    if request.method=="POST":
        data=request.POST
        username=data.get('username')
        password=data.get('password')
        if not User.objects.filter(username=username).exists():
            messages.error(request,'User name is not exist')
            return redirect('/')
        user=authenticate(username=username,password=password)
        if user is None:
            messages.error(request,'Invalid Credentials')
            return redirect('/')
        else:
            login(request,user)
            return redirect('/registration')
    return render(request,'login.html')

@login_required(login_url='/')
def registration1(request):
    user = request.user
    user_id = request.user.id 
    if semester_info.objects.filter(uni_id=user_id):
        messages.info(request,'Details already saved')
        return redirect('/course-register')
    else:
        if request.method=="POST":
            data=request.POST
            year=data.get('year')
            semester=data.get('semester')
            branch=data.get('branch')
            roll=data.get('roll')
            semester_info.objects.create(
                year=year,
                uni_id=user_id,
                branch=branch,
                semester=semester,
                roll=roll,
            )
            messages.info(request,'Details has been saved')
            return redirect('/registration')
    context={
        'user':user,
    }
    return render(request,'registration.html',context)

def register(request):
    if request.method=="POST":
        data=request.POST
        username=data.get('username')
        password=data.get('password')
        password1=data.get('repassword')
        first_name=data.get('first_name')
        last_name=data.get('last_name')
        email=data.get('email')
        if username=="":
            messages.info(request,'User name should not be blank')
            return redirect('/register')
        if first_name=="":
            messages.info(request,'First Name should not be blank')
            return redirect('/register')
        if last_name=="":
            messages.info(request,'Last Name should not be blank')
            return redirect('/register')
        if email=="":
            messages.info(request,'Email should not be blank')
            return redirect('/register')
        if password=="":
            messages.info(request,'Password should not be blank')
            return redirect('/register')
        if password1=="":
            messages.info(request,'Re-enter password should not be blank')
            return redirect('/register')
        user=User.objects.filter(username=username)
        if user.exists():
            messages.info(request,'User name is already Exists')
            return redirect('/register')
        if password!=password1:
            messages.info(request,'Password is not same')
            return redirect('/register')
        user=User.objects.create(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
        )
        user.set_password(password)
        user.save()
        messages.info(request,'Account Created successfully')
        return redirect('/register')
    return render(request,'register.html')

@login_required(login_url='/')
def course_register(request):
    user=request.user
    user_id = request.user.id 
    query=semester_info.objects.filter(uni_id=user_id)
    for i in query:
        r=i.roll
        sem=i.semester
        year=i.year
        q1=Database.objects.filter(Q(branch=i.branch) & Q(sem=i.semester) & Q(Group='A'))
        q2=Database.objects.filter(Q(branch=i.branch) & Q(sem=i.semester) & Q(Group='B'))
        q3=Database.objects.filter(Q(branch=i.branch) & Q(sem=i.semester) & Q(Group='C'))
        q4=Database.objects.filter(Q(branch=i.branch) & Q(sem=i.semester) & Q(Group='D'))
        q5=Database.objects.filter(Q(branch=i.branch) & Q(sem=i.semester) & Q(Group='E'))
        q6=Database.objects.filter(Q(branch=i.branch) & Q(sem=i.semester) & Q(Group='F'))
        q7=Database.objects.filter(Q(branch=i.branch) & Q(sem=i.semester) & Q(Group='G'))
        q8=Database.objects.filter(Q(branch=i.branch) & Q(sem=i.semester) & Q(Group='H'))
    context={
        'user':user,
        'q1':q1,
        'q2':q2,
        'q3':q3,
        'q4':q4,
        'q5':q5,
        'q6':q6,
        'q7':q7,
        'q8':q8,
        'r':r,
        'sem':sem,
        'year':year,
        
    }
    
    return render(request,'course_register.html',context)

def review(request):
    user=request.user
    user_id=request.user.id
    query=semester_info.objects.get(uni_id=user_id)
    
    data=semester_info.objects.all()
    user = request.user
    slotA = request.GET.get('slotA')
    slotB = request.GET.get('slotB')
    slotC = request.GET.get('slotC')
    slotD = request.GET.get('slotD')
    slotE = request.GET.get('slotE')
    slotF = request.GET.get('slotF')
    slotG = request.GET.get('slotG')
    slotH = request.GET.get('slotH')
    photo=request.GET.get('photo1')
    context = {
        'user': user,
        'slotA': slotA,
        'slotB':slotB,
        'slotC':slotC,
        'slotD':slotD,
        'slotE':slotE,
        'slotF':slotF,
        'slotG':slotG,
        'slotH':slotH,
        'photo':photo,
        'data':data,
        'query':query,
        # 'r':r,
        # 'sem':sem,
        # 'year':year

    }
    return render(request, 'view.html', context)