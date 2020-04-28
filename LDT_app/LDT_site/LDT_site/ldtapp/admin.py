from django.contrib import admin
from ldtapp.models import variables
from ldtapp.models import geneLengthList
from ldtapp.models import geneDiseaseList
from ldtapp.models import kitOutputCost
from ldtapp.models import hybridProbesCost
# Register your models here.

admin.site.register(variables)
admin.site.register(geneLengthList)
admin.site.register(geneDiseaseList)
admin.site.register(kitOutputCost)
admin.site.register(hybridProbesCost)

admin.site.site_header = 'Strandls Content Manager' 