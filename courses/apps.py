'''Module that enables the use of Namespacing for the courses app'''
from django.apps import AppConfig


class CoursesConfig(AppConfig):
    '''Instantiation of the namespace for the courses app'''
    name = 'courses'
