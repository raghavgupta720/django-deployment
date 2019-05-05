from django.apps import AppConfig
from apps.myapp.models import MyModel
django.messages import *

class BasicAppConfig(AppConfig):
    name = 'basic_app'
