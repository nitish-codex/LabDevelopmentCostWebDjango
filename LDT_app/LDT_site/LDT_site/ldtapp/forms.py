from django import forms
from ldtapp.models import geneDiseaseList

class geneDiseaseForm(object):
	geneDisease = forms.CharField()
	length = forms.IntegerField()

	class Meta:
		model = geneDiseaseList
		fields = {'geneDisease', 'length',}