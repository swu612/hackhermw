from django.shortcuts import render
from .import brain
import requests

def gen_ideas(request):
    user_input = requests.GET.get('input')
    response = brain.generate_ideas(user_input)
    return response 

def gen_stack(request):
    user_input = requests.GET.get('input')
    level = requests.GET.get('level')
    response = brain.generate_stack(user_input, level)
    return response

def gen_boilerplate(request):
    user_input = requests.GET.get('input')
    level = requests.GET.get('level')
    tech_stack = requests.GET.get('tech_stack')
    response = brain.write_boilerplate(user_input,level, tech_stack)
    return response




