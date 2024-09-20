from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Books, bookReviews, Stores
from .serializers import BookSerializer, bookReviewSerializer, StoreSerializer
from django.contrib.auth.decorators import login_required

# API view to list all books or create a new book
class BookListCreateAPIview(generics.ListCreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        print(serializer.validated_data)
        BookName = serializer.validated_data.get('BookName')
        description = serializer.validated_data.get('description', BookName)
        serializer.save(description=description)

# API view to retrieve the details of a specific book
class BookDetailAPIview(generics.RetrieveAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer

# API view to list all books
class BookListAPIview(generics.ListAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer

# API view to list all reviews or create a new review
class ReviewListCreateAPIView(generics.ListCreateAPIView):
    queryset = bookReviews.objects.all()
    serializer_class = bookReviewSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        print(serializer.validated_data)
        serializer.save()

# API view to retrieve the details of a specific review
class ReviewDetailAPIview(generics.RetrieveAPIView):
    queryset = bookReviews.objects.all()
    serializer_class = bookReviewSerializer

# API view to list all reviews, sorted by the date they were added (most recent first)
class ReviewListAPIview(generics.ListAPIView):
    serializer_class = bookReviewSerializer

    def get_queryset(self):
        return bookReviews.objects.all().order_by('-DateAdded')

# API view to list reviews for a specific book, identified by its book_id
class BookReviewListAPIview(generics.ListAPIView):
    serializer_class = bookReviewSerializer

    def get_queryset(self):
        book_id = self.kwargs.get('book_id')
        if book_id:
            return bookReviews.objects.filter(Book_id=book_id).order_by('-DateAdded')
        return Response({"error": "No book specified"}, status=status.HTTP_400_BAD_REQUEST)

# API view to retrieve, update, or delete a specific review
class ReviewRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = bookReviews.objects.all()
    serializer_class = bookReviewSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({
            'message': 'Review updated successfully.',
            'updated_review': serializer.data
        })

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        response_data = {
            'Book': instance.Book.BookName,
            'Review_User': instance.Review_User.username,
            'Rating': instance.Rating,
            'Review': instance.Review,
            'DateAdded': instance.DateAdded,
        }
        self.perform_destroy(instance)
        return Response({
            'message': 'Review deleted successfully.',
            'deleted_review': response_data
        }, status=status.HTTP_200_OK)

# API view to list or create stores, only accessible to store users
class StoreListCreateAPIView(generics.ListCreateAPIView):
    queryset = Stores.objects.all()
    serializer_class = StoreSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    # permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        print(serializer.validated_data)
        serializer.save()

# API view to list all stores, only accessible to store users
class StoreListAPIview(generics.ListAPIView):
    queryset = Stores.objects.all()
    serializer_class = StoreSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Stores.objects.all().order_by('-DateAdded')

# API view to list stores where a specific book is available, only accessible to store users
class BookStoreListAPIview(generics.ListAPIView):
    serializer_class = StoreSerializer
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        book_id = self.kwargs.get('book_id')
        return Stores.objects.filter(books_available__id=book_id).order_by('-DateAdded')

# API view to retrieve, update, or delete a specific store
class StoreRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Stores.objects.all()
    serializer_class = StoreSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({
            'message': 'Store updated successfully.',
            'updated_store': serializer.data
        })

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        response_data = {
            'storeName': instance.storeName,
            'location': instance.location,
            'books_available': list(instance.books_available.values('id', 'BookName'))
        }
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


#+--------------------------------------------------------------------------------------------------------------+
#UNUSED LOGIC:

    # # Handle adding books to the store
    # books_to_add = data.get('books_to_add', [])
    # if books_to_add:
    #     for book_id in books_to_add:
    #         try:
    #             book = Books.objects.get(id=book_id)
    #             instance.books_available.add(book)
    #         except Books.DoesNotExist:
    #             return Response({'error': f'Book with id {book_id} does not exist.'}, status=status.HTTP_400_BAD_REQUEST)
    #
    # # Handle removing books from the store
    # books_to_remove = data.get('books_to_remove', [])
    # if books_to_remove:
    #     for book_id in books_to_remove:
    #         try:
    #             book = Books.objects.get(id=book_id)
    #             instance.books_available.remove(book)
    #         except Books.DoesNotExist:
    #             return Response({'error': f'Book with id {book_id} does not exist.'}, status=status.HTTP_400_BAD_REQUEST)
