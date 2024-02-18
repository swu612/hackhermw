from django.shortcuts import render
from django.http import JsonResponse
from .import brain

def gen_ideas(request):
    user_input = request.GET.get('input')
    response =  brain.generate_ideas(user_input)
    data = {"response": response}
    return JsonResponse(data)

def gen_stack(request):
    user_input = request.GET.get('input')
    level = request.GET.get('level')
    response = brain.generate_stack(user_input, level)
    data = {"response": response, "level": level}
    return JsonResponse(data)

def gen_boilerplate(request):
    user_input = request.GET.get('input')
    level = request.GET.get('level')
    tech_stack = request.GET.get('tech_stack')
    response = brain.write_boilerplate(user_input,level, tech_stack)
    data = {"response": response, "level": level, "tech_stack": tech_stack}
    return JsonResponse(data)




