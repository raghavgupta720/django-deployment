from django.db import models
from django import forms


class Person(models.Model):

    name = models.CharField(max_length=60)
    question_1 = models.CharField( max_length=60,default='NA')
    question_2 = models.CharField( max_length=60,default='NA')
    question_3 = models.CharField( max_length=60,default='NA')
    question_4 = models.CharField( max_length=60,default='NA')
    question_5 = models.CharField( max_length=60,default='NA')
    question_6 = models.CharField( max_length=60,default='NA')
    question_7 = models.CharField( max_length=60,default='NA')
    question_8 = models.CharField( max_length=60,default='NA')
    question_9 = models.CharField( max_length=60,default='NA')
    question_10 = models.CharField( max_length=60,default='NA')
    question_11 = models.CharField( max_length=60,default='NA')
    question_12 = models.CharField( max_length=60,default='NA')
    question_13 = models.CharField( max_length=60,default='NA')
    question_14 = models.CharField( max_length=60,default='NA')
    question_15 = models.CharField( max_length=60,default='NA')
    question_16 = models.CharField( max_length=60,default='NA')
    question_17 = models.CharField( max_length=60,default='NA')
    question_18 = models.CharField( max_length=60,default='NA')
    question_19 = models.CharField( max_length=60,default='NA')
    question_20 = models.CharField( max_length=60,default='NA')
    question_21 = models.CharField( max_length=60,default='NA')
    question_22 = models.CharField( max_length=60,default='NA')
    question_23 = models.CharField( max_length=60,default='NA')
    question_24 = models.CharField( max_length=60,default='NA')
    question_25 = models.CharField( max_length=60,default='NA')
    question_26 = models.CharField( max_length=60,default='NA')
    question_27 = models.CharField( max_length=60,default='NA')
    question_28 = models.CharField( max_length=60,default='NA')
    question_29 = models.CharField( max_length=60,default='NA')
    question_30 = models.CharField( max_length=60,default='NA')
    question_31 = models.CharField( max_length=60,default='NA')
    class Meta:
        db_table="Person"
