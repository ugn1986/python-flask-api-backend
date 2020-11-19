from flask import Response, request,jsonify
from database.models import User,Loan
from flask_restful import Resource
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist,ValidationError,NotRegistered
from resources.errors import SchemaValidationError,LoanTypeAlreadyExistsError,UserNameAlreadyExistsError, UnauthorizedError,InternalServerError,UserDoesNotExist

# For user Registration
class SignupApi(Resource):
    def post(self):
        try:
            body = request.get_json()
            user =  User(**body)
            user.save()          
            return 'User Registered sucessfully', 200         
        except FieldDoesNotExist:
            raise SchemaValidationError
        except ValidationError:
            raise SchemaValidationError        
        except NotUniqueError:
            raise UserNameAlreadyExistsError
        except Exception as e:
            raise InternalServerError

# for User Login
class LoginApi(Resource):
    def post(self):
        try:
            body = request.get_json()
            user = User.objects.get(username=body.get('username'),password=body.get('password'))
        #   If both username and password matches user return 1 and below condition will be true
            if user:
                    return 'User Login Sucessfully', 200
            else:
                raise UnauthorizedError
        except (UnauthorizedError, DoesNotExist):
            raise UnauthorizedError
        except Exception as e:
            raise InternalServerError
        
    def put(self,username):
        body = request.get_json()
        User.objects.get(username=username).update(**body)
        return "User Updated successfully", 201
    
    def get(self,username):
        user=User.objects.get(username=username).to_json()
        return Response(user, mimetype="application/json", status=200)

# For getting applying loan
class LoanApi(Resource):
    def post(self,username):
        try:
            body = request.get_json()
            user = User.objects.get(username=body.get('username'))
            loan =  Loan(**body)
            loan.save()
            return 'loan updated sucessfully', 200
            if not user:
                raise UserDoesNotExist
        except (NotRegistered):
            raise UserDoesNotExist
        except NotUniqueError:
            raise LoanTypeAlreadyExistsError
        except Exception as e:
            raise InternalServerError
    
    def get(self,username): 
            loan=Loan.objects(username=username).to_json()   
            # print(loan)
            return Response(loan, mimetype="application/json", status=200)