from django.db import models

# Create your models here.

class Bank(models.Model):
  account_number=models.IntegerField()
  name=models.CharField(max_length=23)
  age=models.IntegerField()
  gender=models.CharField(choices=[('male','male'),('female','female')],max_length=29)
  dob=models.DateField()
  balance=models.IntegerField()


  def __str__(self):
    return f"{self.name} - Balance: {self.balance}"

  


  
  

class Transaction(models.Model):
    from_account = models.ForeignKey('Bank', on_delete=models.CASCADE, related_name='outgoing_transactions')
    to_account = models.ForeignKey('Bank', on_delete=models.CASCADE, related_name='incoming_transactions')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, default="Pending")
    created_at = models.DateTimeField(auto_now_add=True)

  
  

