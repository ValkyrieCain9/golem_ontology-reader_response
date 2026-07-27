import csv
from rdflib import Graph, Namespace, Literal, RDF, URIRef, RDFS, OWL, DCTERMS
from rdflib.namespace import XSD

RESPONSE_ONT = Namespace("https://w3id.org/golem/ontology/response#")
RESPONSE_DATA = Namespace("https://w3id.org/golem/ontology/response/data#")

# Graph
g = Graph()
# g.parse("reader_response_module/development/01/modelet_TBox.ttl", format="turtle")

g.bind("r", RESPONSE_ONT)
g.bind("rd", RESPONSE_DATA)

g.add((URIRef("https://w3id.org/golem/ontology/response/data#"), RDF.type, OWL.Ontology))
g.add((URIRef("https://w3id.org/golem/ontology/response/data#"), OWL.imports, URIRef("https://w3id.org/golem/ontology/response#")))

# read the csv
with open("reader_response_module/development/01/data_modelet.csv", newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=",")
    for row in reader:
        comment_uri = RESPONSE_DATA[row["comment"].strip()]
        post_uri = RESPONSE_DATA[row["post"].strip()]
        post_creator_uri = RESPONSE_DATA[row["post_creator_id"]]
        comment_creator_uri = RESPONSE_DATA[row["comment_creator_uri"]]
        site_uri = RESPONSE_DATA[row["site"]]

        #comment triples
        #not including rating
        g.add((comment_uri, RESPONSE_ONT.hasPost, post_uri))
        g.add((comment_uri, RESPONSE_ONT.createdBy, comment_creator_uri))
        if row["thread"]:
            thread_uri = RESPONSE_DATA[row["thread"]]
            g.add((comment_uri, RESPONSE_ONT.partOfThreadt, thread_uri))
        if row["rating"]:
            rating_uri = RESPONSE_DATA[row["rating"]]
        if row["hasReply"]:
            replies = row["hasReply"].split(",")
            for r in replies:
                reply_uri = RESPONSE_DATA[r]
                g.add((comment_uri, RESPONSE_ONT.hasReply, reply_uri))

        #post triples
        g.add((post_uri, RESPONSE_ONT.createdBy, post_creator_uri))
        g.add((post_uri, RESPONSE_ONT.hasSite, site_uri))
        g.add((post_uri, DCTERMS.title, Literal(row["post_title"])))


# save
g.serialize(destination="reader_response_module/development/01/modelet_ABox.ttl", format="turtle")
print("RDF file successfully saved as 'modelet_ABox.ttl'")

        