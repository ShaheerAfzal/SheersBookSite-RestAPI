from rest_framework import generics, status
from rest_framework.response import Response

from .models import Books, bookReviews, Stores
from .serializers import BookSerializer, bookReviewSerializer, StoreSerializer

# API view to list all books or create a new book
class BookListCreateAPIview(generics.ListCreateAPIView):
    queryset = Books.objects.all()  # Retrieve all books from the database
    serializer_class = BookSerializer  # Use the BookSerializer to serialize/deserialize book data

    # Override the method to customize how the book is saved when a new book is created
    def perform_create(self, serializer):
        # Print the validated data for debugging purposes
        print(serializer.validated_data)
        
        # Extract the BookName from the validated data
        BookName = serializer.validated_data.get('BookName')
        
        # Extract the description if provided
        if serializer.validated_data.get('description'):
            description = serializer.validated_data.get('description') 
        else:
            description = None
        
        # If no description is provided, default it to the BookName
        if description is None:
            description = BookName
        
        # Save the book instance with the finalized description
        serializer.save(description=description)

# API view to retrieve the details of a specific book
class BookDetailAPIview(generics.RetrieveAPIView):
    queryset = Books.objects.all()  # Retrieve all books from the database
    serializer_class = BookSerializer  # Use the BookSerializer to serialize/deserialize book data
    #lookup = 'pk'  # The default lookup field is 'pk' (primary key)

# API view to list all books without any creation functionality
class BookListAPIview(generics.ListAPIView):
    queryset = Books.objects.all()  # Retrieve all books from the database
    serializer_class = BookSerializer  # Use the BookSerializer to serialize/deserialize book data
    #lookup = 'pk'  # The default lookup field is 'pk' (primary key)

# API view to list all reviews or create a new review
class ReviewListCreateAPIView(generics.ListCreateAPIView):
    queryset = bookReviews.objects.all()  # Retrieve all reviews from the database
    serializer_class = bookReviewSerializer  # Use the bookReviewSerializer to serialize/deserialize review data

    # Override the method to customize how the review is saved when a new review is created
    def perform_create(self, serializer):
        # Print the validated data for debugging purposes
        print(serializer.validated_data)
        
        # Save the review instance with the provided data
        serializer.save()
        # The following code is commented out and can be used if custom logic for saving the review is needed.
        # Book = serializer.validated_data.get('Book')
        # if serializer.validated_data.get('Review'):
        #     Review = serializer.validated_data.get('Review') 
        # else:
        #     Review = None
        # if Review is None:
        #     Review = Book
        # serializer.save(Review=Review)

# API view to retrieve the details of a specific review
class ReviewDetailAPIview(generics.RetrieveAPIView):
    queryset = bookReviews.objects.all()  # Retrieve all reviews from the database
    serializer_class = bookReviewSerializer  # Use the bookReviewSerializer to serialize/deserialize review data

# API view to list all reviews, sorted by the date they were added (most recent first)
class ReviewListAPIview(generics.ListAPIView):
    serializer_class = bookReviewSerializer  # Use the bookReviewSerializer to serialize/deserialize review data

    # Override the method to customize the queryset returned
    def get_queryset(self):
        # Retrieve all reviews and sort them by DateAdded in descending order
        return bookReviews.objects.all().order_by('-DateAdded')
    #lookup = 'pk'  # The default lookup field is 'pk' (primary key)

# API view to list reviews for a specific book, identified by its book_id
class BookReviewListAPIview(generics.ListAPIView):
    serializer_class = bookReviewSerializer  # Use the bookReviewSerializer to serialize/deserialize review data

    # Override the method to customize the queryset returned
    def get_queryset(self):
        # Get the book_id from the URL parameters, if provided
        book_id = self.kwargs.get('book_id')
        
        if book_id:
            # If a book_id is provided, filter reviews by that book and sort by DateAdded in descending order
            return bookReviews.objects.filter(Book_id=book_id).order_by('-DateAdded')
        
        # If no book_id is provided, return an error message (this would typically cause an error in practice)
        return {"NoBookError": "No book was specified"} 
    #lookup = 'pk'  # The default lookup field is 'pk' (primary key)

