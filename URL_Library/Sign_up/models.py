from django.db import models
import bcrypt
# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    REQUIRED_FIELDS = ['email', 'username', 'name', 'password']
    USERNAME_FIELD = 'username'

    def SetPassword(self, raw_password):
        self.password = bcrypt.hashpw(raw_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        self.save()
        
    def CheckPassword(self, raw_password):
        return bcrypt.checkpw(raw_password.encode('utf-8'), self.password.encode('utf-8'))
    
    def UpdatePassword(self, raw_password):
        self.SetPassword(raw_password)
        
    def UpdateUsername(self, new_username):
        self.username = new_username
        self.save()
        
    def UpdateEmail(self, new_email):
        self.email = new_email
        self.save()
        
    def updateName(self, new_name):
        self.name = new_name
        self.save()
        
    def __str__(self):
        return self.username    

class UserContent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    URL = models.URLField(max_length=200)
    QrCode = models.ImageField(upload_to='qrcodes/', null=True, blank=True)
    video = models.FileField(upload_to='videos/', null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Content for {self.user.username}"