from django.contrib import admin

from main.models import Student, Subject


# admin.site.register(Student)

@admin.register(Student)
class StudetAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'is_activ',)
    list_filter = ('is_activ', )
    search_fields = ('first_name', 'last_name', )


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'student',)
    list_filter = ('student',)
