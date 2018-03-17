from django.contrib import admin
from first_app.models import AccessRecord, webpage, Topic, TestUsers
# Register your models here.

admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(webpage)
admin.site.register(TestUsers)

 