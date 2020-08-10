from django.shortcuts import render
from .models import Destination
# Create your views here.
def index(request):

    #dests=Destination.objects.all()
    #<img src="{{dest.img.url}}" alt="">
    #   or 
    dest1=Destination()
    dest1.name='Mumbai'
    dest1.desc='The City That Never Sleeps'
    dest1.img='destination_1.jpg'
    dest1.price='700'
    dest1.offer=False

    dest2=Destination()
    dest2.name='Hyderabad'
    dest2.desc='First Biryani,Then Sherwani'
    dest2.img='destination_2.jpg'
    dest2.price='650'
    dest2.offer=True

    dest3=Destination()
    dest3.name='Bengaluru'
    dest3.desc='Beautiful City'
    dest3.img='destination_3.jpg'
    dest3.price='750'

    dest4=Destination()
    dest4.name='Assam'
    dest4.desc='Aloo Pitika – Comfort food of Assam!'
    dest4.img='destination_4.jpg'
    dest4.price='700'
    dest4.offer=False

    dest5=Destination()
    dest5.name='Punjab'
    dest5.desc='Makke ki Roti and Sarson ka Saag'
    dest5.img='destination_5.jpg'
    dest5.price='700'
    dest5.offer=True

    dest6=Destination()
    dest6.name='South India'
    dest6.desc='Masala dosa is the most popular South Indian '
    dest6.img='destination_6.jpg'
    dest6.price='700'
    dest6.offer=True
 
    dests=[dest1,dest2,dest3,dest4,dest5,dest6]

    return render(request,'index.html',{'dests':dests})
    #return render(request,'index.html',{'price':700})
def contact(request):
    return render(request,'contact.html')
def news(request):
    return render(request,'news.html')
def about(request):
    return render(request,'about.html')
def destinations(request):
    return render(request,'destinations.html') 
def elements(request):
    return render(request,'elements.html')    
def home(request):
    return render(request,'home.html')                           
