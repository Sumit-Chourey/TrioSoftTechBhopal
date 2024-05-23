from django.db import models

# Create your models here.
# Creating a own Models here is Like Entity class

class TrioCompany(models.Model):
    company_id = models.AutoField(primary_key=True)
    name=models.CharField( max_length=50)
    location= models.CharField(max_length=50)
    about= models.TextField(null=True)
    type=models.CharField(max_length=50,choices=(('IT','IT'),('NON IT','NON IT'),('MOBILE PHONE','MOBILE PHONE')))
    added_date=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)
    


#Override one method

def __str__(self):
    return self.name

#Creating Matrixsoft sub branch of Triosoft company to show One to Many relation
     
class MatrixSoft(models.Model):
    name= models.CharField(max_length=100)
    email=models.CharField(max_length=50)
    address=models.CharField(max_length=200)
    phone=models.CharField(max_length=10)
    about=models.TextField()
    position = models.CharField(max_length=50,choices=(('Manager','Manager'),('Software Developer','Sr.Developer'),('Project Lead','Sub-Manager')))        
    
    
company_id=models.ForeignKey(TrioCompany, on_delete=models.CASCADE)    
    
    
    
