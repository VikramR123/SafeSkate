from firebase import firebase

fb = firebase.FirebaseApplication("https://safeskate-499c0.firebaseio.com/", None)

res = fb.get('/safeskate-499c0/test', '')

print(res)