#Source: https://stackoverflow.com/questions/75320868/attributeerror-module-click-utils-has-no-attribute-expand-args-when-im-t
# Loop over the contents of the directory containing the resumes, filtering by .pdf or .doc(x)
for resume in list(filter(lambda x: extension in x, os.listdir(PROJECT_DIR + '/CV'))):
    if extension == 'pdf':
        # Read in every resume with pdf extension in the directory
        resume_texts.append(nlp(extract_text_from_pdf(PROJECT_DIR + '/CV/' + resume)))
    elif 'doc' in extension:
        # Read in every resume with .doc or .docx extension in the directory
        resume_texts.append(nlp(extract_text_from_word(PROJECT_DIR + '/CV/' + resume)))
        
    resume_names.append(resume.split('_')[0].capitalize())