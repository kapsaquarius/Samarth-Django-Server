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
			Response(err,status = status.HTTP_500_INTERNAL_SERVER_ERROR)


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
			Response(err,status = status.HTTP_500_INTERNAL_SERVER_ERROR)

		# If everything goes fine, we return 201 status code
		successContent = {'status': 'Donor Registered Created'}
		return Response(successContent, status = status.HTTP_201_CREATED)


		
