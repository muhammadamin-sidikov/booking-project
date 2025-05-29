from rest_framework import viewsets, permissions
from .models import Booking
from .serializers import BookingSerializer, BookingListSerializer
from rest_framework import viewsets
from .models import Booking
from .serializers import BookingSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingListSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'create':
            return BookingSerializer
        return BookingListSerializer


