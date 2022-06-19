from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
import datetime
now = datetime.date.today()

class Post(models.Model):
    title=models.CharField(max_length=10000,blank=False,verbose_name='Название статьи')
    text=RichTextUploadingField(max_length=10000,blank=False,verbose_name='текст')
    photo = models.ImageField(upload_to='post_images',null=False,blank=False,verbose_name="выбрать фото")
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.title

class Work(models.Model):
    title = models.CharField(max_length=30,verbose_name="Имя фамилие работающих людей",null=False,blank=False)
    totle = models.CharField(max_length=50,verbose_name="должность",null=False,blank=False)
    tel_number = models.CharField(max_length=20,verbose_name="Номера сотрудников",null=False,blank=False)
    photo = models.ImageField(upload_to='post_images',null=False,blank=False,verbose_name="Фоторафия сотрудника")

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return self.title

class Articles(models.Model):
    title = models.CharField(max_length=30,verbose_name="имя пользователя",null=False,blank=False)
    email = models.EmailField(verbose_name="Email",null=False,blank=False)
    text = models.CharField(max_length=300,verbose_name="Текст",null=False,blank=False)

    class Meta:
        verbose_name = 'Коментарие'
        verbose_name_plural = 'Коментарии'

    def __str__(self):
        return self.title

class Contacts(models.Model):
    title = models.CharField(max_length=30, verbose_name="имя пользователя",null=False,blank=False)
    email = models.EmailField(verbose_name="Email",null=False,blank=False)
    phone_number = models.CharField(max_length=30,verbose_name="Номер телефона",null=False,blank=False)
    text = models.CharField(max_length=300, verbose_name="Текст",null=False,blank=False)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return self.title

class News(models.Model):
    title = models.CharField(max_length=30, verbose_name="Название новостей", null=False, blank=False)
    text = models.CharField(max_length=300, verbose_name="Текст", null=False, blank=False)
    photo = models.ImageField(upload_to='post_images',null=False,blank=False,verbose_name="Фото новостей")
    date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title

class Aboutcomp(models.Model):
    title = models.CharField(max_length=30, verbose_name="Корхонамиз хакида", null=False, blank=False)
    text = models.CharField(max_length=300, verbose_name="Текст", null=False, blank=False)
    photo = models.ImageField(upload_to='post_images', null=False, blank=False, verbose_name="Фото о нашей компании")

    class Meta:
        verbose_name = 'Информация'
        verbose_name_plural = 'Информации'

    def __str__(self):
        return self.title