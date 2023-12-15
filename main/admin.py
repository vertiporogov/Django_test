from django.contrib import admin

from main.models import Student


# admin.site.register(Student)

@admin.register(Student)
class StudetAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'is_activ',)
    list_filter = ('is_activ', )
    search_fields = ('first_name', 'last_name', )