# API view to retrieve, update, or delete a specific review
class ReviewRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = bookReviews.objects.all()  # Retrieve all reviews from the database
    serializer_class = bookReviewSerializer  # Use the bookReviewSerializer to serialize/deserialize review data

    # Override the update method to customize how a review is updated
    def update(self, request, *args, **kwargs):
        # Get the current review instance that needs to be updated
        instance = self.get_object()
        
        # Serialize the incoming data, allowing partial updates (i.e., not all fields are required)
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)  # Validate the data
        
        # Save the updated review instance
        self.perform_update(serializer)

        # Return a success response with the updated review data
        return Response({
            'message': 'Review updated successfully.',
            'updated_review': serializer.data
        })

    # Override the destroy method to customize how a review is deleted
    def destroy(self, request, *args, **kwargs):
        # Get the current review instance that needs to be deleted
        instance = self.get_object()
        
        # Prepare data about the review being deleted for the response
        response_data = {
            'Book': instance.Book.BookName,
            'Review_User': instance.Review_User.username,
            'Rating': instance.Rating,
            'Review': instance.Review,
            'DateAdded': instance.DateAdded,
        }
    
        # Delete the review instance
        self.perform_destroy(instance)

        # Return a success response with details of the deleted review
        return Response({
            'message': 'Review deleted successfully.',
            'deleted_review': response_data
        }, status=status.HTTP_200_OK)

class StoreListCreateAPIView(generics.ListCreateAPIView):
    queryset = Stores.objects.all()  # Retrieve all Stores from the database
    serializer_class = StoreSerializer  # Use the StoreSerializer to serialize/deserialize review data

    # Override the method to customize how the Store is saved when a new review is created
    def perform_create(self, serializer):
        # Print the validated data for debugging purposes
        print(serializer.validated_data)
        
        # Save the review instance with the provided data
        serializer.save()

class StoreListAPIview(generics.ListAPIView):
    serializer_class = StoreSerializer  # Use the StoreSerializer to serialize/deserialize review data

    # Override the method to customize the queryset returned
    def get_queryset(self):
        # Retrieve all reviews and sort them by DateAdded in descending order
        return Stores.objects.all().order_by('-DateAdded')
    #lookup = 'pk'  # The default lookup field is 'pk' (primary key)

class BookStoreListAPIview(generics.ListAPIView):
    serializer_class = StoreSerializer

    def get_queryset(self):

        # Retrieve the book_id from the URL parameters
        book_id = self.kwargs.get('book_id')

        # Filter stores where the book with the given book_id is available
        queryset = Stores.objects.filter(books_available__id = book_id).order_by('-Date_Added')
        return queryset

class StoreRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Stores.objects.all()  # Retrieve all stores from the database
    serializer_class = StoreSerializer  # Use the StoreSerializer to serialize/deserialize store data

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = request.data

        # Handle adding books to the store
        books_to_add = data.get('books_to_add', [])
        if books_to_add:
            for book_id in books_to_add:
                try:
                    book = Books.objects.get(id=book_id)
                    instance.books_available.add(book)
                except Books.DoesNotExist:
                    return Response({'error': f'Book with id {book_id} does not exist.'}, status=status.HTTP_400_BAD_REQUEST)

        # Handle removing books from the store
        books_to_remove = data.get('books_to_remove', [])
        if books_to_remove:
            for book_id in books_to_remove:
                try:
                    book = Books.objects.get(id=book_id)
                    instance.books_available.remove(book)
                except Books.DoesNotExist:
                    return Response({'error': f'Book with id {book_id} does not exist.'}, status=status.HTTP_400_BAD_REQUEST)

        # Save any other changes to the store
        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response({
            'message': 'Store updated successfully.',
            'updated_store': serializer.data
        })

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        # Gather details about the store being deleted
        response_data = {
            'storeName': instance.storeName,
            'location': instance.location,
            'books_available': list(instance.books_available.values('id', 'BookName'))
        }

        # Delete the store instance
        self.perform_destroy(instance)

        return Response({
            'message': 'Store deleted successfully.',
            'deleted_store': response_data
        }, status=status.HTTP_200_OK)




