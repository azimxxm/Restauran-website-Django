from django.db import models

class Pizza(models.Model):
    title = models.CharField(max_length=20)
    info = models.TextField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='Pizza/')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Salad(models.Model):
    title = models.CharField(max_length=20)
    info = models.TextField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='Pizza/')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Noodle(models.Model):
    title = models.CharField(max_length=20)
    info = models.TextField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='Pizza/')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Famous(models.Model):
    title = models.CharField(max_length=20)
    info = models.TextField(max_length=255)
    url = models.URLField()
    image = models.ImageField(upload_to='Pizza/')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Person(models.Model):
    name = models.CharField(max_length=50)
    work_type = models.CharField(max_length=50)
    info = models.TextField(max_length=100)
    facebook = models.URLField()
    telegram = models.URLField()
    instagram = models.URLField()
    image = models.ImageField(upload_to='Person/')

    def __str__(self):
        return self.name


class History(models.Model):
    name = models.CharField(max_length=50)
    info_1 = models.TextField(max_length=100)
    info_2 = models.TextField(max_length=100)
    url = models.URLField()
    image = models.ImageField(upload_to='Person/')

    def __str__(self):
        return self.name

class Banner(models.Model):
    image = models.ImageField(upload_to='Banner/')

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    message = models.TextField(max_length=255)

    def __str__(self):
        return self.name