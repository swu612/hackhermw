from django.urls import path
from .views import gen_boilerplate, gen_ideas, gen_stack, clear_memory

urlpatterns = [
    path('gen_ideas/', gen_ideas, name='gen_ideas'),
    path('gen_stack/', gen_stack, name='gen_stack'),
    path('gen_boilerplate/', gen_boilerplate, name='gen_boilerplate'),
    path('clear_memory/', clear_memory, name='clear_memory')
]