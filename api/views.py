from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import AdminSignupSerializer, BookSerializer
from .permissions import IsAdminOrReadOnly
from rest_framework.permissions import IsAuthenticated
from .models import Book
from django.shortcuts import get_object_or_404

# Create your views here.

class AdminSignupView(APIView):
  """
  API to register a new admin user. Only existing admin can create new admin.
  """

  permission_classes= [IsAuthenticated]

  def post(self,request):
    serializer = AdminSignupSerializer(data=request.data)

    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class BookView(APIView):
  """
  Handles all CRUD operations for Books
   - Students can only read books  
   - Admins can create, update, and delete books 
  """

  permission_classes = [IsAdminOrReadOnly]

  def get(self, request, pk=None):
    """List all books or retrieve a single book (accessible by both students & admin)"""

    if pk:
      book = get_object_or_404(Book, pk=pk)  # Returns 404 if book is not found
      serializer = BookSerializer(book)
    else:
      books = Book.objects.all()
      serializer = BookSerializer(books, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)
  
  def post(self, request):
    """Create a new book (Admin only)"""

    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  def put(self, request, pk):
    """Update a book (Admin only)"""

    book = get_object_or_404(Book,pk=pk)
    serializer = BookSerializer(book, data=request.data, partial=True)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  def delete(self, request, pk):
    """Delete a book (Admin only)"""

    book = get_object_or_404(Book,pk=pk)
    book.delete()
    return Response({'message': 'Book deleted succcessfully'}, status=status.HTTP_204_NO_CONTENT)
