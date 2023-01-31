from django.contrib import admin
from home import models

# Register your models here.
admin.site.register((models.Blog,models.Blogcomments))
admin.site.register(models.Contact)
admin.site.register(models.Testimonial)
admin.site.register(models.userprotection)
admin.site.register(models.reportingcrime)
admin.site.register(models.usersafety)