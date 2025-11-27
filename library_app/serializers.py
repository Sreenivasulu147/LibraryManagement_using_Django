from rest_framework.serializers import ModelSerializer
from library_app.models import Book_info
class LibrarySerializer(ModelSerializer):
    class Meta:
        model=Book_info
        fields="__all__"