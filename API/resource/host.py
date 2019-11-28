from flask import request,jsonify
from flask_restful import Resource
from Model import db,Host
from werkzeug.security import generate_password_hash
import uuid
import datetime
import jwt


class HostApi(Resource):
    def get(self,*args,**kwargs):
        Hostdata = db.session.query(Host)
        query=Hostdata.all()
        user_list=[]
        for i in query:
            temp_obj={
                'id':i.id,
                'name':i.name,
                'phone_no':i.phone_no,
                'email':i.email
            }
            user_list.append(temp_obj)

        return {"status":"success",'data': user_list},200


    def post(self,*args):
        json_data=request.get_json(force=True)
        if not json_data:
            return {'message':'Missing Body data '},400
        prehost=Host.query.filter_by(phone_no=json_data['phone_no'],email=json_data['email']).first()
        if prehost:
            return {'message':'email & phone no already exist'},400
        id=str(uuid.uuid4())

        newhost=Host(
            id=id,
            name=json_data['name'],
            email=json_data['email'],
            phone_no=json_data['phone_no']
        )
        db.session.add(newhost)
        db.session.commit()


        return  {"message":"Host added succesfully"}, 201

    


