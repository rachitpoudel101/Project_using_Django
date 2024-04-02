from django.shortcuts import render
from django.http import JsonResponse

def index(request):
    return render(request, 'calculator/index.html')

def add(request):
    if request.method == 'GET':
        num1 = int(request.GET.get('num1'))
        num2 = int(request.GET.get('num2'))
        result = num1 + num2
        return JsonResponse({'result': result})

def subtract(request):
    if request.method == 'GET':
        num1 = int(request.GET.get('num1'))
        num2 = int(request.GET.get('num2'))
        result = num1 - num2
        return JsonResponse({'result': result})

def multiply(request):
    if request.method == 'GET':
        num1 = int(request.GET.get('num1'))
        num2 = int(request.GET.get('num2'))
        result = num1 * num2
        return JsonResponse({'result': result})

def divide(request):
    if request.method == 'GET':
        num1 = int(request.GET.get('num1'))
        num2 = int(request.GET.get('num2'))
        if num2 == 0:
            return JsonResponse({'error': 'Cannot divide by zero'})
        else:
            result = num1 / num2
            return JsonResponse({'result': result})
