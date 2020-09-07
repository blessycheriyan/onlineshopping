import datetime
from django.shortcuts import render
from c1.models import advisor
from c1.forms import advisorform
from c1.models import users4
from c1.forms import userform
from c1.models import dress
from c1.forms import dressform
from c1.models import book10
from c1.forms import bookform
from c1.models import feedback1

from c1.forms import feedbackform
from django.http import HttpResponse

def home(request):
    return render(request,'homepg.html')
#Admin Registration &ViewDetails#
def admin0(request):
    userlist=advisor.objects.all()
    return render(request,'viewadmin.html',{'user':userlist})

def admin1(request):
    form=advisorform()
    if request.method=="POST":
        form=advisorform(request.POST)
        if form.is_valid():
            form.save()
            return home(request)
        else:
            HttpResponse("invalid data")
    return render(request,"registrationadmin.html",{'form':form})

#User Registration &ViewDetails#
def user0(request):
    userlist=users4.objects.all()
    return render(request,'viewuserdesign.html',{'user':userlist})



#boostrap using user registration #
def user1(request):
    a=request.session['users_name']
    userlist = users4.objects.filter(name=a)

    if request.method == "POST":

        name1 = request.POST["name"]
        email1 = request.POST["email"]
        password1 = request.POST["password"]
        address1 = request.POST["address"]
        contactno1 = request.POST["contactno"]
        city1 = request.POST["city"]
        c = request.POST['date']
        g = request.POST['gender']
        t = request.POST['country']
        users4.objects.filter(name=a).update(name=name1, email=email1, password=password1, address=address1, contactno=contactno1,
                           city=city1, date=c, gender=g, country=t)
        return render(request, 'userhome.html')
    else:
        return render(request, 'profileuser.html',{'user':userlist})


def register(request):
  try:

    if request.method == "POST":
        name1 = request.POST["name"]
        email1 = request.POST["email"]
        password1 = request.POST["password"]
        address1 = request.POST["address"]
        contactno1 = request.POST["contactno"]
        city1 = request.POST["city"]
        c = request.POST['date']
        g = request.POST['gender']
        t = request.POST['country']
        p = request.FILES["picture"]
        register1 = users4( name=name1, email=email1, password=password1, address=address1, contactno=contactno1,city=city1,date=c,gender=g,country=t,data=p)
        register1.save()
        return render(request, 'homepg.html')
    else:
        return render(request, 'register.html')
  except:
        return render(request, 'register.html',{'error':"Please Fill The Form"})
#Dress registration and viewform#

def viewadminproduct(request):
    userlist=dress.objects.all()
    return render(request,'viewadminproduct.html',{'user':userlist})
def product7(request):
    userlist = dress.objects.all()
    return render(request,'logout.html',{'user':userlist})

def productregister(request):
 try:

    if request.method == "POST":
        name1 = request.POST["name"]
        price1 = request.POST["price"]
        image1 = request.FILES["images"]
        if  name1 and price1 and image1:
            register1 = dress(name=name1,  price=price1,  data=image1)
            register1.save()
            return render(request, 'adminlogout.html')

    else:
        return render(request, 'registrationproduct.html')
 except:
     return render(request, 'registrationproduct.html',{'error': "Please Fill The Form"})

 return render(request, 'registrationproduct.html', {'error': "Please Fill The Form"})
def search1(request):
    userlist = dress.objects.filter(name=request.POST['name'])
    return render(request, 'viewproductdesign.html', {'user': userlist})
def adminsearch1(request):
    userlist = dress.objects.filter(name=request.POST['name'])
    return render(request, 'viewadminproduct.html', {'user': userlist})
def user4(request):
    userlist = book10.objects.all()
    return render(request, 'viewadminbookingdetails.html', {'user': userlist})
#User Login & Logout#

def userdel(request):
    book10.objects.filter(id=request.POST['btn']).update(status=1)
    userlist = book10.objects.all()
    return render(request, 'viewadminbookingdetails.html', {'user': userlist})

