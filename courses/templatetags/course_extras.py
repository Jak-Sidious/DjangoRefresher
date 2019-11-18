from django import template
from courses.models import Course

register = template.Library()

@register.simple_tag #Option 2 in the form of a decorator
def newest_course():
    '''Gets the most recent course that was added to the Library.'''
    return Course.objects.latest('created_at')

@register.inclusion_tag('courses/course_nav.html')
def nav_courses_list():
    ''' Returns dict of courses to display as navigation pane.'''
    courses = Course.objects.all()
    return {'courses': courses}

# Custom filters begin here
@register.filter('time_estimate')
def time_estimate(word_count):
    '''Estimates numbe of minutes it will take to complete a step based on the 
    passed in wordcount.'''
    minutes = round(word_count/20)
    return minutes

#register.inclusion_tag('courses/course_nav.html')(nav_courses_list) Option 1 for template tag that renders a new template

# register.simple_tag('newest_course') #Option 1