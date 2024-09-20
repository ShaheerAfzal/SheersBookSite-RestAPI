from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models import Avg
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.conf import settings  # Import settings for AUTH_USER_MODEL

# Create your models here.

class Books(models.Model):
    BookName = models.CharField(max_length=150)
    Author = models.CharField(max_length=100)
    num_pages = models.IntegerField(default= 0)
    description = models.TextField(blank=True, null=True)
    Date_Added = models.DateTimeField(default=timezone.now)
    def maxLimInt(self):
        # Check if num_pages is within the 6-digit limit
        if self.num_pages < 1 or self.num_pages > 999999:
            raise ValidationError("num_pages must be between 1 and 999,999.")

    def save(self, *args, **kwargs):
        # Call maxLimInt before saving
        self.maxLimInt()
        super(Books, self).save(*args, **kwargs)

    def __str__(self):
        return self.BookName
    
class bookReviews(models.Model):
    Book = models.ForeignKey(Books, on_delete=CASCADE, related_name='Reviews')
    Review_User = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    Rating = models.IntegerField(default=1, choices=[(i, str(i)) for i in range(1, 6)])
    Review = models.TextField(blank=True, null=True)
    DateAdded = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Update the Stars field in the related Book
        average_rating = self.Book.Reviews.aggregate(Avg('Rating'))['Rating__avg'] or 0.0
        self.Book.Stars = round(average_rating, 1)
        self.Book.save()
    def __str__(self):
        return f'Review by {self.Review_User.username} for {self.Book.BookName} - Rating: {self.Rating}'

class Stores(models.Model):
    storeName = models.CharField(max_length=150)
    location = models.TextField(max_length=500)
    books_available = models.ManyToManyField(Books, related_name= "available_in")
    # booksToAdd = models.ManyToManyField(Books, related_name='Temp_ToAdd')
    # booksToDel = models.ManyToManyField(Books, related_name='Temp_ToRemove')
    Date_Added = models.DateTimeField(default=timezone.now)

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)

    #     # Add books from booksToAdd to books_available
    #     for book in self.booksToAdd.all():
    #         self.books_available.add(book)

    #     # Remove books from booksToDel from books_available
    #     for book in self.booksToDel.all():
    #         self.books_available.remove(book)

    #     # Clear booksToAdd and booksToDel after updating books_available
    #     self.booksToAdd.clear()
    #     self.booksToDel.clear()
        
    def __str__(self):
        return self.storeName