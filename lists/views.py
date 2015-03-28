<<<<<<< HEAD
from django.shortcuts import redirect, render
from lists.models import Item
#from django.http import HttpResponse
=======
from django.shortcuts import render
from django.http import HttpResponse
>>>>>>> b8a368306af0c1e7d3157cd2fc799da72a8e44e9

# Create your views here.
def home_page(request):
  #if request.method == 'POST':
    #return HttpResponse(request.POST['item_text'])
  #return HttpResponse('<html><title>To-Do lists</title></html>')
<<<<<<< HEAD
  if request.method == 'POST':
    Item.objects.create(text=request.POST['item_text'])
    return redirect('/')

  items = Item.objects.all()
  return render(request, 'home.html', {'items': items})
=======
  return render(request, 'home.html', {
    'new_item_text': request.POST.get('item_text', ''),
  })
>>>>>>> b8a368306af0c1e7d3157cd2fc799da72a8e44e9

