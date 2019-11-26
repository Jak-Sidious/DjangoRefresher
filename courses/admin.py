'''Class that deals with the admin view inside the courses app'''
from django.contrib import admin
from . import models

# You can also use StackedInline or
class TextInline(admin.StackedInline):
    model = models.Text

class QuizInline(admin.StackedInline):
    model = models.Quiz

class CourseAdmin(admin.ModelAdmin):
    inlines = [TextInline]

    serach_fields = ['title', 'description'] ##search filters

    list_filter = ['created_at']

# class QuizAdmin(admin.ModelAdmin):
#     inlines = [QuizInline]
#     # fields = ['course', 'title', 'description', 'order', 'total_questions']

    


admin.site.register(models.Course, CourseAdmin)
admin.site.register(models.Text)
admin.site.register(models.Quiz)
admin.site.register(models.MultipleChoiceQuestion)
admin.site.register(models.TrueFalseQuestion)
admin.site.register(models.Answer)

admin.site.site_header = "Learning Site administration"
