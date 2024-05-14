#Source: https://stackoverflow.com/questions/70477075/i-keep-getting-this-error-when-i-want-to-query-data-from-a-model-in-mysql-databa
from Inec_results.models import PollingUnit, Lga
local = Lga.objects.all()   
print(local)