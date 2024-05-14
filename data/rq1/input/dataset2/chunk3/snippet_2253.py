#Source: https://stackoverflow.com/questions/60446978/while-using-biopython-nameerror-name-pubmed-id-is-not-defined-even-though-it
for plant, disease in plant_disease_list:
    search_query = generate_search_query(plant, disease)
    handle1 = Entrez.esearch(db="pmc", term=search_query, retmax="10")
    record1 = Entrez.read(handle1)
    pubmed_ids = record1.get("IdList")
    if pubmed_id in pubmed_ids=="":
     print("Plant: {} Disease: {} PubmedID: DOI:".format(plant, disease))
    else:

     for pubmed_id in pubmed_ids:
       handle2 = Entrez.esummary(db="pmc", id=pubmed_id)
       records = Entrez.read(handle2)
       for record in records:
          doi = record.get("DOI")
          print("Plant: {} Disease: {} PubmedID: {} DOI: http://doi.org/{}".format(plant, disease, pubmed_id, doi))