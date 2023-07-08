from django.shortcuts import render, HttpResponse , redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User
from .models import Movie , Series
from django.core.files.storage import FileSystemStorage
from django.db.models import F
# import movie_site.address
from django.template.defaulttags import register

@register.filter
def get_range(value):
    return range(value)


# Create your views here.
def home(request):
    if request.user.is_anonymous:
        return redirect('/login')
    
    ser_names = set()
    for i in Series.objects.all():
        ser_names.add(i.ser_name)
    ser_imgs = []
    for i in ser_names:
        u = Series.objects.filter(ser_name = i)[0]
        ser_imgs.append(u.ser_img)
    name= list(ser_names)
    ser = []
    for i in range(len(ser_imgs)):
        ser.append([name[i],ser_imgs[i]])
    context = {
        'movies':Movie.objects.all(),
        'series':ser,
    }
    return render(request,'home.html',context)

def movies(request):
    context = {
        'movies':Movie.objects.all(),
    }
    return render(request,'movies.html',context)

def series(request):
    ser_names = set()
    for i in Series.objects.all():
        ser_names.add(i.ser_name)
    ser_imgs = []
    for i in ser_names:
        u = Series.objects.filter(ser_name = i)[0]
        ser_imgs.append(u.ser_img)
    name= list(ser_names)
    ser = []
    for i in range(len(ser_imgs)):
        ser.append([name[i],ser_imgs[i]])
    
    return render(request,'series.html',{'data':ser })

def categories_specific(request,cat):
    a = Movie.objects.all()
    d = []
    data = []
    for i in a:
        if cat in i.mov_cat:
            d.append(i.id)
    for i in d:
        data.append(Movie.objects.get(id=i))
    return render(request, 'cat.html' , {'data':data , 'cat':cat })

def categories(request):
    return render(request,'category.html')



def create_account(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(username=username, password=password)
        try:
            user.save()
            return redirect('/')
        except:
            pass
    return render(request,'create.html')



def logout(request):
    auth_logout(request)
    return redirect('/')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request , username=username , password=password)
        if user is not None:
            auth_login(request,user)
            return redirect('/')
    return render(request,'login.html')

def upload(request):
    if request.method == "POST":
        try :
            new = Movie(mov_name=request.POST['moviename'] , mov_desc=request.POST['moviedesc'] , mov_cat=request.POST['cat'] , mov_trailer=request.POST['trailer'] , mov_img=request.FILES.get('mimage') , mov_poster=request.FILES.get('poster') , mov_vid=request.FILES.get('video'))
            new.save()
            return redirect("/")
        except:
            print("Error")
    return render(request,'upload.html')

def upload_se(request):
    if request.method == "POST":
        try :
            for i in request.FILES.getlist('video'):
                new = Series(ser_name=request.POST['moviename'] , ser_desc=request.POST['moviedesc'] , ser_cat=request.POST['cat'] , ser_trailer=request.POST['trailer'] , ser_img=request.FILES.get('mimage') , ser_poster=request.FILES.get('poster') , ser_vid= i)
                new.save()
            return redirect("/")
        except:
            print("Error")
    return render(request,'upload_ser.html')


def play(request,url):
    l = Movie.objects.get(id=url)
    return render(request,'player.html',{
        'v':l
    })

def play_ser(request,name):
    i = Series.objects.filter(ser_name=name)
    vids = []
    for j in i:
        vids.append(j.ser_vid)
    videos = []
    for k in range(len(vids)):
        videos.append([k,vids[k]])
    print(len(vids))
    return render(request,'player_series.html',{'data':i[0] , 'video':videos})
