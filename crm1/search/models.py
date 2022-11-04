from django.db import models


class RegModel(models.Model):

    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    Confirm_password = models.CharField(max_length=50)
    email = models.EmailField()
    phonenumber = models.IntegerField()

    status = ((0, 'Inactive'), (1, 'Active'))
    userstatus = models.SmallIntegerField(choices=status)

    def __str__(self):
        return self.username


class logModel(models.Model):

    logId = models.IntegerField()
    userID = models.IntegerField()
    Ip = models.IntegerField()
    date = models.IntegerField()
    time = models.TimeField()
    session = models.IntegerField()
    Logout = models.TimeField()

    def __str__(self):
        return self.logId
