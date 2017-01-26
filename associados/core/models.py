#!/usr/bin/env python
# encoding: utf-8
from django.db import models
from .managers import CanceledManager, ActiveManager


class DefaultFields(models.Model):
    """
    Class Abstract created date (created_at), updated date (updated_at)
    and active (active)
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True, db_index=True)

    objects = ActiveManager()
    canceleds = CanceledManager()

    class Meta:
        abstract = True


class TestDefaultFields(DefaultFields):
    "just for test manager"
    pass

from django.db.models import F, Func
from django.db.models.functions import TruncDate


class DateFunc(Func):
    function = 'DATE'

def get_others_with_last_login_on_the_same_day(pk):
    # retorna um QuerySet cujo resultado é uma lista com unico elemento
    person_last_login_list = Person.objects.annotate(last_login_date=TruncDate(F('last_login'))).filter(pk=pk).values('last_login_date')

    persons = Person.objects.annotate(last_login_date=TruncDate(F('last_login'))).filter(last_login_date__in=person_last_login_list).exclude(pk=pk)

    return persons