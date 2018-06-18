# -*- coding: utf-8 -*-
from . import helpers
import pandas as pd


class Query(object):
    _select = ''
    _where = []
    _df = None

    def __init__(self, df):
        self._df = df

    def select(self, *colums):
        c = '", "'.join(colums)
        q = '.loc[:, ["{}"]]'.format(c)
        self._select = q
        return self

    def where(self, columm, operator, condition):
        if type(condition) == str:
            q = '.loc[df["{}"] {} "{}"]'.format(columm, operator, condition)
        else:
            q = '.loc[df["{}"] {} {}]'.format(columm, operator, condition)
        self._where = q
        return self

    def first(self):
        p = '{}.head()'.format(self._build())
        return eval(p)

    def head(self):
        p = '{}.head()'.format(self._build())
        return eval(p)

    def _build(self):
        q = 'self._df'
        # where
        # q += self._where
        # select
        q += self._select
        return q


a = pd.read_csv("jirei.csv")
b = pd.read_csv("location.csv")
df = pd.merge(a, b, on="pkey", how="inner")  # how: {inner, outer, left, right}

a = Query(df).select("pkey", "price_y").first()
print(a)
