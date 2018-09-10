class Config:
    DEBUG = True

    TESTING = True

    #追踪对象修改并发送信号，不必要可禁用
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    SQLALCHEMY_ECHO = True

    SECRET_KEY = "key_key"

    # SQLALCHEMY_DATABASE_URI = "postgresql://127.0.0.1:5432/flask"
    SQLALCHEMY_DATABASE_URI = 'postgresql://lus@localhost/del'

