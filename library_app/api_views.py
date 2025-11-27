from rest_framework import viewsets
from library_app.models import Book_info
from library_app.serializers import LibrarySerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
class BooksApiviews(viewsets.ModelViewSet):
    queryset=Book_info.objects.all()
    serializer_class=LibrarySerializer
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    lookup_field = 'Book_id'