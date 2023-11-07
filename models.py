from django.db import models

class KeyValue(models.Model):
    key = models.CharField(max_length=100)
    value = models.TextField()

    def __str__(self):
        return self.key

    class Meta:
        db_name = 'key_value_table'


# python manage.py makemigrations keyvalue
# python manage.py migrate
