from rest_framework import serializers
from .models import Books, bookReviews, Stores


        
class bookReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = bookReviews
        fields = [
            'id',
            'Book',
            'Review_User',
            'Rating',
            'Review',
            'DateAdded'
            ]
        
class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stores
        fields = [
            'id',
            'storeName',
            'location',
            'books_available',
            'Date_Added'
            ]
        
class BookSerializer(serializers.ModelSerializer):
    stores_available = StoreSerializer(many=True, read_only=True, source='available_in')
    class Meta:
        model = Books
        fields = [
            'id',
            'BookName',
            'Author',
            'num_pages',
            'description',
            'stores_available',
            'Date_Added'
            ]