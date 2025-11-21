from django.shortcuts import render,redirect
from perfumeapp.models import FragranceDB,PerfumesDB
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from webapp.models import ContactDB

# Create your views here.
def index_page(request):
    frag =FragranceDB.objects.count()
    pfum = PerfumesDB.objects.count()
    msgs = ContactDB.objects.count()
    return render(request, "Index.html",{'frag':frag,'pfum':pfum,'msgs':msgs})
def add_category(request):
    return render(request, "Add_Fragrance_Note_Categories.html")
def save_add_category(request):
    if request.method =="POST":
        FRAGRANCE_NAME = request.POST.get('f_name')
        DESCRIPTION = request.POST.get('f_description')
        KEY_NOTES =  request.POST.get('f_keynotes')
        CHARACTERISTICS =  request.POST.get('f_characteristics')
        FRAGRANCE_IMAGE = request.FILES['f_image']
        obj = FragranceDB(Fragrance_Name=FRAGRANCE_NAME, Description=DESCRIPTION, Key_Notes=KEY_NOTES, Characteristics=CHARACTERISTICS, Fragrance_Image=FRAGRANCE_IMAGE)
        obj.save()
        return redirect(add_category)
def display_add_category(request):
    data = FragranceDB.objects.all()
    return render (request, "Display_Add_Fragrances.html",{'data':data})
def edit_add_category(request,fcategory_id):
    note = FragranceDB.objects.get(id=fcategory_id)
    return render(request,"Edit_Add_Fragrances.html", {'note':note})
def update_add_category(request,F_id):
    if request.method == "POST":
        FRAGRANCE_NAME = request.POST.get('f_name')
        DESCRIPTION = request.POST.get('f_description')
        KEY_NOTES = request.POST.get('f_keynotes')
        CHARACTERISTICS = request.POST.get('f_characteristics')
        try:
            FRAGRANCE_IMAGE = request.FILES['f_image']
            fs= FileSystemStorage()
            file= fs.save(FRAGRANCE_IMAGE.name,FRAGRANCE_IMAGE)
        except MultiValueDictKeyError:
            file= FragranceDB.objects.get(id=F_id).Fragrance_Image
        FragranceDB.objects.filter(id=F_id).update(Fragrance_Name=FRAGRANCE_NAME, Description=DESCRIPTION, Key_Notes=KEY_NOTES, Characteristics=CHARACTERISTICS, Fragrance_Image=file)
        return redirect(display_add_category)
def delete_add_category(request,fragrance_id):
    data = FragranceDB.objects.filter(id=fragrance_id)
    data.delete()
    return redirect(display_add_category)
def add_perfumes(request):
    fragrance = FragranceDB.objects.all()
    return render(request, "Add_Perfumes.html",{'fragrance':fragrance})
def save_add_perfumes(request):
    if request.method =="POST":
        PERFUME_NAME = request.POST.get('p_name')
        BRAND_NAME = request.POST.get('p_brand')
        FRAGRANCE_CATEGORY = request.POST.get('f_category')
        DESCRIPTION = request.POST.get('p_description')
        PRICE =  request.POST.get('p_price')
        EXPIRY_DATE =  request.POST.get('e_date')
        SIZE =  request.POST.get('p_size')
        PERFUME_IMAGE =  request.FILES['p_image']
        obj1 = PerfumesDB(Perfume_Name=PERFUME_NAME, Brand_Name=BRAND_NAME, Fragrance_Category=FRAGRANCE_CATEGORY, Description=DESCRIPTION,
                           Price=PRICE, Expiry_Date=EXPIRY_DATE, Size=SIZE, Perfume_Image=PERFUME_IMAGE)
        obj1.save()
        return redirect(add_perfumes)
def display_add_perfumes(request):
    data = PerfumesDB.objects.all()
    return render(request, "Display_Add_Perfumes.html", {'data':data})
def edit_add_perfumes(request,perfume_id):
    perfume =PerfumesDB.objects.get(id=perfume_id)
    categories =FragranceDB.objects.all()
    return render(request, "Edit_Add_Perfumes.html", {'perfume':perfume,'categories':categories})
def update_add_perfumes(request,P_id):
    if request.method == "POST":
        PERFUME_NAME = request.POST.get('p_name')
        BRAND_NAME = request.POST.get('p_brand')
        FRAGRANCE_CATEGORY = request.POST.get('f_category')
        DESCRIPTION = request.POST.get('p_description')
        PRICE = request.POST.get('p_price')
        EXPIRY_DATE = request.POST.get('e_date')
        SIZE = request.POST.get('p_size')
        try:
            PERFUME_IMAGE= request.FILES['p_image']
            FS = FileSystemStorage()
            file = FS.save(PERFUME_IMAGE.name,PERFUME_IMAGE)
        except MultiValueDictKeyError:
            file =PerfumesDB.objects.get(id=P_id).Perfume_Image
        PerfumesDB.objects.filter(id=P_id).update(Perfume_Name=PERFUME_NAME, Brand_Name=BRAND_NAME, Fragrance_Category=FRAGRANCE_CATEGORY, Description=DESCRIPTION,
                     Price=PRICE, Expiry_Date=EXPIRY_DATE, Size=SIZE, Perfume_Image=file)
        return redirect(display_add_perfumes)
def delete_add_perfumes(request,pfume_id):
    data = PerfumesDB.objects.filter(id=pfume_id)
    data.delete()
    return redirect(display_add_perfumes)

def admin_login(request):
    return render(request, "Admin_Login_Page.html")
def admin_login_check(request):
    if request.method =="POST":
        UN = request.POST.get('username')
        PW = request.POST.get('password')
        if User.objects.filter(username__contains=UN).exists():
            data =authenticate(username=UN, password=PW)
            if data is not None:
                login(request, data)
                request.session['username']=UN
                request.session['password']=PW
                return redirect(index_page)
            else:
                return redirect(admin_login)
        else:
            return redirect(admin_login)
def admin_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(index_page)

def view_messages(request):
    data = ContactDB.objects.all()

    return render(request, "View_Messages.html",{'data':data})

def delete_message_data(request,msg_id):
    data = ContactDB.objects.filter(id=msg_id)
    data.delete()
    return redirect(view_messages)
