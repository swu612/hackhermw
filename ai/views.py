from django.shortcuts import render
from brain import generate_ideas, generate_stack, write_boilerplate

def gen_ideas(user_input: str):
    response = generate_ideas(user_input)
    return response 

def gen_stack(user_input: str, level: str):
    response = generate_stack(user_input)
    return response

def gen_boilerplate(user_input: str, level: str, tech_stack: str):
    response = write_boilerplate(user_input)
    return response




