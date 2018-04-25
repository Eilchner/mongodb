from pymongo import MongoClient

client = MongoClient()

db = client.projekt
coll = db.kindle

userID = raw_input("Podaj ID uzytkownika: ")
data = coll.find({'reviewerID': userID})
revHelpful = 0
revTotal = 0

revAmmount = data.count()

if revAmmount is 0:
	print "Dany uzytkownik nie istnieje w bazie!"
	quit()

for rev in data:
	revHelpful += rev['helpful'][0]
	revTotal += rev['helpful'][1]

helpfulness = (float(revHelpful) / revTotal) * 100
print revHelpful 

print "Pomocnosc recenzji uzytkownika " + userID + " wynosi " + str(int(helpfulness)) + "%" 
