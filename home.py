#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pywebio import start_server
from pywebio.output import put_link, put_buttons
from pywebio.session import go_app
from callgroup import Callgroup


def index():
    put_buttons(["轮选组脚本生成器"], [lambda: go_app("callgroup")])


def callgroup():
    cg = Callgroup()


start_server([index, callgroup], port=7086)
