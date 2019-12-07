from rest_framework import viewsets, permissions
from .permissions import IsAdminOrPostOnly
from .models import Report
from .serializers import ReportSerializer


class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = (permissions.IsAuthenticated,
                          IsAdminOrPostOnly,
                          )
