from django.http import HttpResponse

def suma(request, num1, num2):
    result = num1 + num2
    return HttpResponse(f'{num1} + {num2} = {result}')

def resta(request, num1, num2):
    result = num1 - num2
    return HttpResponse(f'{num1} - {num2} = {result}')

def multiplicacion(request, num1, num2):
    result = num1 * num2
    return HttpResponse(f'{num1} * {num2} = {result}')

def divition(request, num1, num2):
    result = num1 / num2
    return HttpResponse(f'{num1} / {num2} = {result}')

def potencia(request, num1, num2):
    result = num1 ** num2
    return HttpResponse(f'{num1} ** {num2} = {result}')
