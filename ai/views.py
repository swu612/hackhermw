from django.shortcuts import render
from.import brain

def gen_ideas(user_input: str):
    response = brain.generate_ideas(user_input)
    return response 

def gen_stack(user_input: str, level: str):
    response = brain.generate_stack(user_input)
    return response

def gen_boilerplate(user_input: str, level: str, tech_stack: str):
    response = brain.write_boilerplate(user_input)
    return response




