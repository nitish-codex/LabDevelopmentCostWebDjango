from django.db import models

# Create your models here.
class variables(models.Model):
	tat = models.IntegerField(default=3)
	batchsize = models.IntegerField(default=8)
	dnaExtractionCost = models.FloatField(default=100)
	libPrepCost = models.FloatField(default=300)
	# hybridKitCost = models.FloatField(default=200)
	eurToDollerConFact = models.FloatField(default=100)
	hybridizationRxnCount = models.IntegerField(default=2)

	class Meta:
		verbose_name_plural = "Basic Variables"

class geneLengthList(models.Model):
	# geneID = models.CharField(max_length=30, default='GL-0000XX')
	gene = models.CharField(max_length=100, default='SOME GENE')
	length = models.IntegerField(default=100)

	def __self__(self):
		return self.gene

	class Meta:
		verbose_name_plural = "Gene and length"

class geneDiseaseList(models.Model):
	geneID = models.CharField(max_length=30, default='GL-0000XX')
	disease = models.CharField(max_length=200, default='SOME STRING')
	genes = models.CharField(max_length=50000, default='SOMEGENES')

	def __self__(self):
		return self.disease

	class Meta:
		verbose_name_plural = "GeneID and Disease"

class kitOutputCost(models.Model):
	kit = models.CharField(max_length=30)
	output = models.CharField(max_length=20)
	cost = models.CharField(max_length=20)

	def __self__(self):
		return self.kit

	class Meta:
		verbose_name_plural = "Kit type, capacity & cost"

class hybridProbesCost(models.Model):
	numProbeslim = models.IntegerField(default=50)
	pricesInEUR = models.FloatField(default=300)

	def __self__(self):
		return self.numProbeslim

	class Meta:
		verbose_name_plural = "NumberOfProbes & its cost"
