from django.conf.urls import url,include
from django.urls import path
from django.conf import settings
from server.views import AddUserView,DonorRegisterView

urlpatterns = [
	path('addUser/', AddUserView.as_view(),name='addUser'),
	path('registerDonor/', DonorRegisterView.as_view(),name='registerDonor'),
]