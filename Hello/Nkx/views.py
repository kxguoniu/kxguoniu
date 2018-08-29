# -*- encoding:utf-8 -*-
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
# Create your views here.

import openpyxl

def upload(request):
    if request.method == 'POST':
        obj = request.FILES.get('fafafa')
        import os
        wb = openpyxl.load_workbook(obj)
        sheet = wb.active
        for row in sheet.rows:
            print row
        print(obj.name)
        filepath = obj.name
        f = open(filepath, 'wb')
        for chunk in obj.chunks():
            f.write(chunk)
        f.close()
        return  HttpResponse('OK')
    return render(request, 'index.html')