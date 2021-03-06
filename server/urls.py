from django.conf.urls import url,include
from django.urls import path
from django.conf import settings
from server.views import AddUserView,DonorRegisterView,DonorGetView,AddResourceView

urlpatterns = [
	path('addUser/', AddUserView.as_view(),name='addUser'),
	path('registerDonor/', DonorRegisterView.as_view(),name='registerDonor'),
	path('getDonorsByPincodeState/', DonorGetView.as_view(),name='getDonorsByPincodeState'),
	path('addResources/', AddResourceView.as_view(),name='addResources'),
]