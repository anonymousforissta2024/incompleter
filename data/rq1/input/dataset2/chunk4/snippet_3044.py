#Source: https://stackoverflow.com/questions/77696025/typeerror-object-of-type-client-is-not-json-serializable-when-using-langchain
template = """Tell me a {adjective} joke about {subject}."""
prompt = PromptTemplate(template=template, input_variables=["adjective", "subject"])
llm_chain = LLMChain(prompt=prompt, llm=config.openaiExample, verbose=True)

llm_chain.predict(adjective="sad", subject="ducks")