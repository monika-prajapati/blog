import os

class Config:
    SECRET_KEY='0f622755b7cb1481e76c31e396436a4c'
    SQLALCHEMY_DATABASE_URI='sqlite:///site.db'
    MAIL_SERVER='smpt.googlemail.com'
    MAIL_PORT=587
    MAIL_USE_TLS=True
    MAIL_USERNAME=os.environ.get('EMAIL_USER')
    MAIL_PASSWORD=os.environ.get('EMAIL_PASS')
    