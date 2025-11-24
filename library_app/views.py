from django.shortcuts import render,redirect
from library_app.models import Book_info
from django.http import HttpResponse
from library_app.forms import Book_form
from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import Book_info
@login_required
def Book_add(request):
    if request.method == "POST":
        s=Book_info.objects.values()
        # for i in s:
        #     if int(Book_id) ==i['Book_id']:
        #         return render(request, "homeapp2.html", {"sA": "Book id is already existed"})
        form = Book_form(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=True)
            return render(request, "homeapp2.html", {"sA": "Your Book added successfully"})
        else:
            return render(request, "homeapp2.html", {"sA": "please add  your book again"})

@login_required
def add_form(request):
    f=Book_form()
    return render(request,"homeapp.html",context={"f":f})
def view(request):
    return render(request,"homeapp2.html")

def update(request):
    """ Book_id=models.IntegerField(primary_key=True)
    Book_name=models.CharField(max_length=69)
    Book_price=models.FloatField()
    Book_publication=models.CharField(max_length=69)
    Book_publish_year=models.DateField(default=date.today())
    Book_quantity=models.CharField(max_length=69)
    """
    Book_id=request.POST['Book_id']
    Book_name=request.POST['Book_name']
    Book_price=request.POST['Book_price']
    Book_publication=request.POST['Book_Author']
    Book_publish_year=request.POST['Book_publish_year']  #YYYY-MM-DD
    Book_quantity=request.POST['Book_quantity']
    Book_stack= True if request.POST.get('Book_stack') == 'on' else False
    Book_image = request.FILES.get('Book_image') 
    try:
        cn=Book_info.objects.get(Book_id=Book_id)
        cn.Book_name=Book_name
        cn.Book_price=Book_price
        cn.Book_Author=Book_publication
        cn.Book_publish_year=Book_publish_year
        cn.Book_quantity=Book_quantity
        cn.Book_stack=Book_stack
        cn.Book_image= Book_image
        cn.save()
        return render(request,'homeapp2.html',context={"sA":"Successfully Updated"})
    except:
        return render(request,'homeapp2.html',context={"sA":"Please Add New book your Book id not available"})
@login_required
def update_view(request):
    f=Book_form()
    return render(request,"update.html",context={'f':f})
@login_required
def deletebook(request):
    avbook=Book_info.objects.all()
    return render(request,'deletebook.html',context={"avbook":avbook})
def deletebook1(request):
    cn=int(request.GET['bookid'])
    delete1=Book_info.objects.get(Book_id=cn)
    avbook=Book_info.objects.all()
    delete1.delete()
    return render(request,'deletebook.html',context={"bookdetails":"Deleted Successfully","bookid":cn,"avbook":avbook})
#display all books data
def display_books(request):
    Books=Book_info.objects.all()
    return render(request,"display.html",context={"Books":Books})
#searching required Book based on id
def search(request):
    book=request.GET['search1']
    if book.isdigit():
        try:
            data=Book_info.objects.get(Book_id=int(book))
            return render(request,"searching.html",context={"data":data})
        except Book_info.DoesNotExist:
            return render(request,"searching.html")
    data=Book_info.objects.filter(Book_name=book)
    return render(request,"searching.html",context={"data":data})
#logout page
from django.contrib.auth import logout
from django.shortcuts import redirect

def custom_logout(request):
    logout(request)   # Logs out the current user 
    return redirect('/app') 