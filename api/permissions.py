from rest_framework.permissions import BasePermission
from rest_framework.permissions import SAFE_METHODS

class IsAdminOrReadOnly(BasePermission):
  """
  Custom permission class:
    - Admin (authenticated) can create, update, and delete books.
    - Students (unauthenticated users) can only read books.
  """

  def has_permission(self, request, view):
    #Allow read-only access to all users
    if request.method in SAFE_METHODS:
      return True
    
    #Only authenticated admins can modify or create books
    return request.user.is_superuser