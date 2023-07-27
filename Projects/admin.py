from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(UserInformation)
admin.site.register(QuestionDetails)
admin.site.register(AnswerDetails)