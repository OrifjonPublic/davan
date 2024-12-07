from django.db import models


class Contact(models.Model):
    phone_number1 = models.CharField(max_length=25, default='+998 90 900 5776')
    phone_number2 = models.CharField(max_length=25, default='+998 99 519 3422')
    email = models.CharField(default='info@davan.uz', max_length=50)
    address_1 = models.CharField(max_length=300, default='Наманган вилояти Чортоқ тумани \n Оқтикан кичик саноат зонаси')
    address_2 = models.CharField(max_length=250, null=True, blank=True)
    telegram_url = models.URLField(null=True, blank=True)
    instagram_url = models.URLField(null=True, blank=True)
    facebook_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.phone_number1 + ': ' + self.address_1


class Mainpart(models.Model):
    name = models.CharField(max_length=120, default='Nomalum', verbose_name='Nomi')
    image = models.ImageField(upload_to='mainparts/', default='none.png', verbose_name='Rasm')
    text = models.TextField(null=True, blank=True, verbose_name='qo\'shimcha ma\'lumot')

    def __str__(self) -> str:
        return self.name


class Company(models.Model):
    logo = models.ImageField(upload_to='logo/', verbose_name='Kompaniya Logotipi')
    name = models.CharField(max_length=250, default='DAVAN', verbose_name='Kompaniya nomi')
    video = models.URLField(verbose_name='Video havolasi(linki)')


class Product(models.Model):
    STATUS = (
        ('bel', 'Бел'),
        ('boyin', 'Бўйин'),
        ('soyabon', 'Ёмғир'),
    )
    name = models.CharField(max_length=250, verbose_name='Номи', null=True, blank=True)
    image = models.ImageField(upload_to='products/', verbose_name='Расм', default='none.png')
    narxi = models.DecimalField(max_digits=12, decimal_places=0, verbose_name='Narxi')
    optom_narxi = models.DecimalField(max_digits=12, decimal_places=0, verbose_name='Optom narxi')
    tur = models.CharField(max_length=100, choices=STATUS, default='bel', verbose_name='Kategoriya')
    batafsil = models.TextField(null=True, blank=True, verbose_name='Qo\'shimcha malumot')

    def narx_format(self):
        return f"{int(self.narxi):,}".replace(',', ' ')
    def optom_narx_format(self):
        return f"{int(self.optom_narxi):,}".replace(',', ' ')
    
    def __str__(self) -> str:
        return self.name + ': ' + self.tur


class Comment(models.Model):
    full_name = models.CharField(max_length=350, default='Nomalum', verbose_name='F.I.SH')
    photo = models.ImageField(upload_to='comments/', default='none.png', verbose_name='Foydalanuvchi rasmi')
    comment = models.TextField(verbose_name='izoh')

    def __str__(self):
        return self.full_name


class Taklif(models.Model):
    full_name = models.CharField(max_length=359, default='Nomalum')
    phone_number = models.CharField(max_length=20, verbose_name='Telefon raqam')
    address = models.CharField(max_length=450, null=True, blank=True)
    batafsil = models.TextField(verbose_name='Buyurtma haqida malumot')

    def __str__(self):
        return self.full_name
    

class Buyurtma(models.Model):
    full_name = models.CharField(max_length=359, default='Nomalum')
    phone_number = models.CharField(max_length=20, verbose_name='Telefon raqam')
    address = models.CharField(max_length=450, null=True, blank=True)
    batafsil = models.TextField(verbose_name='Buyurtma haqida malumot')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True, related_name='products')

    def __str__(self):
        return self.full_name
    