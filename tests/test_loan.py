import json

from tests.BaseCase import BaseCase


class LoanTest(BaseCase):       
    def test_successful_loan(self):
        user = json.dumps({
            "username":"ramakrishna",
            "password":"ramakrishna",
            "address":"8/121,p.k. ramaya street,jammalamadugu",
            "state":"andhrapradesh",
            "country":"India",
            "emailAddress":"chimmaniramakrishna25@gmail.com",
            "pan":"CWEPR7923F",
            "contactNo":9440921058,
            "DOB":"17/12/1995",
            "accountType":"savings"
        })
        payload1 = json.dumps({
            "username":"ramakrishna",
            "password":"ramakrishna"
        })
        payload2 = json.dumps({
            "username":"ramakrishna",
            "loan_type":"car_Loan",
            "loan_Amount":200000,
            "date":"17/12/1995",
            "rate_of_interest":1,
            "duration_of_loan":12
        })
        response = self.app.post('/accounts/signup', headers={"Content-Type": "application/json"}, data=user)
        response = self.app.post('/accounts/login', headers={"Content-Type": "application/json"}, data=payload1)
        response = self.app.post('/accounts/login/ramakrishna/loans', headers={"Content-Type": "application/json"}, data=payload2)        
        self.assertEqual(200, response.status_code)

    def test_unsuccessful_loan(self):
        user = json.dumps({
            "username":"ramakrishna",
            "password":"ramakrishna",
            "address":"8/121,p.k. ramaya street,jammalamadugu",
            "state":"andhrapradesh",
            "country":"India",
            "emailAddress":"chimmaniramakrishna25@gmail.com",
            "pan":"CWEPR7923F",
            "contactNo":9440921058,
            "DOB":"17/12/1995",
            "accountType":"savings"
        })
        payload1 = json.dumps({
            "username":"ramakrishna",
            "password":"ramakrishna"
        })
        payload2 = json.dumps({
            "username":"krishna",
            "loan_type":"car_Loan",
            "loan_Amount":200000,
            "date":"17/12/1995",
            "rate_of_interest":1,
            "duration_of_loan":12
        })
        response = self.app.post('/accounts/signup', headers={"Content-Type": "application/json"}, data=user)
        response = self.app.post('/accounts/login', headers={"Content-Type": "application/json"}, data=payload1)
        response = self.app.post('/accounts/login/krishna/loans', headers={"Content-Type": "application/json"}, data=payload2)        
        self.assertEqual(500, response.status_code)
    
    def test_successful_getloandetails(self):
        response = self.app.get('/accounts/login/ramakrishna/loans', headers={"Content-Type": "application/json"})        
        self.assertEqual(200, response.status_code)
    
   