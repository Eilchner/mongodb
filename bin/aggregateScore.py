from pymongo import MongoClient

client = MongoClient()

db = client['projekt']
coll = db['kindle']

prodID = raw_input("Podaj ID ksiazki: ")
data = coll.find({'asin': prodID})
agg = 0

revAmmount = data.count()

if revAmmount is 0:
	print "Brak recenzji dla danej ksiazki!"
	quit()

for rev in data:
	agg += rev['overall']

medScore = agg / revAmmount
print 'Srednia ocen ksiazki ' + prodID + ' wynosi: ' + str(medScore)
