# Iteration 2 - Algnment and Refactoring

## CIDOC-CRMdig and Schema.org

In the previous iteration, the classes of Account, Comment, Post, Site and Rating, were described as subclasses of crm:E73_Information_Object. Instead, this iteration makes use of CRMdig, an extension of CIDOC specifically designed for digital resources. 

With its classes, D1_Digital_Object, D7_Digital_Machine_Event, D13_Digital_Information_Carrier, which align with the digital object, translation event and material bearer, respectively, CRMdig provides an established ontological structure for the aspects of a digital object described in the motivating scenario. 

As CRMdig is an extension of CIDOC-CRM this also means that crm:E55_Type can be used as an interface to enrich the classes of CRMdig with type descriptions from Schema.org. Schema.org provides an extensive vocabulary particularly for internet-based resources like WebSite, WebPage, Comment etc., as well as some internet-specific object properties and data properties. To properly align Schema.org with CIDOC, the Schem.org classes need to redefined in the ontology as subclasses or individuals of crm:E55_Type. 

With this, the classes described in the modelet can be condensed or redefined to fit better with the type descriptions that Schema.org provides. In the cases where specific types are not described by Schema.org they can be created within the ontology (e.g. Schema.org has a UserComments class but not a UserPosts class, so this will be created to complement the Schema.org terms). 

A partial view of the model with both CRMdig and Schema.org can be seen below. 

<img width="4347" height="2127" alt="it2_refactor_partial" src="https://github.com/user-attachments/assets/53f7ff54-97b5-493e-a609-f47bb0abea52" />


