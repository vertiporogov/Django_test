from django.core.management import BaseCommand

from main.models import Student


class Command(BaseCommand):

    def handle(self, *args, **options):
        student_list = [
            {'last_name': 'ivanov', 'first_name': 'ivan'},
            {'last_name': 'dfdggs', 'first_name': 'ivaytn'},
            {'last_name': 'ivanopiuoutv', 'first_name': 'ivtyiuan'},
            {'last_name': 'ivatititinov', 'first_name': 'ivaytiutin'},
        ]

        # for student_item in student_list:
        #     Student.objects.create(**student_item)

        student_for_creats = []
        for student_item in student_list:
            student_for_creats.append(Student(**student_item))

        Student.objects.bulk_create(student_for_creats)
