'''Class that deals with the admin view inside the courses app'''
from django.contrib import admin
from . import models

# You can also use StackedInline or
# class TextInline(admin.StackedInline):
#     model = Text

# class CourseAdmin(admin.ModelAdmin):
#     inlines = [TextInline,]

class QuizAdmin(admin.ModelAdmin):
    fields = ['course', 'title', 'description', 'order', 'total_questions']


admin.site.register(models.Course)
admin.site.register(models.Text)
admin.site.register(models.Quiz, QuizAdmin)
admin.site.register(models.MultipleChoiceQuestion)
admin.site.register(models.TrueFalseQuestion)
admin.site.register(models.Answer)

admin.site.site_header = "Learning Site administration"
