from django.contrib import admin
from .models import User, Paper, Query, Section, Answers

# Register your models here.
admin.site.register(User)
admin.site.register(Paper)
admin.site.register(Query)
admin.site.register(Section)
admin.site.register(Answers)