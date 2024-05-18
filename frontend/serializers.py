from rest_framework import serializers
from .models import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('price', 'brand')


class RAMSerializer(serializers.ModelSerializer):
    class Meta:
        model = RAM
        fields = ('ram_type', 'ddr_gen', 'channel', 'capacity', 'clock_rate', 'remark')

class HDDSerializer(serializers.ModelSerializer):
    class Meta:
        model = HDD
        fields = ('hdd_type','series', 'capacity', 'memory', 'model', 'RPM', 'warranty')

class SSDSerializer(serializers.ModelSerializer):
    class Meta:
        model = SSD
        fields = ('ssd_type', 'read_speed', 'write_speed', 'capacity', 'warranty')
        