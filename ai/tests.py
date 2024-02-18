import json
from django.test import TestCase
from brain import generate_stack, write_boilerplate

tech_stack_test = generate_stack("I wanna build a food app", "Beginner")
# print(str(json.loads(tech_stack_test)['response']))

boilerplate_test = write_boilerplate("I want to make a dinosaur simulation app", "Beginner", str(json.loads(tech_stack_test)['response']))
print(str(json.loads(boilerplate_test)['response']))
