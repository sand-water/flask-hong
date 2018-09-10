from flask import Flask

from App.apis import init_api
from App.ext import init_ext
from App.settings import Config
from App.models import Users

def create_app():
    app = Flask(__name__)

    # 工程初始化
    app.config.from_object(Config)
    # 第三方插件初始化
    init_ext(app=app)

    # 路由初始化
    init_api(app)

    return app
