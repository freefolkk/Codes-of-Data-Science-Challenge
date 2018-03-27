import numpy as np 
import csv

def fetch_ratings():
	#fetching the gender dataset
	#add your own path
	filepath = open("C://Users/Downloads/libimseti/gender.dat")
	csvReader = csv.reader(filepath)

	genderList = []

	for row in csvReader:
		user = row[0]
		sex = row[1]
		genderList.append([user,sex])


	#fetching the ratings dataset
	filepath = open("C://Users/Downloads/libimseti/ratings.dat")
	csvReader = csv.reader(filepath)


	ratingsList = []
	user_id = []
	match_id = []
	rating = []

	for row in csvReader:
		user_id.append(row[0])
		match_id.append(row[1]) 
		rating.append(row[2])

	#formatting the data as required by the lightfm library model class
	ratingsList = coo_matrix((rating,(user_id,match_id)))

	dictionary = {
		'ratings' : ratingsList,
		'gender' : genderList
	}	

	return dictionary	

