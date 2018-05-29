from flask import render_template
from . import main

# 使用errorhandler修饰器只有蓝本中的错误会触发，这里用app_errorhandler可以处理全局错误
@main.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@main.app_errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
