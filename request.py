import requests

# URL
url = 'http://franadek.pythonanywhere.com/api'

# Change the value of experience that you want to test
PAY_1=input("PAY_1: ")
PAY_2=input("PAY_2: ")
PAY_3=input("PAY_3: ")
LIMIT_BAL=input("LIMIT_BAL: ")
BILL_AMT3=input("BILL_AMT3: ")
PAY_AMT3=input("PAY_AMT3: ")


r = requests.post(url,json={'PAY_1':int(PAY_1),
                            'PAY_2':int(PAY_2),
                            'PAY_3':int(PAY_3),
                            'LIMIT_BAL':int(LIMIT_BAL),
                            'BILL_AMT3':int(BILL_AMT3),
                            'PAY_AMT3':int(PAY_AMT3)},)

print(r.json())
