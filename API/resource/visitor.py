from Model import db,Visitor,Host
from flask_restful import Resource
from flask import request,jsonify,make_response
import uuid
import datetime 
import json
from .MailService import SendMail,send_email_at
from .SmsService import SendSms
import datetime as dt

class VisitorApi(Resource):
    
    def get(self):
        visitor = db.session.query(Visitor)
        queryall=visitor.all()
        visitorlist=[]
        for query in queryall:
            temp_obj={
                'id':query.id,
                'name':query.name,
                'phone_no':query.phone_no,
                'email':query.email,
                'checkintime':query.checkintime,
                'checkouttime':query.checkouttime
            }
            visitorlist.append(temp_obj)
        return jsonify(data=visitorlist,message="Success",status=200)

    
    def post(self):

        json_data=request.get_json(force=True)
        if not json_data:
            return {"message":"Request body missing","status":"Failure"},401
        
        else:
            x=datetime.datetime.utcnow()
            id=str(uuid.uuid4())
            checkout=json_data['checkouttime']
            newvis=Visitor(id=id,name=json_data['name'],phone_no=json_data['phone_no'],email=json_data['email'],checkintime=x)

            db.session.add(newvis)
            db.session.commit()
            json_data['id']=id
            json_data['checkintime']=str(x)
            
            # response=SendSms(message,phone_no_list)
            # sendmailtovisitor(message,json_data['email'])
            msg="""The visitor just registered in the system:\n Name-%s\n Email-%s\n phone-Number-%s \n checkin Time-%s \n checkout Time-%s""",(json_data['name'],json_data['email'],json_data['phone_no'],str(x),checkout)
            host = db.session.query(Host)
            queryall=visitor.all()
            phone_no_list=""
            hostname=[]
            hostemail=[]
            for i in queryall:
                phone_no_list+=i.phone_no+','
                hostname.append(i.name)
                hostmail.append(i.email)
            SendSms(msg,phone_no_list)
            SendMail(msg,"New visitor Added",hostmail)
            message="""Your last visit Deltails were:\n Name-%s\n Email-%s\n phone-Number-%s \n checkin Time-%s \n checkout Time-%s \nHost Name-%s \n visit Address:xyz""",(json_data['name'],json_data['email'],json_data['phone_no'],str(x),checkout,str(hostname))
            
            send_time = dt.datetime(x[0:4],x[5:7],x[8:],checkout[0:2],checkout[3:],0)
            send_email_at(send_time,json_data['email'],message)
            return {"message":"Visitor registered successfully","visitor":json_data},200        
    
    