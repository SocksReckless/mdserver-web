# coding:utf-8

# ---------------------------------------------------------------------------------
# MW-Linux面板
# ---------------------------------------------------------------------------------
# copyright (c) 2018-∞(https://github.com/midoks/mdserver-web) All rights reserved.
# ---------------------------------------------------------------------------------
# Author: midoks <midoks@163.com>
# ---------------------------------------------------------------------------------

from functools import wraps

from admin import model
from admin import session
from admin.common import isLogined

def panel_login_required(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        if not isLogined():
            return {'status':False, 'msg':'未登录/登录过期'}

        return func(*args, **kwargs)
    return wrapper