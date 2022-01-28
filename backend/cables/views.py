from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissions, IsAuthenticated

from .filters import (
    EquipmentFilter,
    PoleEquipmentFilter,
    PoleFilter,
    SegmentEquipmentFilter,
    SegmentFilter,
    VisitFilter,
)
from .models import Operation, Pole, Segment, Visit
from .serializers import (
    EquipmentSerializer,
    PoleSerializerEdit,
    PoleSerializerInfo,
    SegmentSerializerEdit,
    SegmentSerializerInfo,
    VisitSerializerEdit,
    VisitSerializerInfo,
)


class PoleViewSetInfo(viewsets.ModelViewSet):
    """A ViewSet to retrieve one specific Pole item or the list of Pole items, both with full data (nested data)"""

    serializer_class = PoleSerializerInfo
    permission_classes = [IsAuthenticated]
    queryset = Pole.objects.all()
    filterset_class = PoleFilter


class PoleViewSetEdit(viewsets.ModelViewSet):
    """A ViewSet to create or retrieve one specific Pole item or the list of Pole items (both with pk reference as ForeignKey only, not nested data), or update, partially update or delete a specific Pole item"""

    serializer_class = PoleSerializerEdit
    permission_classes = [DjangoModelPermissions]
    queryset = Pole.objects.all()
    filterset_class = PoleFilter


class SegmentViewSetInfo(viewsets.ModelViewSet):
    """A ViewSet to retrieve one specific Segment item or the list of Segment items, both with full data (nested data)"""

    serializer_class = SegmentSerializerInfo
    permission_classes = [IsAuthenticated]
    queryset = Segment.objects.all()
    filterset_class = SegmentFilter


class SegmentViewSetEdit(viewsets.ModelViewSet):
    """A ViewSet to create or retrieve one specific Segment item or the list of Segment items (both with pk reference as ForeignKey only, not nested data), or update, partially update or delete a specific Segment item"""

    serializer_class = SegmentSerializerEdit
    permission_classes = [DjangoModelPermissions]
    queryset = Segment.objects.all()
    filterset_class = SegmentFilter


class VisitViewSetInfo(viewsets.ModelViewSet):
    """A ViewSet to retrieve one specific Visit item or the list of Visit items, both with full data (nested data)"""

    serializer_class = VisitSerializerInfo
    # permission_classes = [IsAuthenticated]
    queryset = Visit.objects.all()
    filterset_class = VisitFilter


class VisitViewSetEdit(viewsets.ModelViewSet):
    """A ViewSet to create or retrieve one specific Visit item or the list of Visit items (both with pk reference as ForeignKey only, not nested data), or update, partially update or delete a specific Segment item"""

    serializer_class = VisitSerializerEdit
    # permission_classes = [DjangoModelPermissions]
    queryset = Visit.objects.all()
    filterset_class = VisitFilter


###################################################################################################
###################################################################################################
class EquipmentViewSet(viewsets.ModelViewSet):
    """A simple viewset to retrieve all the Visit items

    If no value given for "pole" (and/or "segment") parameter (get parameters), no filter will be applied to Poles (and/or Segment) all instances will be returned with result"""

    serializer_class = EquipmentSerializer
    permission_classes = [DjangoModelPermissions]
    queryset = Operation.objects.all()
    filterset_class = EquipmentFilter

    def get_queryset(self):
        pole = self.request.query_params.get("pole")
        segment = self.request.query_params.get("segment")
        pole_qs = self.queryset
        sgmt_qs = self.queryset
        queryset = Operation.objects.all()
        if pole is not None:
            pole_qs = queryset.filter(pole=pole)
        if segment is not None:
            sgmt_qs = queryset.filter(segment=segment)
        return pole_qs | sgmt_qs


class PoleEquipmentViewSet(viewsets.ModelViewSet):
    """A simple viewset to retrieve all the Visit items"""

    serializer_class = EquipmentSerializer
    permission_classes = [DjangoModelPermissions]
    queryset = Operation.objects.all()
    filterset_class = PoleEquipmentFilter

    def get_queryset(self):
        return self.queryset.filter(pole__isnull=False)


class SegmentEquipmentViewSet(viewsets.ModelViewSet):
    """A simple viewset to retrieve all the Visit items"""

    serializer_class = EquipmentSerializer
    permission_classes = [DjangoModelPermissions]
    queryset = Operation.objects.all()
    filterset_class = SegmentEquipmentFilter

    def get_queryset(self):
        return self.queryset.filter(segment__isnull=False)
