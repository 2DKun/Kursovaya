from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.http import HttpResponse
from sqlite3 import Error
import sqlite3

def showme(req):
    try:
        conn = sqlite3.connect(r'C:\Users\kerg6\PycharmProjects\Kursov\Rursovaya\visits\db.sqlite3')
        cur = conn.cursor()
        cur.execute(f"{req}")
        try:
            resp = str(cur.fetchall())
        except:
            resp = 'Запрос успешно выполнен!'
    except (Exception, Error) as error:
        resp = str(error)
    return resp

def index(reqest, req):

    return HttpResponse(f"Результат: {showme(req)}")