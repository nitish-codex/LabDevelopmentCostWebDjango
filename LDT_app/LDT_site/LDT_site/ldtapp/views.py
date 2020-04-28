from django.shortcuts import render 
from django.http import HttpResponse
from ldtapp.models import variables
from ldtapp.models import geneDiseaseList
from ldtapp.models import geneLengthList
from ldtapp.models import kitOutputCost
from ldtapp.models import hybridProbesCost
from ldtapp.forms import geneDiseaseForm
import math

# Create your views here.
def index(request):
	return render(request, 'ldtapp/cover.html')

def costAnalysis(request):
	geneDisease = geneDiseaseList.objects.all()
	args = {'geneDisease': geneDisease}
	return render(request, 'ldtapp/costCalc2.html', args)

def costEstimated(request):
	## Geting all values from the user
	finalvalues = request.GET.get('finalvalues')
	totalTime = request.GET.get('tat') 
	sp_values = finalvalues.split(':')
	print(sp_values, totalTime)

	totalFreqSmp = int(sp_values[1])
	genelist = sp_values[0]
	totNumberGenes = len(genelist.split(' '))
	print(totNumberGenes)

	print("From user: ", totalFreqSmp, genelist, totalTime)

	## geting all the variables
	var = variables.objects.all()[0]
	kits = kitOutputCost.objects.all()
	probsCost = hybridProbesCost.objects.all()

	turnAroundTime = var.tat
	batchSize = var.batchsize
	dnaExtCst = var.dnaExtractionCost
	libPrpCst = var.libPrepCost
	#hybKitCst = var.hybridKitCost
	eurToDolFact = var.eurToDollerConFact
	hybRxnCount = var.hybridizationRxnCount

	#1 Calculating the labProcessBatchSize/Total number of samples given
	actualTime = int(totalTime)-turnAroundTime
	labProcessBatchSize = totalFreqSmp*actualTime
	print("Total number of samples=> ", labProcessBatchSize) 

	#2 Calculating the panel length
	panelLength = 0
	for gene in genelist.split(' '):
		try:
			Length = geneLengthList.objects.filter(gene=gene).values('length')[0]
		except:
			Length = {'length': 2000}
		panelLength = panelLength + int(Length['length'])
	print("panelLength=>", panelLength)

	#3 Calculating the preperation cost of the complete batch
	prepCost = (libPrpCst*labProcessBatchSize) + (dnaExtCst*labProcessBatchSize)
	print("prepCost ", prepCost)

	#4 Calculating the hybridization cost
	K = math.ceil(labProcessBatchSize/batchSize)

	numProbes = panelLength/100
	probsCostEUR = 0
	for i in probsCost:
		if numProbes < i.numProbeslim:
			probsCostEUR = i.pricesInEUR
			break
		else:
			pass

	hybKitProbCst = (numProbes * probsCostEUR * eurToDolFact) * (1/96) * hybRxnCount
	hybKitCstBlocking = 16
	hybKitCst = hybKitProbCst + hybKitCstBlocking


	hybridizationCost = K * hybKitCst
	hybridizationCostPerSamples = hybridizationCost/labProcessBatchSize
	print("hybridizationCost ", hybridizationCost)
	
	#5 ideal number of sample needed for seq 
	actualNumberSamplesSeq = batchSize * K
	print("actualNumberSamplesSeq ", actualNumberSamplesSeq) 
	

	#6 total number of reads needed for sequencing
	readsPerSamples = panelLength * 3
	readsNeeded = readsPerSamples * actualNumberSamplesSeq

	#7 Finding the sequencing cost of the total number of reads calculated
	kit_cost = 0
	for i in kits:
		if readsNeeded < int(i.output):
			kit_cost = int(i.cost)
			kitType = i.kit
			break
		else:
			pass

	##?????????????? Point of doubt
	#8 if seq length is larger than the all values given in table
	if kit_cost == 0:
		kit_cost = 4400

	#9 Final cost of sequencing each sample
	print(prepCost, hybridizationCost, kit_cost, kitType)
	netCost = prepCost + hybridizationCost + kit_cost
	print("Final cost=>", netCost)

	#Rounding up all numbers
	netCostPerSample = round(netCost/labProcessBatchSize,2)
	netCost = round(netCost, 2)
	hybKitCst = round(hybKitCst, 2)
	hybKitCstPerSample = round(hybKitCst/labProcessBatchSize, 2)
	hybKitCstPerRxn = round(hybKitCst/K, 2)
	seqCostPerSample = round(kit_cost/labProcessBatchSize, 2)


	args = {'netCostPerSample': netCostPerSample, \
			'totNumberGenes': totNumberGenes, \
			'genelist': genelist, \
			'actualTime' :actualTime, \
			'totalFreqSmp': totalFreqSmp, \
			'labProcessBatchSize': labProcessBatchSize, \
			'panelLength': panelLength, \
			'dnaExtCst': dnaExtCst, \
			'libPrpCst': libPrpCst, \
			'hybKitCst': hybKitCst, \
			'kitType' : kitType, \
			'kit_cost' : kit_cost, \
			'netCost' : netCost, \
			'batchSize' : batchSize, \
			'hybKitCstPerSample' : hybKitCstPerSample, \
			'hybKitCstPerRxn' : hybKitCstPerRxn, \
			'seqCostPerSample' : seqCostPerSample, \
		   }
	return render(request, 'ldtapp/resultDisplay.html', args)