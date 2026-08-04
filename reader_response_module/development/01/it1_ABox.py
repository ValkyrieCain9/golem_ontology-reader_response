import csv
from rdflib import Graph, Namespace, Literal, RDF, URIRef, RDFS, OWL, DCTERMS
from rdflib.namespace import XSD

RESPONSE_ONT = Namespace("https://w3id.org/golem/ontology/response#")
RESPONSE_DATA = Namespace("https://w3id.org/golem/ontology/response/data#")
CRM = Namespace("http://erlangen-crm.org/240307/")
DLP_LITE = Namespace("http://www.ontologydesignpatterns.org/ont/dlp/DOLCE-Lite.owl#")
GOLEM = Namespace("https://w3id.org/golem/ontology#")

# Graph
g = Graph()
# g.parse("reader_response_module/development/01/modelet_TBox.ttl", format="turtle")

g.bind("r", RESPONSE_ONT)
g.bind("rd", RESPONSE_DATA)
g.bind("crm", CRM)
g.bind("dlp_lite", DLP_LITE)
g.bind("golem", GOLEM)

g.add((URIRef("https://w3id.org/golem/ontology/response/data#"), RDF.type, OWL.Ontology))
g.add((
    URIRef("https://w3id.org/golem/ontology/response/data#"),
    OWL.imports,
    URIRef("file:///Users/regina/Documents/UNIBO/Thesis/GOLEM/golem_ontology-reader_response/reader_response_module/development/01/it1_Tbox.ttl")
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

        # comment triples
        g.add((post_uri, RESPONSE_ONT.hasComment, comment_uri))
        g.add((comment_uri, RESPONSE_ONT.createdBy, comment_creator_uri))

        if row["thread"].strip():
            thread_uri = RESPONSE_DATA[row["thread"].strip()]
            g.add((thread_uri, RDF.type, RESPONSE_ONT.Thread))
            g.add((comment_uri, DLP_LITE.part_of, thread_uri))

        if row["rating"].strip():
            rating_uri = RESPONSE_DATA[f"rating_{index}"]
            rating_value_uri = RESPONSE_DATA[f"rating_value_{index}"]
            g.add((rating_uri, RDF.type, RESPONSE_ONT.Rating))
            g.add((rating_value_uri, RDF.type, CRM.E54_Dimension))
            g.add((rating_value_uri, CRM.P90_hasValue, Literal(row["rating"].strip())))
            
            rating_system_uri = RESPONSE_DATA[row["rating system"].strip()]
            g.add((rating_system_uri, RDF.type, RESPONSE_ONT.RatingSystem))
            g.add((rating_uri, CRM.P177_assigned_property_of_type, rating_system_uri))
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
        g.add((post_uri, DLP_LITE.part_of, site_uri))
        g.add((post_uri, DCTERMS.title, Literal(row["post_title"].strip())))

# save
g.serialize(destination="reader_response_module/development/01/it1_ABox.ttl", format="turtle")
print("RDF file successfully saved as 'it1_ABox.ttl'")