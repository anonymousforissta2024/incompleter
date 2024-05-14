#Source: https://stackoverflow.com/questions/75876808/typeerror-unsupported-operand-types-for-rv-continuous-frozen-and-rv-con
model = Doc2Vec.load('doc2vec.model')
v1 = model.infer_vector(resume.split())
v2 = model.infer_vector(jd_df['data'][0].split())
cosine_similarity = (np.dot(np.array(v1), np.array(v2))) / (norm(np.array(v1)) * norm(np.array(v2)))
print(round(cosine_similarity, 3))