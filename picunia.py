import requests, base64, urllib, urllib2, json
from requests.auth import HTTPBasicAuth


def create_account():
	email = raw_input("Enter email for account: ")
	name =  raw_input("Enter name for account: ")
	lastname =  raw_input("Enter lastname for account: ")
	passwd = raw_input("Enter passwd for account: ")

	print email, name, lastname, passwd

	msg = {}
	msg['email'] = email
	msg['name'] = name
	msg['lastname'] = lastname
	msg['password'] = passwd
	msg['reg_id'] = "t9PTZcW8C1NMQAHAHSTkc"

	url = 'http://picunia.com/api/v1.0/register_account'
	headers = {'Content-Type': 'application/json'}
	r = requests.post(url, data=json.dumps(msg), headers=headers)
	print r
	print r.json
	print r.text

def get_user_info():
	email = raw_input("Enter email for account: ")
	passwd = raw_input("Enter passwd for account: ")

	url = 'http://picunia.com/api/v1.0/account_info/%s' % email.replace('\n', '')
	headers = {'Content-Type': 'application/json'}
	r = requests.get(url, auth=HTTPBasicAuth(email,passwd), headers=headers)
	print r.text

def pay_someone():
	email = raw_input("Enter email to send bitcoint to: ")
	amount = raw_input("Enter amount to send to %s: " % email)
	msg = raw_input("Enter a message to sender: " )
	

	my_email = raw_input("Login: enter email: ")
	passwd = raw_input("Login: passwd: ")

	url = 'http://picunia.com/api/v1.0/pay_to_address'
	payload = {}
	payload['from'] = my_email
	payload['to'] = email
	payload['amount'] = amount
	payload['msg'] = msg
	#sandra.green@example.com
	headers = {'Content-Type': 'application/json'}
	r = requests.post(url, auth=HTTPBasicAuth(my_email,passwd), data=json.dumps(payload), headers=headers)
	print r
	print r.json
	print r.text

def write_blockchain_message():
	my_email = raw_input("Login: enter email: ")
	passwd = raw_input("Login: passwd: ")
	msg = raw_input("Enter your blockchain message: ")

	url = 'http://picunia.com/api/v1.0/blockchain_message'
	payload = {}
	payload['email'] = my_email
	payload['message'] = msg

	headers = {'Content-Type': 'application/json'}
	r = requests.post(url, auth=HTTPBasicAuth(my_email,passwd), data=json.dumps(payload), headers=headers)
	print r
	print r.json
	print r.text	

def main_menu():
	ans=True
	while ans:
		print ("""
		1. create account
		2. get user info
		3. pay some one
		4. write blockchain message
		5. Exit/End
		""")
		ans=raw_input("What would you like to do? ") 
		if ans=="1": 
			create_account() 
		elif ans=="2":
			get_user_info()
		elif ans=="3":
			pay_someone() 
		elif ans=="4":
			write_blockchain_message()
		elif ans=="5":
			exit(1)			
		elif ans !="":
			print("\n Not Valid Choice Try again") 

main_menu()
