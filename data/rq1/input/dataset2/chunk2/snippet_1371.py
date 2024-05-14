#Source: https://stackoverflow.com/questions/57958178/attributeerror-transaction-object-has-no-attribute-append
from py2neo import Graph
graph = Graph("bolt://localhost:7687", user="neo4j", password="mypass")
tx = graph.begin()
for name in ["Mohammad", "Ahmad", "Dad", "Mom"]:
    tx.append("CREATE (person:Person {name:{name}}) RETURN person", name=name)
Mohammad, Ahmad, Dad, Mom = [result.one for result in tx.commit()]