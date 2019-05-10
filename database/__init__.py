from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


from User import User
from Device import Device
from UserDevice import UserDevice
from Session import Session
from UserSession import UserSession
from TestResults import TestResults
from UserTestResults import UserTestResults
from Features import Features


