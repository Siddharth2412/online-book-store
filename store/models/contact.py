from django.db import models



class Contact(models.Model):
    Name=models.CharField(max_length=70,null=True) 
    Phone=models.CharField(max_length=14,null=True)
    Email=models.CharField(max_length=70,null=True)
    Message=models.CharField(max_length=500,null=True)

    def __str__(self):
        return self.Name


class Feedback(models.Model):
    Comment=models.CharField(max_length=30,null=True)
    line2=models.CharField(max_length=30,null=True)
    line3=models.CharField(max_length=30,null=True)
    line4=models.CharField(max_length=30,null=True)
    F_Name=models.CharField(max_length=70,null=True) 
    Email=models.CharField(max_length=70,null=True)

