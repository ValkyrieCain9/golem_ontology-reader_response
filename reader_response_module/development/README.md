# Development of Reader Response Module with SAMOD

The Simplified Agile Methodology for Ontology Development (SAMOD) provides a simple workflow centred around a set of small iterative steps aimed at creating well-developed and well-documented ontological models.

Each iteration is made up of a set of resources. Firstly is the Motivating Scenario which provides a description of certain aspect of the domain, with an accompanying set of intuitive examples. 

From the Motivating scenario a set of Informal Competency Questions are created to outline the informal requirements of the model as well as the key aspects that should be included in the model. 

With the Motivating Scenario and Informal Competency Questions a Glossary of Terms is created which provides a list of the key terms and their descriptions which will be used to create the modelet of the iteration. 

The modelet is described both visually in a diagram as well as in RDF, saved in a Tbox. Once the TBox is tested an ABox is created with a small set of example data.  From the Informal Competency Questions a set of SPARQL queries are used to test ABox. 

Once the modelet has been tested it is then aligned to the current full model and refactored with existing ontologies and standards. Again another TBox and ABox are created to test the full model after this alignment. 

*Peroni, Silvio. 2017. ‘A Simplified Agile Methodology for Ontology Development’. In OWL: Experiences and Directions – Reasoner Evaluation, edited by Mauro Dragoni, María Poveda-Villalón, and Ernesto Jimenez-Ruiz. Springer International Publishing. https://doi.org/10.1007/978-3-319-54627-8_5.*


### Iteration 1 – Comments and Commenting
This iteration provides a  simplistic view of the domain of commenting online. It defines a set of 8 new classes which are then aligned to the CIDOC-CRM framework as subclasses. 

### Iteration 2 - Digital Objects, Websites and Webpages
This iteration looks more closely at the nature of digital objects, following closely the description provided by *Faulkner, P., & Runde, J. (2019). Theorizing the Digital Object.* 

While it still aligns with CIDOC-CRM it makes use of one of its extensions CRMdig which provides established classes for digital objects and events in the digital space. With the structure grounded in CIDOC-CRM it then makes use of Schema.org for its type descriptions of digital objects like websites and webpages. 

### Iteration 3 - Discourse Acts and Discourse Structure
This iteration is concerned with the social expression of discourse in general as well as particularly about creative works. It extends the work of *Zhang, A., Culbertson, B., & Paritosh, P. (2017). Characterizing Online Discussion Using Coarse Discourse Sequences.* and *Rebora, S., & Vezzani, G. (2024). Models of Literary Evaluation and Web 2.0. An Annotation Experiment with Goodreads Reviews.*, which both provided descriptions for different types of discourse, and combines this with the work of *Liu, Y., Choi, F., & Chandrasekharan, E. (2026). Needling Through the Threads: A Visualization Tool for Navigating Threaded Online Discussions.*, which helps to describe threads as a structure of discourse. 

From this the aspect of discourse is combined with the full model to sit on top of the digital framework established in the previous iteration. 

