from django.urls import path
from library_app.views import Book_add,add_form,view,update,update_view,deletebook,deletebook1,display_books,custom_logout,search
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [

    path("add/",Book_add),
    path('addBook/',add_form),
    path("",view,name='home'),
    path('up/',update),
    path('update_view/',update_view),
    path('deletebook/',deletebook),
    path('deletebook1/',deletebook1),
    path('view/',display_books),
    path('search/',search),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