#+-----------------------------------------------------------------------------------------------------------------------------------+

#below is the og code without most comments as i couldn't bring myself to go line by line to comment and asked gpt to add them in.
#thus im keeping the og code incase something goes wrong in the future so i can check if the problem persists in the original.

# from rest_framework import generics, status
# from rest_framework.response import Response

# from .models import Books, bookReviews, Stores
# from .serializers import BookSerializer, bookReviewSerializer

# class BookListCreateAPIview(generics.ListCreateAPIView):
#     queryset = Books.objects.all()
#     serializer_class= BookSerializer

#     def perform_create(self, serializer):
#         #serializer.save(user=self.request.user)
#         print(serializer.validated_data)
#         BookName = serializer.validated_data.get('BookName')
#         if serializer.validated_data.get('description'):
#             description = serializer.validated_data.get('description') 
#         else:
#             description = None
#         if description is None:
#             description = BookName
#         serializer.save(description=description)

# class BookDetailAPIview(generics.RetrieveAPIView):
#     queryset = Books.objects.all()
#     serializer_class= BookSerializer

#     #lookup = 'pk'

# class BookListAPIview(generics.ListAPIView):
#     queryset = Books.objects.all()
#     serializer_class= BookSerializer
#     #lookup = 'pk'

# class ReviewListCreateAPIView(generics.ListCreateAPIView):
#     queryset = bookReviews.objects.all()
#     serializer_class= bookReviewSerializer

#     def perform_create(self, serializer):
#         #serializer.save(user=self.request.user)
#         print(serializer.validated_data)
#         serializer.save()
#         #Book = serializer.validated_data.get('Book')
#         # if serializer.validated_data.get('Review'):
#         #     Review = serializer.validated_data.get('Review') 
#         # else:
#         #     Review = None
#         # if Review is None:
#         #     Review = Book
#         #serializer.save(Review=Review)

# class ReviewDetailAPIview(generics.RetrieveAPIView):
#     queryset = bookReviews.objects.all()
#     serializer_class= bookReviewSerializer

# class ReviewListAPIview(generics.ListAPIView):
#     # queryset = bookReviews.objects.all()
#     serializer_class= bookReviewSerializer
#     def get_queryset(self):
#         return bookReviews.objects.all().order_by('-DateAdded')  # Sort by DateAdded descending
#     #lookup = 'pk'

# class BookReviewListAPIview(generics.ListAPIView):
#     # queryset = bookReviews.objects.all()
#     serializer_class= bookReviewSerializer
#     def get_queryset(self):
#         # Get the book_id from the URL parameters, if provided
#         book_id = self.kwargs.get('book_id')
#         if book_id:
#             # Filter reviews by the specific book_id
#             return bookReviews.objects.filter(Book_id=book_id).order_by('-DateAdded')
#         # If no book_id is provided, return all reviews, or only say that no id was specified.
#         return {"NoBookError": "No book was specified"} #, bookReviews.objects.all().order_by('-DateAdded') 
#     #lookup = 'pk'

# class ReviewRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = bookReviews.objects.all()
#     serializer_class = bookReviewSerializer

#     def update(self, request, *args, **kwargs):
#         instance = self.get_object()
#         serializer = self.get_serializer(instance, data=request.data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         self.perform_update(serializer)

#         return Response({
#             'message': 'Review updated successfully.',
#             'updated_review': serializer.data
#         })

#     def destroy(self, request, *args, **kwargs):
#         instance = self.get_object()
#         response_data = {
#             'Book': instance.Book.BookName,
#             'Review_User': instance.Review_User.username,
#             'Rating': instance.Rating,
#             'Review': instance.Review,
#             'DateAdded': instance.DateAdded,
#         }

#         self.perform_destroy(instance)

#         return Response({
#             'message': 'Review deleted successfully.',
#             'deleted_review': response_data
#         }, status=status.HTTP_200_OK)