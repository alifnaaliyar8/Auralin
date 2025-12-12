from platform import uname

from django.shortcuts import render,redirect
from perfumeapp.models import FragranceDB, PerfumesDB
from webapp.models import RegisterDB,ContactDB,CartDB,OrderDB
from django.contrib import messages
import razorpay
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

def checkout_page(request):
    fragrances = FragranceDB.objects.all()
    perfumes= CartDB.objects.filter(User_Name=request.session['User_Name'])
    cart_total = 0
    uname = request.session.get('User_Name')
    if uname:
        cart_total = CartDB.objects.filter(User_Name=uname).count()
    # Calculating total amount
    sub_total = 0
    delivery_charge = 0
    total_amount = 0
    for i in perfumes:
        sub_total += i.Total_Price
        if sub_total > 500:
            delivery_charge = 50
        else:
            delivery_charge = 100
        total_amount = sub_total + delivery_charge

    return render(request,"Checkout.html", {'fragrances':fragrances,
                                            'cart_total': cart_total, 'sub_total': sub_total,
                                            'delivery_charge': delivery_charge, 'total_amount': total_amount
                                            })

def cart_page(request):
    perfumes= CartDB.objects.filter(User_Name=request.session['User_Name'])
    fragrances = FragranceDB.objects.all()
    cart_total=0
    uname= request.session.get('User_Name')
    if uname:
        cart_total=CartDB.objects.filter(User_Name=uname).count()
    #Calculating total amount
    sub_total=0
    delivery_charge=0
    total_amount=0
    for i in perfumes:
        sub_total +=i.Total_Price
        if sub_total>500:
            delivery_charge=50
        else:
            delivery_charge=100
        total_amount= sub_total+delivery_charge
    return render(request,"Cart.html", {'fragrances':fragrances,'perfumes':perfumes,'cart_total':cart_total,'sub_total':sub_total,
                                        'delivery_charge':delivery_charge,'total_amount':total_amount})

def save_to_cart(request):
    if request.method == "POST":
        USER_NAME = request.POST.get('username')
        PERFUME_NAME = request.POST.get('perfume_name')
        QUANTITY = int(request.POST.get('quantity'))
        PRICE = int(request.POST.get('price'))
        TOTAL_PRICE = int(request.POST.get('total'))
        perfumes = PerfumesDB.objects.filter(Perfume_Name=PERFUME_NAME).first()
        IMG=perfumes.Perfume_Image if perfumes else None
        obj = CartDB(User_Name=USER_NAME, Perfume_Name=PERFUME_NAME,
                     Quantity=QUANTITY, Price=PRICE,  Total_Price=TOTAL_PRICE,
                     Perfume_Image=IMG)
        obj.save()
        return redirect(home_page)

def remove_cart_item(request, del_id):
    data= CartDB.objects.filter(id=del_id)
    data.delete()
    return redirect(cart_page)

def check_out_save(request):
    if request.method=="POST":
        FIRST_NAME=request.POST.get('First_Name')
        LAST_NAME=request.POST.get('Last_Name')
        ADDRESS=request.POST.get('Address')
        PLACE=request.POST.get('Place')
        POSTCODE=request.POST.get('Post_Code')
        PHONE= request.POST.get('Phone')
        EMAIL=request.POST.get('Email')
        TOTAL_PRICE = request.POST.get('Total')
        obj = OrderDB(First_Name=FIRST_NAME, Last_Name=LAST_NAME,
                  Address=ADDRESS, Place=PLACE,Post_Code=POSTCODE,
                  Phone=PHONE,Email=EMAIL,Total_Price=TOTAL_PRICE)
        obj.save()
        return redirect(checkout_page)
    perfumes= CartDB.objects.filter(User_Name=request.session['User_Name'])
    sub_total=0
    delivery_charge=0
    total_amount=0
    for i in perfumes:
        sub_total += i.Total_Price
        if sub_total > 500:
            delivery_charge=50
        else:
            delivery_charge= 100
            total_amount= sub_total + delivery_charge
    return render(request, "Payment_Page.html", {'perfumes':perfumes,'sub_total': sub_total,
                                             'delivery_charge': delivery_charge, 'total_amount': total_amount})

def payment_page(request):
    fragrances = FragranceDB.objects.all()
    cart_total = 0
    uname = request.session.get('User_Name')
    payy = 0
    payy_str = "0"
    if uname:
        cart_total = CartDB.objects.filter(User_Name=uname).count()
        #Adding details for payment
        # Retrieve the data from OrderDB with the specified ID

        # Fetch the last order safely
        customer= OrderDB.objects.order_by('-id').first()
        #Get the amount of the specified customer
        if customer:
            payy = customer.Total_Price
            amount= int(payy*100)
            payy_str= str(amount)
        else:
            # No order exists → redirect or show message
            return render(request, "Payment.html", {
            "fragrances": fragrances,
            "cart_total": cart_total,
            "error": "No order found. Please place an order before proceeding to payment."
        })

        if request.method == "POST":
            order_currency= 'INR'
            client = razorpay.Client(auth=('rzp_test_0ib0jPwwZ7I1lT', 'VjHNO5zKeKxz8PYe7VnzwxMR'))
            payment= client.order.create({'amount':amount, 'currency':order_currency})
    return render(request, "Payment.html", {'fragrances':fragrances,
                                                 'cart_total':cart_total, 'payy':payy, 'payy_str':payy_str })
