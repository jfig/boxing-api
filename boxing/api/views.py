from rest_framework import viewsets
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import list_route
from rest_framework.response import Response

from boxing.api.serializers import *
from boxing.api.models import *
from boxing.api import filtersets

class AccountViewSet(viewsets.ModelViewSet):
    """
    A list of users
    """
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    @list_route(permission_classes=[IsAuthenticated])
    def me(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)

class CategoryViewSet(viewsets.ModelViewSet):
    """
    A list of categories to categorize items
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ContainerViewSet(viewsets.ModelViewSet):
    """
    A list of containers
    """
    queryset = Container.objects.all()
    serializer_class = ContainerSerializer
    ordering_fields = ('name',)
    ordering = 'name'

class ItemViewSet(viewsets.ModelViewSet):
    """
    A list of items
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_class = filtersets.ItemFilterSet
    search_fields = ('name', )

class LendingViewSet(viewsets.ModelViewSet):
    """
    A list of lendings
    """
    queryset = Lending.objects.all()
    serializer_class = LendingSerializer
    permission_classes = [IsAuthenticated]
    filter_class = filtersets.LendingFilterSet

    def get_serializer(self, *args, **kwargs):
        """
        Passes extra kwarg to serializer class
        if user is staff, to allow for read_only_fields
        modification on runtime
        """
        if self.request.user.is_authenticated() and self.request.user.is_staff:
            kwargs['override_read_only_fields'] = ('state', 'return_date')
        return super(LendingViewSet, self).get_serializer(*args, **kwargs)

class MediaViewSet(viewsets.ModelViewSet):
    """
    A list of media items
    """
    queryset = Media.objects.all()
    serializer_class = MediaSerializer
    filter_class = filtersets.MediaFilterSet
    permission_classes = [IsAuthenticated]

class PhotoViewSet(viewsets.ModelViewSet):
    """
    A list of photos
    """
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = [IsAuthenticated]

class RelatedViewSet(viewsets.ModelViewSet):
    """
    A list of related items
    """
    queryset = Related.objects.all()
    serializer_class = RelatedSerializer
