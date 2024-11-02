from django.db import models

class Team_Member(models.Model):
    Profile_Image=models.FileField(upload_to="media")
    Name=models.CharField(max_length=40)
    Role=models.CharField(max_length=40)
