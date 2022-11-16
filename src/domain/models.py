# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Catalog(models.Model):

    class Meta:
        managed = False
        db_table = 'catalog'


class Credit(models.Model):

    class Meta:
        managed = False
        db_table = 'credit'


class Debit(models.Model):

    class Meta:
        managed = False
        db_table = 'debit'


class Game(models.Model):

    class Meta:
        managed = False
        db_table = 'game'


class Log(models.Model):

    class Meta:
        managed = False
        db_table = 'log'


class Session(models.Model):

    class Meta:
        managed = False
        db_table = 'session'


class User(models.Model):

    class Meta:
        managed = False
        db_table = 'user'
