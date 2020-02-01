from firebase import firebase


fb = firebase.FirebaseApplication("https://safeskate-499c0.firebaseio.com/", None)

data = {
	'Name' : 'Tommy'
}


result = fb.post('/safeskate-499c0/test', data)
print(result)