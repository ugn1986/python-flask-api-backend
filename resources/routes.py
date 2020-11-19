from .accounts import SignupApi, LoginApi,LoanApi

def initialize_routes(api):
    
    api.add_resource(SignupApi, '/accounts/signup')
    api.add_resource(LoginApi, '/accounts/login','/accounts/login/<username>')
    api.add_resource(LoanApi, '/accounts/login/<username>/loans')    
