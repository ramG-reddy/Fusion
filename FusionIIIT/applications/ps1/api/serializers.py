from applications.filetracking.models import Tracking
from applications.globals.models import ExtraInfo, HoldsDesignation
from applications.ps1.models import (
    File,
    IndentFile,
    StockEntry,
    StockItem,
    StockTransfer,
)
from rest_framework import serializers  # type:ignore


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = "__all__"


class IndentFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndentFile
        fields = "__all__"


class ExtraInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtraInfo
        fields = "__all__"


class HoldsDesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model = HoldsDesignation
        fields = "__all__"


class TrackingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tracking
        fields = "__all__"


class StockEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = StockEntry
        fields = "__all__"


class StockItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockItem
        fields = "__all__"


class StockTransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockTransfer
        fields = "__all__"
