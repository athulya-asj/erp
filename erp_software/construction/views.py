from django.shortcuts import render,redirect
from django.http import HttpResponse

from construction.models import admin,contractor_registration,employee,work,select_employee
from django.contrib.auth import logout

# Create your views here.
def index(request):
    return render(request,'index.html')
def login(request):
    return render(request,'login.html')
def loginsubmit(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        username=str(username)
        password=str(password)
        u=admin.objects.filter(username=username)
        v=admin.objects.filter(password=password)
        if u.count()==1 and v.count()==1:
            return render(request,'adminhome.html')
        else:
            u=contractor_registration.objects.filter(email=username)
            v=contractor_registration.objects.filter(password=password)
            if u.count()==1 and v.count()==1:
                request.session['usr']=username
                return render(request,'contractorhome.html')
            else:
                u=admin.objects.filter(username=username)
                v=admin.objects.filter(password=password)
                if u.count()==1 and v.count()==1:
                    return render(request,'adminhome.html')
                else:
                    u=employee.objects.filter(email=username)
                    v=employee.objects.filter(password=password)
                    if u.count()==1 and v.count()==1:
                        request.session['usr1']=username
                        return render(request,'employeehome.html')
                    else:
                        return render(request,'login.html', {'messege':"wrong Username or Password"})
def adminaddcontractor(request):
    return render(request,'adminaddcontractor.html')
def admin_submit_contractor(request):
    if request.method=='POST': 
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        password=request.POST.get('password')
        
        a=contractor_registration(name=name,email=email,phone=phone, password= password)
        a.save()
        return render(request,'adminaddcontractor.html')
def adminaddemployee(request):
    return render(request,'adminaddemployee.html')
def admin_submit_employee(request):
    if request.method=='POST': 
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        nid=request.POST.get('nid')
        salary=request.POST.get('salary')
        grade=request.POST.get('grade')
        password=request.POST.get('password')
        a=employee(name=name,email=email,phone=phone,nid=nid,salary=salary,grade=grade,password= password)
        a.save()
        return render(request,'adminaddemployee.html')
def adminaddcontract(request):
    query = contractor_registration.objects.all().filter(status='available')
    return render(request,'adminaddcontract.html',{'authors':query})
def admin_submit_work(request):
    if request.method=='POST': 
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        type=request.POST.get('type')
        fromdate=request.POST.get('fromdate')
        todate=request.POST.get('todate')
        budget=request.POST.get('budget')
        enumber=request.POST.get('enumber')
        contractor=request.POST.get('contractor')
        a=work(name=name,phone=phone,type=type,fromdate=fromdate,todate=todate,budget=budget,enumber=enumber,contractor=contractor)
        a.save()
        return render(request,'adminaddcontract.html')
def adminremovecontractor(request):
    query = contractor_registration.objects.all()
    return render(request,'adminremovecontractor.html',{'authors':query})
def deletecontractor(request):
    id=request.POST.get('id')
    b = contractor_registration.objects.get(id = id)
    b.delete()
    query = contractor_registration.objects.all()
    return render(request,'adminremovecontractor.html',{'authors':query})
def adminremoveemployee(request):
    query = employee.objects.all()
    return render(request,'adminremoveemployee.html',{'authors':query})
def deleteemployee(request):
    id=request.POST.get('id')
    b = employee.objects.get(id = id)
    b.delete()
    query = contractor_registration.objects.all()
    return render(request,'adminremoveemployee.html',{'authors':query})
def adminviewemployee(request):
    query = employee.objects.all()
    return render(request,'adminviewemployee.html',{'authors':query})
def adminviewcontractor(request):
    query = contractor_registration.objects.all()
    return render(request,'adminviewcontractor.html',{'authors':query})
def logout(request):
    return redirect('login')
def contractor_view_work(request):
    a = contractor_registration.objects.get(email=request.session['usr'])
    b = a.id
    c=  work.objects.filter(id=b)
    return render(request,'contractorviewwork.html',{'authors':c})
def contractor_update_status(request):
    a = contractor_registration.objects.get(email=request.session['usr'])
    b = a.id
    c=  work.objects.filter(id=b)
    return render(request,'contractor_update_work.html',{'authors':c})
def updatestatus(request):
    wid=request.POST.get('id')
    status=request.POST.get('status')
    a = contractor_registration.objects.get(email=request.session['usr'])
    b = a.id
    c =  work.objects.filter(id=b)
    if status=='completed':
        contractor_registration.objects.filter(id=wid).update(status='available')
        work.objects.filter(id=wid).update(status=status)
    if status=='approved':
        contractor_registration.objects.filter(id=wid).update(status='on work')
        work.objects.filter(id=wid).update(status='pending')
    if status=='pending':
        contractor_registration.objects.filter(id=wid).update(status='available')
        work.objects.filter(id=wid).update(status='pending')
    return render(request,'contractor_update_work.html',{'authors':c})
def contractor_select_employee(request):
    query1 = work.objects.all()
    query2 = employee.objects.all()
    return render(request,'contractor_select_employee.html',{'authors1':query1,'authors2':query2})
def contractor_submit_employee(request):
    if request.method=='POST': 
        wid=request.POST.get('wid')
        eid=request.POST.get('eid')
       
        a=select_employee(wid=wid,eid=eid)
        a.save()
        return render(request,'contractor_select_employee.html')
def employee_view_work(request):
    a = employee.objects.get(email=request.session['usr1'])
    b = a.id
    c = select_employee.objects.filter(eid=b)
    if c.count()>0:
        d = select_employee.objects.get(eid=b)
        e = d.wid
        f = work.objects.filter(id=e)
        return render(request,'employee_view_work.html',{'authors':c})
    else:
        return HttpResponse('unsuccessfull')