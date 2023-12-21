from django.db import models

# Create your models here.
class Dept(models.Model):
    dept_no=models.IntegerField(primary_key=True) 
    dname=models.CharField(max_length=100)
    loc=models.CharField(max_length=100)
    
    def __str__(self):
        return self.dname
    



class Emp(models.Model):
    emp_no=models.IntegerField()
    ename=models.CharField(max_length=100)
    job=models.CharField(max_length=100)
    hiredate=models.DateField()
    sal=models.IntegerField()
    comm=models.IntegerField()
    dept_no=models.ForeignKey(Dept,on_delete=models.CASCADE)

    def __str__(self):
        return self.ename
    

    
    