def login(request):
    try:
         if request.method=="POST":
            m=users4.objects.get(name=request.POST['username'])

            if m.password==int(request.POST['passw']):
                request.session['users_name']=m.name
                request.session['usersid'] = m.userid
                userlist = dress.objects.all()

                return render(request,'userhome.html',{'user':userlist,'name':m.name})
            else:
                return render(request, 'login.html',{'error':"please check the password"})
         else:
            return render(request,'login.html')
    except:
        return render(request, 'login.html',{'error':"Please Check the Username and Password"})
def logout(request):
    try:
        del request.session['users_name']
    except KeyError:
        pass
    return  render(request,'homepg.html')


#add booking & viewdetails#
def book1(request):
    userlist = book10.objects.all()
    return render(request, 'viewbookdesign.html', {'user': userlist})
def adminbook1(request):
    userlist = book10.objects.all()
    return render(request, 'viewadminbookingdetails.html', {'user': userlist})
#pass the value#
def add(request):
        id=request.POST['na']
        userlist = dress.objects.filter(name=id)
        date = datetime.date.today()
        return render(request, 'bookingdesign.html',{'user': userlist,'date':date})
def book9(request):
   try:
        if request.method == "POST":
            c = request.POST['date']
            d = request.POST['quantity']
            e = request.POST['totalprice']
            f = request.session['usersid']

            register = book10(date=c, quantity=d, totalprice=e, usr=f)
            register.save()

        return render(request, 'userhome.html')
   except:

       id = request.POST['na']
       userlist = dress.objects.filter(name=id)
       date = datetime.date.today()

       return render(request, 'bookingdesign.html', {'user': userlist,'name':id,'error':"Please Fill The Form",'date':date})

#feedback using session to pass name#
def feedback(request):
    if request.session:
        f = request.session['users_name']
        return render(request, 'fed.html', {'name': f})
def feed(request):
 try:
        if request.method=="POST":
            c = request.POST['rate']
            d = request.POST['comment']
            f = request.session['users_name']
            if c and d and f:
                register = feedback1(rate=c, comment=d, name=f)
                register.save()

                return render(request, 'fed.html', {'name': f, 'error': "Please Fill The Form"})

            else:
                return render(request, 'fed.html', {'name': f, 'error': "Please Fill The Form"})


        return render(request, 'fed.html', {'name': f,'error': "Please Fill The Form"})

 except:
        f = request.session['users_name']


        return render(request, 'fed.html', {'name': f,'error': "Please Fill The Form"})


#Adnin Login &Logout#
def adminlogin(request):
    try:
         if request.method=="POST":
            m=advisor.objects.get(name=request.POST['username'])
            print(m.password)
            if m.password==int(request.POST['passw']):
                request.session['advisor_name']=m.name
                userlist = dress.objects.all()
                return render(request,'adminlogout.html',{'user':userlist,'name':m.name})
            else:
                return render(request, 'adminlogin.html',{'error':"Please Check the Username and Password"})
         else:
            return render(request,'adminlogin.html')
    except:
        return render(request, 'adminlogin.html',{'error':"Please Check the Username and Password"})
def user2(request):
    userlist = book10.objects.filter(usr= request.session['usersid'])
    return render(request, 'viewbookdesign.html', {'user': userlist})
def viewuserdetails(request):
    userlist = users4.objects.filter(userid= request.session['usersid'])
    return render(request, 'profileuser.html', {'user': userlist})
def deleteproduct(request):
        id = int(request.POST['dressid'])
        print(id)
        dress.objects.get(dressid=id).delete()
        userlist=dress.objects.all()
        print("deleteeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
        return render(request, 'viewadminproduct.html', {'user': userlist})
def adminlogout1(request):
    return render(request, 'adminlogout.html')
def homepg1(request):
    return render(request, 'homepg.html')
def about1(request):
    return render(request, 'about.html')
def homepg2(request):
    return render(request, 'userhome.html')

def viewadminfeedback(request):
    userlist = feedback1.objects.all()
    return render(request, 'viewadminfeedback.html', {'user': userlist})
