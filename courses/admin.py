from django.contrib import admin
from . import models

# You can also use StackedInline or
# class TextInline(admin.StackedInline):
#     model = Text

# class CourseAdmin(admin.ModelAdmin):
#     inlines = [TextInline,]
    

admin.site.register(models.Course)
admin.site.register(models.Text)
admin.site.register(models.Quiz)
admin.site.register(models.Question)
admin.site.register(models.Answer)