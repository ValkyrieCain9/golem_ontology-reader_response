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
g.add((
    URIRef("https://w3id.org/golem/ontology/response/data#"),
    OWL.imports,
    URIRef("file:///Users/regina/Documents/UNIBO/Thesis/GOLEM/golem_ontology-reader_response/reader_response_module/development/01/modelet_TBox.ttl")
))

index = 1  # moved outside loop

# read the csv
with open("reader_response_module/development/01/data_modelet.csv", newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=",")
    for row in reader:
        comment_uri = RESPONSE_DATA[row["comment"].strip()]
        g.add((comment_uri, RDF.type, RESPONSE_ONT.Comment))

        post_uri = RESPONSE_DATA[row["post"].strip()]
        g.add((post_uri, RDF.type, RESPONSE_ONT.Post))

        post_creator_uri = RESPONSE_DATA[row["post_creator"].strip()]
        g.add((post_creator_uri, RDF.type, RESPONSE_ONT.User))

        comment_creator_uri = RESPONSE_DATA[row["comment_creator"].strip()]
        g.add((comment_creator_uri, RDF.type, RESPONSE_ONT.User))

        site_uri = RESPONSE_DATA[row["site"].strip()]
        g.add((site_uri, RDF.type, RESPONSE_ONT.Site))
        g.add((site_uri, RESPONSE_ONT.hasPost, post_uri))

        # comment triples
        g.add((post_uri, RESPONSE_ONT.hasComment, comment_uri))
        g.add((comment_uri, RESPONSE_ONT.createdBy, comment_creator_uri))

        if row["thread"].strip():
            thread_uri = RESPONSE_DATA[row["thread"].strip()]
            g.add((thread_uri, RDF.type, RESPONSE_ONT.Thread))
            g.add((comment_uri, RESPONSE_ONT.partOfThread, thread_uri))

        if row["rating"].strip():
            rating_uri = RESPONSE_DATA[f"rating_{index}"]
            g.add((rating_uri, RDF.type, RESPONSE_ONT.Rating))
            g.add((rating_uri, RESPONSE_ONT.hasRatingValue, Literal(row["rating"].strip())))
            rating_system_uri = RESPONSE_DATA[row["rating system"].strip()]
            g.add((rating_system_uri, RDF.type, RESPONSE_ONT.RatingSystem))
            g.add((rating_uri, RESPONSE_ONT.hasRatingSystem, rating_system_uri))
            g.add((comment_uri, RESPONSE_ONT.hasRating, rating_uri))
            index += 1

        if row["hasReply"].strip():
            replies = row["hasReply"].split(",")
            for r in replies:
                r = r.strip()
                if r:
                    reply_uri = RESPONSE_DATA[r]
                    g.add((comment_uri, RESPONSE_ONT.hasReply, reply_uri))

        # post triples
        g.add((post_uri, RESPONSE_ONT.createdBy, post_creator_uri))
        g.add((post_uri, RESPONSE_ONT.hasSite, site_uri))
        g.add((post_uri, DCTERMS.title, Literal(row["post_title"].strip())))

# save
g.serialize(destination="reader_response_module/development/01/modelet_ABox.ttl", format="turtle")
print("RDF file successfully saved as 'modelet_ABox.ttl'")