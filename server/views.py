from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
import json
from rest_framework import status

from pymongo import MongoClient


class AddUserView(APIView):
	def get(self,request,*args,**kwargs):
		pass
	def post(self,request,*args,**kwargs):

		# # Takes the following JSON requests(example)
		'''

			{
				"uuid" : "qwejkfbfjdsjk",
				"fullName" : "Sindhura Dasari",
				"phoneNumber" : 9324745828 
			}

		'''

		reqData = request.data

		# Converting request data into a dictionary object
		reqDataDict = dict(reqData)

		try:
			# Initialize a mongodb client
			client = MongoClient()

			# Connect to mongodb
			client = MongoClient('mongodb+srv://samarth:covid19Help@cluster0.4qbde.mongodb.net/test')

			# Access Login db, if not created, mongodb creates it automatically
			loginDB = client['Login']

			# Make collection within db
			loggedInUsersCollection = loginDB['loggedInUsers']

			# Insert request data in db
			loginDB.loggedInUsersCollection.insert_one(reqDataDict)

		except:
			# Database error, we return 501 status code
			err = {'error':'Some thing went wrong on our end'}
			return Response(err,status = status.HTTP_500_INTERNAL_SERVER_ERROR)


		# If everything goes fine, we return 201 status code
		successContent = {'status': 'User Created'}
		return Response(successContent, status = status.HTTP_201_CREATED)


class DonorRegisterView(APIView):
	def get(self,request,*args,**kwargs):
		pass
	def post(self,request,*args,**kwargs):
		# Takes the following JSON requests(examples):

		'''

			{
			    "fullName" : "Raghav Saxena",
			    "mobileNumber" : 9803458287,
			    "bloodGroup": "AB-",
			    "city": "Mumbai",
			    "state": "Maharashtra",
			    "pincode": 400088
			} 



		 {
			"fullName" : "Sindhura Dasari",
			"mobileNumber" : 9324745828,
			"bloodGroup": "B+",
			"city": "Warangal",
			"state": "Telangana",
			"pincode": 506002

		 } 


		'''
		reqData = request.data

		reqDataDict = dict(reqData)

		state = reqDataDict['state']
		try:
			# Initialize a mongodb client
			client = MongoClient()

			# Connect to mongodb
			client = MongoClient('mongodb+srv://samarth:covid19Help@cluster0.4qbde.mongodb.net/test')

			# Access RegisterDonor db, if not created, mongodb creates it automatically
			registerDonorDB = client['RegisterDonor']

			# Insert request data into database
			registerDonorDB[state+'-Collection'].insert_one(reqDataDict)


		except:
			# Database error
			err = {'error':'Some thing went wrong on our end'}
			return Response(err,status = status.HTTP_500_INTERNAL_SERVER_ERROR)

		# If everything goes fine, we return 201 status code
		successContent = {'status': 'Donor Registered Created'}
		return Response(successContent, status = status.HTTP_201_CREATED)

class DonorGetView(APIView):

	def get(self,request,*args,**kwargs):
		pass
	def post(self,request,*args,**kwargs):

		reqData = request.data

		reqDataDict = dict(reqData)

		pin = reqDataDict['pincode']
		state = reqDataDict['state']

		try:

			client = MongoClient()

			# Connect to mongodb
			client = MongoClient('mongodb+srv://samarth:covid19Help@cluster0.4qbde.mongodb.net/test')

			query = {'pincode': pin }

			# Access RegisterDonor db,
			getDonorDB = client['RegisterDonor']


			donorsInPincode = getDonorDB[state+'-Collection'].find(query)

			res = []

			if donorsInPincode.count() != 0:
				for doc in donorsInPincode:
					doc['_id'] = str(doc['_id'])
					res.append(doc)
			else:
				strPin = str(pin)
				firstThree = strPin[0:3]

				pincodes = getDonorDB[state+'-Collection'].distinct('pincode')

				print(pincodes)

				selectedPins = []
				for pincode in pincodes:
					strPin = str(pincode)
					if firstThree == strPin[0:3]:
						selectedPins.append(pincode)
			

				newQuery = {"pincode": { "$in": selectedPins}}


				donors = getDonorDB[state+'-Collection'].find(newQuery)

			
				for doc in donors:
					doc['_id'] = str(doc['_id'])
					res.append(doc)

		except:
			# Database error
			err = {'error':'Some thing went wrong on our end'}
			return Response(err,status = status.HTTP_500_INTERNAL_SERVER_ERROR)

		#If everything goes fine, we return 200 status code
		successContent = {'status': 'Success'}
		return Response(res,status = status.HTTP_201_CREATED)


		





		
