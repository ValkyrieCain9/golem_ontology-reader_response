import csv
from rdflib import Graph, Namespace, Literal, RDF, URIRef, RDFS, OWL, DCTERMS, SDO
from rdflib.namespace import XSD

#rdflib namespace SDO = schema.org

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
    # change uri to current ttl modelet
    URIRef("file:///Users/regina/Documents/UNIBO/Thesis/GOLEM/golem_ontology-reader_response/reader_response_module/development/03/modelet_TBox.ttl")
))

DISCOURSE_ACT = RESPONSE_ONT.Discourse_Act
EXPRESSION = RESPONSE_ONT.Expression
ACTOR = RESPONSE_ONT.Actor

# read the csv
# change path to new data modelet

# modelet 1 - goodreads review
with open("reader_response_module/development/03/modelet_goodreads.csv", newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=",")
    for row in reader:

        #actor
        actor_uri = RESPONSE_DATA[row["comment_actor"].strip()]
        g.add((actor_uri, RDF.type, ACTOR))

        #expression
        exp_uri = RESPONSE_DATA["goodReadsBook"]
        g.add((exp_uri, RDF.type, EXPRESSION))
        g.add((exp_uri, DCTERMS.title, Literal(row["comment_subject"].strip())))

        #comment
        comment_uri = RESPONSE_DATA[row["comment_id"].strip()]
        g.add((comment_uri, RDF.type, DISCOURSE_ACT))
        g.add((comment_uri, RESPONSE_ONT.has_value, Literal(row["comment_content"].strip())))
        g.add((actor_uri, RESPONSE_ONT.created, comment_uri))
        g.add((comment_uri, RESPONSE_ONT.has_subject, exp_uri))
        g.add((comment_uri, RESPONSE_ONT.has_type, RESPONSE_ONT[row["comment_type"].strip()]))

        #clause
        clause_uri = RESPONSE_DATA[row["clause_id"].strip()]
        g.add((clause_uri, RDF.type, DISCOURSE_ACT))
        g.add((clause_uri, RESPONSE_ONT.has_value, Literal(row["clause_content"].strip())))
        g.add((clause_uri, RESPONSE_ONT.has_type, RESPONSE_DATA[row["clause_type"].strip()]))
        if row["clause_theme"]:
            g.add((clause_uri, RESPONSE_ONT.has_theme, RESPONSE_ONT[row["clause_theme"].strip()]))
        if row["clause_sentiment"]:
            g.add((clause_uri, RESPONSE_ONT.has_sentiment, RESPONSE_ONT[row["clause_sentiment"].strip()]))
        g.add((clause_uri, RESPONSE_ONT.part_of, comment_uri))

# modelet 2 - ao3
with open("reader_response_module/development/03/modelet_ao3.csv", newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=",")
    for row in reader:

        #actor
        actor_uri = RESPONSE_DATA[row["comment_actor"].strip()]
        g.add((actor_uri, RDF.type, ACTOR))
        g.add((actor_uri, RESPONSE_ONT.has_role, RESPONSE_ONT[row["actor_role"].strip()]))

        #expression
        exp_uri = RESPONSE_DATA["ao3Fanfic"]
        g.add((exp_uri, RDF.type, EXPRESSION))
        g.add((exp_uri, DCTERMS.title, Literal(row["comment_subject"].strip())))

        post_exp_uri = RESPONSE_DATA["ForeverGirl_Chapter1"]
        g.add((post_exp_uri, RDF.type, EXPRESSION))
        g.add((post_exp_uri, DCTERMS.title, Literal("Breathless")))

        #comment
        comment_uri = RESPONSE_DATA[row["comment_id"].strip()]
        g.add((comment_uri, RDF.type, DISCOURSE_ACT))
        g.add((comment_uri, RESPONSE_ONT.has_value, Literal(row["comment_content"].strip())))
        g.add((actor_uri, RESPONSE_ONT.created, comment_uri))
        g.add((comment_uri, RESPONSE_ONT.has_subject, exp_uri))
        g.add((comment_uri, RESPONSE_ONT.has_type, RESPONSE_ONT[row["comment_type"].strip()]))
        g.add((comment_uri, RESPONSE_ONT.responds_to, RESPONSE_DATA[row["comment_responds_to"].strip()]))

        #clause
        clause_uri = RESPONSE_DATA[row["clause_id"].strip()]
        g.add((clause_uri, RDF.type, DISCOURSE_ACT))
        g.add((clause_uri, RESPONSE_ONT.has_value, Literal(row["clause_content"].strip())))
        g.add((clause_uri, RESPONSE_ONT.has_type, RESPONSE_ONT[row["clause_type"].strip()]))
        if row["clause_theme"]:
            g.add((clause_uri, RESPONSE_ONT.has_theme, RESPONSE_ONT[row["clause_theme"].strip()]))
        if row["clause_sentiment"]:
            g.add((clause_uri, RESPONSE_ONT.has_sentiment, RESPONSE_ONT[row["clause_sentiment"].strip()]))
        if row["clause_responds_to"]:
            g.add((clause_uri, RESPONSE_ONT.responds_to, RESPONSE_DATA[row["clause_responds_to"].strip()]))
        g.add((clause_uri, RESPONSE_ONT.part_of, comment_uri))

# modelet 3 - reddit
with open("reader_response_module/development/03/modelet_reddit.csv", newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=",")
    for row in reader:

        #actor
        actor_uri = RESPONSE_DATA[row["comment_actor"].strip()]
        g.add((actor_uri, RDF.type, ACTOR))

        #expression
        post_exp_uri = RESPONSE_DATA["redditAnimeDiscussion"]
        g.add((post_exp_uri, RDF.type, EXPRESSION))
        g.add((post_exp_uri, DCTERMS.title, Literal("Araburu Kisetsu no Otome-domo yo. - Thursday Anime Discussion Thread (ft. /r/anime Writing Club)")))

        anime_exp_uri = RESPONSE_DATA["anime"]
        g.add((exp_uri, RDF.type, EXPRESSION))
        g.add((exp_uri, DCTERMS.title, Literal(row["comment_subject"].strip())))

        #thread
        thread_uri = RESPONSE_DATA[row["thread_id"].strip()]
        g.add((thread_uri, RDF.type, RESPONSE_ONT[row["thread_type"].strip()]))

        #comment
        comment_uri = RESPONSE_DATA[row["comment_id"].strip()]
        g.add((comment_uri, RDF.type, DISCOURSE_ACT))
        g.add((comment_uri, RESPONSE_ONT.has_value, Literal(row["comment_content"].strip())))
        g.add((actor_uri, RESPONSE_ONT.created, comment_uri))
        g.add((comment_uri, RESPONSE_ONT.has_subject, anime_exp_uri))
        g.add((comment_uri, RESPONSE_ONT.has_type, RESPONSE_ONT[row["comment_type"].strip()]))
        g.add((comment_uri, RESPONSE_ONT.responds_to, RESPONSE_DATA[row["comment_responds_to"].strip()]))
        g.add((comment_uri, RESPONSE_ONT.part_of, thread_uri))

# save
g.serialize(destination="reader_response_module/development/03/modelet_ABox.ttl", format="turtle")
print("RDF file successfully saved as 'modelet_ABox.ttl'")