from django.shortcuts import redirect, render
from lists.models import Item

# Create your views here.
def home_page(request):
  #if request.method == 'POST':
    #return HttpResponse(request.POST['item_text'])
  #return HttpResponse('<html><title>To-Do lists</title></html>')
  if request.method == 'POST':
    Item.objects.create(text=request.POST['item_text'])
    return redirect('/')

  items = Item.objects.all()
  return render(request, 'home.html', {'items': items})

