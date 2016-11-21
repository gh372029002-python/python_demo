#!/usr/bin/python
#!-*-coding:utf-8-*-

import imp
with open('sample_13.18_moneyfmt.py', 'rb') as fp:
    models_admin = imp.load_module(
        'moneyfmt', fp, 'sample_13.18_moneyfmt.py',
        ('.py', 'rb', imp.PY_SOURCE)
    )
# import sample_13.18_moneyfmt as  moneyfmt

cash = sample_13/.18_moneyfmt.MoneyFmt(123.456)

print cash