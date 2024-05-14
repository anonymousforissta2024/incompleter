#Source: https://stackoverflow.com/questions/70302409/elasticsearch-typeerror-string-indices-must-be-integers
doc_dir = "GRIs/"  # contains 2 .pdfs

with open('filt_gri.txt', 'r') as filehandle:
    tags = [current_place.rstrip() for current_place in filehandle.readlines()]


doc_classifier = TransformersDocumentClassifier(model_name_or_path="cross-encoder/nli-distilroberta-base",
                                                task="zero-shot-classification",
                                                labels=tags,
                                                batch_size=2)

# convert to Document using a fieldmap for custom content fields the classification should run on
docs_to_classify = [Document.from_dict(d) for d in docs_sliding_window]

# classify using gpu, batch_size makes sure we do not run out of memory
classified_docs = doc_classifier.predict(docs_to_classify)

# let's see how it looks: there should be a classification result in the meta entry containing labels and scores.
print(classified_docs[0].to_dict())

all_docs = convert_files_to_dicts(dir_path=doc_dir)

preprocessor_sliding_window = PreProcessor(split_overlap=3,
                                           split_length=10,
                                           split_respect_sentence_boundary=False,
                                           split_by='passage')