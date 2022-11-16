from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.http import HttpResponse
import sqlite3

def showme(req):
    conn = sqlite3.connect(r'E:\Kursov\Rursovaya\visits\db.sqlite3')
    cur = conn.cursor()
    cur.execute(f"{req}")
    resp = cur.fetchall()
    return resp

def index(reqest, req):

    return HttpResponse(f"Результат: {showme(req)}")