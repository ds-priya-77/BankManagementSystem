from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib import messages

# Create your views here.

#-------------------- Add ----------------------------------
def Add(request):
  context={
    'form_data':BankForm()
  }

  if request.method=='POST':
    data=BankForm(request.POST)
    if data.is_valid():
      data.save()
      

  return render(request,'add.html',context)


#------------------ Trans ----------------------------------
'''
def trans(request):
  if request.method=='POST':


    fromid=request.POST.get('fromid')
    toid=request.POST.get('toid')
    amount=request.POST.get('amount',0)

    if fromid != toid:
      from_account=Bank.objects.get(id=fromid)
      to_account=Bank.objects.get(id=toid)
      
      if from_account.balance >= amount:
        from_account.balance-=amount
        to_account.balance+=amount
        from_account.save()
        to_account.save()
        


        Transaction.objects.create(

           from_account=from_account,
           to_account=to_account,
           amount=amount,
           status='Success'


        )

        messages.success(request,'Transaction successfull')
        return redirect('/his/')

      else:
        messages.error(request,'Insufficient balance.')


    else:
      messages.error(request,'Two Accounts Must be Different.')

  else:
    context={
      'all_data':Bank.objects.all(),
      'trans_form':TransForm()
    }
    return render(request,'trans.html',context)
  





def trans(request):
    context={
           'trans_form' : TransForm()
        }
    if request.method == "POST":
        form = TransForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/his/')
    
        

    return render(request, 'trans.html', context)


    '''







def trans(request):
    if request.method == "POST":
        form = TransForm(request.POST)

        if form.is_valid():
            from_account = form.cleaned_data['from_account']
            to_account = form.cleaned_data['to_account']
            amount = form.cleaned_data['amount']

            if from_account == to_account:
                messages.error(request, "Source and destination accounts must be different.")
            elif from_account.balance < amount:
                messages.error(request, "Insufficient balance.")
            else:
                # Perform the transaction
                from_account.balance -= amount
                to_account.balance += amount
                from_account.save()
                to_account.save()

                # Log the transaction
                Transaction.objects.create(
                    from_account=from_account,
                    to_account=to_account,
                    amount=amount,
                    status="Success"
                )
                messages.success(request, "Transaction successful!")
                return redirect('/his/')

    else:
        form=TransForm()
        

    return render(request, 'trans.html', {'trans_form':form})





def History(request):
    context={
       'all_data' : Transaction.objects.all()
      }  # Retrieve all transactions
    return render(request, 'his.html', context)
