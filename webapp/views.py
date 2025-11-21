from django.shortcuts import render,redirect
from perfumeapp.models import FragranceDB, PerfumesDB
from webapp.models import RegisterDB,ContactDB


# Create your views here.
def home_page(request):
    fragrances =FragranceDB.objects.all()
    perfumes = PerfumesDB.objects.all()
    return render(request, "Home_Page.html",
        {'fragrances':fragrances,'perfumes':perfumes})
def about_page(request):
    fragrances =FragranceDB.objects.all()
    return render(request, "About.html", {'fragrances':fragrances})
def contact_page(request):
    fragrances =FragranceDB.objects.all()
    return render(request, "Contact_Page.html", {'fragrances':fragrances})
def all_perfumes_page(request):
    fragrances =FragranceDB.objects.all()
    perfumes= PerfumesDB.objects.all()
    return render(request, "All_Perfumes.html", {'perfumes':perfumes,'fragrances':fragrances})
def filtered_perfume_page(request,perfume_category):
    fume = PerfumesDB.objects.filter(Fragrance_Category=perfume_category)
    return render(request, "Filtered_Perfumes.html", {'fume':fume})
def single_perfume(request, pfume_id):
    pfume= PerfumesDB.objects.get(id=pfume_id)
    return render(request, "Single_Perfume.html", {'pfume':pfume})
def sign_up(request):
    return render(request, "Sign_Up.html")
def save_user(request):
    if request.method== "POST":
        USER_NAME =request.POST.get('username')
        PASSWORD =request.POST.get('password')
        CONFIRM_PASSWORD =request.POST.get('confirm_password')
        EMAIL =request.POST.get('email')
        obj =RegisterDB(User_Name=USER_NAME, Password=PASSWORD, Conform_Password=CONFIRM_PASSWORD, Email=EMAIL)
        if RegisterDB.objects.filter(User_Name=USER_NAME).exists():
             # Alert-Username already exist..!
            return redirect(sign_up)
        elif RegisterDB.objects.filter(Email=EMAIL).exists():
            # Alert-Email already exist..!
            return redirect(sign_up)
        else:
            obj.save()
        return redirect(sign_up)
def sign_in(request):
    return render(request, "Sign_In.html")
def user_sign_in(request):
    if request.method =="POST":
        un = request.POST.get('username')
        pas = request.POST.get('password')
        if RegisterDB.objects.filter(User_Name=un, Password=pas).exists():
            request.session['User_Name'] = un
            request.session['Password'] = pas
            return redirect(home_page)
        else:
            return redirect(sign_in)
    else:
        return redirect(sign_in)
def user_logout(request):
    del request.session['User_Name']
    del request.session['Password']
    return redirect(home_page)

def contact_us_save(request):
    if request.method =="POST":
        NAME =request.POST.get('u_name')
        EMAIL =request.POST.get('u_email')
        SUBJECT =request.POST.get('u_subject')
        MESSAGE =request.POST.get('u_message')
        obj= ContactDB(Name=NAME,Email=EMAIL, Subject=SUBJECT, Message=MESSAGE)
        obj.save()
        return redirect(contact_page)

def cart_page(request):
    fragrances = FragranceDB.objects.all()
    return render(request,"Cart.html", {'fragrances':fragrances})
def checkout_page(request):
    fragrances = FragranceDB.objects.all()
    return render(request,"Checkout.html", {'fragrances':fragrances})
