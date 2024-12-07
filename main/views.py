from django.urls import reverse
import requests
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.conf import settings 

from .models import (Contact, Comment, Company, Product, Taklif, Buyurtma, Mainpart)



TELEGRAM_BOT_TOKEN = settings.BOT

def send_to_telegram(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {'chat_id': settings.USER_ID, 'text': text}
    response = requests.post(url, json=payload)
    return response.status_code


class HomeView(View):
    def get(self, request):

        contact = Contact.objects.last()
        comments = Comment.objects.all()
        company = Company.objects.last()
        products = Product.objects.all()
        bel = Product.objects.filter(tur='bel')
        boyin = Product.objects.filter(tur='boyin')
        soyabon = Product.objects.filter(tur='soyabon')
        mainpart = Mainpart.objects.all()
        
        context = {
            'contact': contact,
            'comments':comments,
            'company':company,
            'products':products,
            'bel': bel,
            'boyin': boyin,
            'soyabon': soyabon,
            'mainpart': mainpart,
            
        }
        return render(request, 'index.html', context)
    def post(self, request):
        name = request.POST.get('name')
        telefon = request.POST.get('telefon')
        message = request.POST.get('xabar')
        manzil = request.POST.get('manzil')
        
        if not telefon:
            messages.error(request, "Telefon raqamni kiriting!")
            return redirect(f"{reverse('main:home')}#contact")
        

        new = Taklif.objects.create(
            full_name=name,
            phone_number=telefon,
            batafsil=message,
            address = manzil  
        )

        ans = send_to_telegram(
            f'Xabar: 🎫 \n\n\nKlient:\t {name}\nTelefon raqam:\t {telefon}\nXabar:\t {message}'
        )
        if ans == 200:
            messages.success(request, "Xabar muvaffaqiyatli jo‘natildi!")
        else:
            messages.error(request, "Xabarni jo‘natishda xatolik yuz berdi.")
        return redirect("main:home")
    

class DetailView(View):
    def get(self, request, x):
        products = Product.objects.filter(tur=x)
        contact = Contact.objects.last()
        company = Company.objects.last()
        p = Product.objects.filter(tur=x).last()
        context = {
            'products': products,
            'one': p,
            'contact': contact,
            'company': company
        }
        return render(request, 'detail.html', context)
    def post(self, request, x):
        name = request.POST.get('name')
        telefon = request.POST.get('telefon')
        message = request.POST.get('xabar')
        if not name:
            name = 'Nomalum'
        if not telefon:
            messages.error(request, "Telefon raqamingizni to'g'ri kiriting!")
            return redirect(f"{reverse('main:detail', args=[x])}#specials")
        if not message:
            message = 'Malumotlar kiritilmagan!'
        new = Buyurtma.objects.create(
            full_name=name,
            phone_number=telefon,
            batafsil=message,
            product=Product.objects.filter(tur=x).last()
            )
        ans = send_to_telegram(
            f'Buyurtma: \n\n\nKlient:\t {name}\nTelefon raqam:\t {telefon}\nXabar:\t {message}'
        )
        messages.success(request, "Buyurtmangiz yuborildi, Buyurtmangiz uchun rahmat!")
        return redirect('main:home')
    