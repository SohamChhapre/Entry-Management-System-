from flask import Blueprint
from  flask_restful import Api

from resources.visitor import VisitorApi
from resources.host import HostApi
api_bp=Blueprint('api',__name__)
api=Api(api_bp)



api.add_resource(HostApi,'/host')

api.add_resource(VisitorApi,'/visitor')
