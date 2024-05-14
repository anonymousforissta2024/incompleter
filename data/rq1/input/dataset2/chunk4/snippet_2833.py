#Source: https://stackoverflow.com/questions/70277732/glob-filenames-attributeerror-str-object-has-no-attribute-content
with open('filt_gri.txt', 'r') as filehandle:
    tags = [current_place.rstrip() for current_place in filehandle.readlines()]

doc_classifier = TransformersDocumentClassifier(model_name_or_path="cross-encoder/nli-distilroberta-base",
                                                task="zero-shot-classification",
                                                labels=tags,
                                                batch_size=16)

classified_docs = doc_classifier.predict(docs_to_classify)

all_docs = convert_files_to_dicts(dir_path=doc_dir)

preprocessor_sliding_window = PreProcessor(split_overlap=3,
                                           split_length=10,
                                           split_respect_sentence_boundary=False,
                                           split_by='passage')