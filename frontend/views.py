from django.shortcuts import render, redirect
from .models import *
from rest_framework import viewsets
from .serializers import *
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
import json
import csv

# Create your views here.
def readRAMInfo():  
    #type,brand,ddr_gen,channel,capacity,clock_rate,remark,price,original_info
    ram = []
    product = []
    file = open("frontend/ram_info.csv", "r", encoding="utf-8")
    data = list(csv.reader(file, delimiter=","))
    file.close()
    try:
        maxid = Product.objects.latest('product_id').product_id
    except:
        maxid = 0
    idx = 1
    for i in range(1, len(data)):
        isExist = RAM.objects.filter(ram_type = data[i][0], ddr_gen = data[i][2], channel = data[i][3], capacity = data[i][4], clock_rate = data[i][5], remark = data[i][6]).count()
        if isExist == 0:
            ram = RAM(product_id = idx+maxid, ram_type = data[i][0], ddr_gen = data[i][2], channel = data[i][3], capacity = data[i][4], clock_rate = data[i][5], remark = data[i][6])
            product = Product(product_id = idx+maxid, brand = data[i][1], price = data[i][7], original_info = data[i][8])
            ram.save()
            product.save()
            idx += 1

def readHDDInfo():  
    #type,brand,ddr_gen,channel,capacity,clock_rate,remark,price,original_info
    hdd = []
    product = []
    file = open("frontend/hdd_info.csv", "r", encoding="utf-8")
    data = list(csv.reader(file, delimiter=","))
    file.close()
    try:
        maxid = Product.objects.latest('product_id').product_id
    except:
        maxid = 0
    idx = 1
    for i in range(1, len(data)):
        isExist = HDD.objects.filter(hdd_type = data[i][0], series = data[i][2], capacity = data[i][3], memory = data[i][4], model = data[i][5], RPM = data[i][6], warranty = data[i][7]).count()
        if isExist == 0:
            hdd = HDD(product_id = idx+maxid, hdd_type = data[i][0], series = data[i][2], capacity = data[i][3], memory = data[i][4], model = data[i][5], RPM = data[i][6], warranty = data[i][7])
            product = Product(product_id = idx+maxid, brand = data[i][1], price = data[i][8], original_info = data[i][9])
            hdd.save()
            product.save()
            idx+=1

def readSSDInfo():  
    #type,brand,ddr_gen,channel,capacity,clock_rate,remark,price,original_info
    ssd = []
    product = []
    file = open("frontend/hdd_info.csv", "r", encoding="utf-8")
    data = list(csv.reader(file, delimiter=","))
    file.close()
    try:
        maxid = Product.objects.latest('product_id').product_id
    except:
        maxid = 0
    idx=1
    for i in range(1, len(data)):
        isExist = SSD.objects.filter(ssd_type = data[i][0], capacity = data[i][2], read_speed = data[i][3], write_speed = data[i][4], warranty = data[i][5]).count()
        if isExist == 0:
            ssd = SSD(product_id = idx+maxid, ssd_type = data[i][0], capacity = data[i][2], read_speed = data[i][3], write_speed = data[i][4], warranty = data[i][5])
            product = Product(product_id = idx+maxid, brand = data[i][1], price = data[i][6], original_info = data[i][7])
            ssd.save()
            product.save()
            idx += 1

def front(request, *args, **kwargs):
    context = {
        }

    return render(request, "index.html", context)

def RAMPages(request, *args, **kwargs):
    context = {
        }

    return render(request, "RAMPages.html", context)
def HDDPages(request, *args, **kwargs):
    context = {
        }

    return render(request, "HDDPages.html", context)
def SSDPages(request, *args, **kwargs):
    context = {
        }

    return render(request, "SSDPages.html", context)

@api_view(('GET','POST'))
def RAMdata (request, *args, **kwargs):
    readRAMInfo()
    if request.method == 'GET':
        queryset=RAM.objects.all()
        data = []
        for i in queryset:
            p = Product.objects.get(product_id = i.product_id)
            ram_serializer = RAMSerializer(i)
            product_serializer = ProductSerializer(p)
            data.append(ram_serializer.data | product_serializer.data)
        return Response(data)
    
@api_view(('GET','POST'))
def HDDdata (request, *args, **kwargs):
    readHDDInfo()
    if request.method == 'GET':
        queryset=HDD.objects.all()
        data = []
        for i in queryset:
            p = Product.objects.get(product_id = i.product_id)
            hdd_serializer = HDDSerializer(i)
            product_serializer = ProductSerializer(p)
            data.append(hdd_serializer.data | product_serializer.data)
        return Response(data)
    
@api_view(('GET','POST'))
def SSDdata (request, *args, **kwargs):
    readSSDInfo()
    if request.method == 'GET':
        queryset=SSD.objects.all()
        data = []
        for i in queryset:
            p = Product.objects.get(product_id = i.product_id)
            ssd_serializer = SSDSerializer(i)
            product_serializer = ProductSerializer(p)
            data.append(ssd_serializer.data | product_serializer.data)
        return Response(data)

def login(request):
    pass

def signup(request):
    pass
