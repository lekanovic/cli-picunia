import requests, base64, urllib, urllib2, json
from requests.auth import HTTPBasicAuth
from random import randint
import time
import sys

#base_url = 'http://localhost:5000'
base_url = 'http://picunia.com'

users = []
users.append({'email': 'egon@teleworm.us', 'passwd' : 'pass'})
users.append({'email': 'erik@teleworm.us', 'passwd' : 'pass'})
users.append({'email': 'penis@teleworm.us', 'passwd' : 'pass'})
users.append({'email': 'Magnus@teleworm.us', 'passwd' : 'pass'})
users.append({'email': 'popjull@teleworm.us', 'passwd' : 'pass'})
users.append({'email': 'lekanovic@gmail.com', 'passwd' : 'pass'})

print users[1]
def create_account(interactive=True):
	if interactive:
		email = raw_input("Enter email for account: ")
		name =  raw_input("Enter name for account: ")
		lastname =  raw_input("Enter lastname for account: ")
		passwd = raw_input("Enter passwd for account: ")
	else:
		pass

	print email, name, lastname, passwd

	msg = {}
	msg['email'] = email
	msg['name'] = name
	msg['lastname'] = lastname
	msg['password'] = passwd
	msg['reg_id'] = "t9PTZcW8C1NMQAHAHSTkc"

	url = base_url + '/api/v1.0/register_account'
	headers = {'Content-Type': 'application/json'}
	r = requests.post(url, data=json.dumps(msg), headers=headers)
	print r
	print r.text
	print r.json
	print r.headers

def get_user_info(interactive=True):
	if interactive:
		email = raw_input("Enter email for account: ")
		passwd = raw_input("Enter passwd for account: ")
	else:
		u = users[randint(0,4)]
		email = u['email']
		passwd = u['passwd']

	url = base_url + '/api/v1.0/account_info/%s' % email.replace('\n', '')
	headers = {'Content-Type': 'application/json'}
	r = requests.get(url, auth=HTTPBasicAuth(email,passwd), headers=headers)
	print r
	print r.text
	print r.json
	print r.headers
	print r.headers['location']

def pay_someone(interactive=True):
	if interactive:
		email = raw_input("Enter email to send bitcoint to: ")
		amount = raw_input("Enter amount to send to %s: " % email)
		msg = raw_input("Enter a message to sender: " )
		my_email = raw_input("Login: enter email: ")
		passwd = raw_input("Login: passwd: ")
	else:
		u = users[randint(0,4)]
		email = u['email']
		amount = randint(1,4)*10000
		msg = "Test message"
		u2 = users[randint(0,4)]
		my_email = u2['email']
		passwd = u['passwd']



	url = base_url + '/api/v1.0/pay_to_address'
	payload = {}
	payload['from'] = my_email
	payload['to'] = email
	payload['amount'] = amount
	payload['msg'] = msg
	#sandra.green@example.com
	headers = {'Content-Type': 'application/json'}
	r = requests.post(url,
				auth=HTTPBasicAuth(my_email,passwd),
				data=json.dumps(payload),
				headers=headers)
	print r
	print r.text
	print r.json
	print r.headers
	print r.headers['location']

def write_blockchain_message(interactive=True):
	if interactive:
		my_email = raw_input("Login: enter email: ")
		passwd = raw_input("Login: passwd: ")
		msg = raw_input("Enter your blockchain message: ")
	else:
		u = users[randint(0,4)]
		my_email = u['email']
		passwd = u['passwd']
		msg = "Test message"

	url = base_url + '/api/v1.0/blockchain_message'
	payload = {}
	payload['email'] = my_email
	payload['message'] = msg

	headers = {'Content-Type': 'application/json'}
	r = requests.post(url,
				auth=HTTPBasicAuth(my_email,passwd),
				data=json.dumps(payload),
				headers=headers)
	print r
	print r.text
	print r.json
	print r.headers
	print r.headers['location']	

def request_payment(interactive=True):
	if interactive:
		my_email = raw_input("Login: enter email: ")
		passwd = raw_input("Login: passwd: ")
		request_from = raw_input("email from you wish to request from: ")
		amount = raw_input("amount to request: ")
		msg = raw_input("message to %s: " % request_from)
	else:
		u = users[randint(0,4)]
		u2 = users[randint(0,4)]
		my_email = u['email']
		passwd = u['passwd']
		request_from = u2['email']
		amount = randint(1,4)*10000
		msg = "Test message"

	url = base_url + '/api/v1.0/request_payment'
	payload = {}
	payload['requester'] = my_email
	payload['request_from'] = request_from
	payload['amount'] = amount
	payload['message'] = msg


	headers = {'Content-Type': 'application/json'}
	r = requests.post(url,
				auth=HTTPBasicAuth(my_email,passwd),
				data=json.dumps(payload),
				headers=headers)
	print r
	print r.text
	print r.json
	print r.headers
	print r.headers['location']

interactive=False

def main_menu():
	global interactive

	if len(sys.argv) == 2:
		if sys.argv[1] == '-i':
			interactive=True
		else:
			print "only argument '-i' supported"
			exit(1)
	ans=True
	while ans:
		print ("""
		1. create account
		2. get user info
		3. pay some one
		4. write blockchain message
		5. request payment
		6. Exit/End
		""")
		if interactive:
			ans=raw_input("What would you like to do? ")
		else:
			ans=str(randint(2,5))
			time.sleep(10)
		if ans=="1": 
			create_account()
		elif ans=="2":
			get_user_info(interactive=interactive)
		elif ans=="3":
			pay_someone(interactive=interactive)
		elif ans=="4":
			write_blockchain_message(interactive=interactive)
		elif ans=="5":
			request_payment(interactive=interactive)
		elif ans=="6":
			exit(1)			
		elif ans !="":
			print("\n Not Valid Choice Try again") 

main_menu()
