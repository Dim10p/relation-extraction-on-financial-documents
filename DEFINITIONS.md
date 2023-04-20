# Definitions

## Data dictionary

| Variable     | Data Type | Definition                                                                                                                                                                                                                                                                     | Values                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | N/X/Y |
|--------------|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------|
| id           | string    | Unique identifier for each data point. (Associated path or ID)                                                                                                                                                                                                                 | e.g, BERTPretrain_10KReports/2017/QTR2/20170518_10-K_edgar_data_319671_0001437749-17-009518_1.txt<br> or <br> None                                                                                                                                                                                                                                                                                                                                                                                                | N     |
| docid        | string    | Fiscal year of each data point.                                                                                                                                                                                                                                                | "2016/2017" everywhere                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | N     |
| relation     | string    | The type of relationship between the two entities.                                                                                                                                                                                                                             | ['no_relation', 'org:org:agreement_with', 'org:org:subsidiary_of','org:org:shares_of', 'org:org:acquired_by', 'pers:univ:attended','pers:univ:employee_of', 'pers:univ:member_of','pers:gov_agy:member_of', 'pers:org:employee_of','pers:org:member_of', 'pers:org:founder_of', 'pers:title:title','org:gpe:operations_in', 'org:gpe:headquartered_in','org:gpe:formed_in', 'org:money:revenue_of', 'org:money:loss_of', 'org:money:cost_of', 'org:money:profit_of', 'org:date:formed_on','org:date:acquired_on'] | Y     |
| rel_group    | string    | The type of the two entities.                                                                                                                                                                                                                                                  | ['ORG-ORG', 'PERSON-UNIV', 'PERSON-GOV_AGY', 'PERSON-ORG', 'PERSON-TITLE', 'ORG-GPE', 'ORG-MONEY', 'ORG-DATE']                                                                                                                                                                                                                                                                                                                                                                                                    | X     |
| token        | list      | The list of tokens for the sentence.                                                                                                                                                                                                                                           | e.g, ["warrants", "to", "purchase", "Lumos", "Networks", ...]                                                                                                                                                                                                                                                                                                                                                                                                                                                     | X     |
| e1_start     | Int       | The starting index of entity 1 in the token list.                                                                                                                                                                                                                              | e.g, 9                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | X     |
| e1_end       | Int       | The ending index of entity 1 in the token list.                                                                                                                                                                                                                                | e.g, 12                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | X     |
| e2_start     | Int       | The starting index of entity 2 in the token list.                                                                                                                                                                                                                              | e.g, 3                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | X     |
| e2_end       | Int       | The ending index of entity 2 in the token list.                                                                                                                                                                                                                                | e.g, 6                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | X     |
| e1_type      | string    | The type of entity 1.                                                                                                                                                                                                                                                          | ['ORG', 'PERSON']                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | X     |
| e2_type      | string    | The type of entity 2.                                                                                                                                                                                                                                                          | ['ORG', 'UNIV', 'GOV_AGY', 'TITLE', 'GPE', 'MONEY', 'DATE']                                                                                                                                                                                                                                                                                                                                                                                                                                                       | X     |
| spacy_pos    | list      | The list of part-of-speech tags* for the sentence.                                                                                                                                                                                                                             | e.g, ["NNS", "TO", "VB", "NNP", "NNP", "NNP", "JJ", "NN", ...]                                                                                                                                                                                                                                                                                                                                                                                                                                                    | X     |
| spacy_ner    | list      | The list of named entity recognition tags** for the sentence.                                                                                                                                                                                                                  | e.g, ["O", "O", "O", "ORG", "ORG", "ORG", "O", "O", ...]                                                                                                                                                                                                                                                                                                                                                                                                                                                          | X     |
| spacy_head   | list      | The list of dependency parsing head indices for each token.                                                                                                                                                                                                                    | e.g, [0, 2, 0, 5, 5, 7, 7, 2, ...]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | X     |
| spacy_deprel | list      | The list of dependency relations*** of each token with respect to its parent token in the sentence, as identified by the Spacy dependency parser.                                                                                                                              | e.g, ["ROOT", "aux", "acl", "nmod", ...]                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | X     |
| sdp          | string    | The shortest dependency path (SDP) between two entities in a sentence. The SDP is the shortest path between the two entities in the dependency tree, where each edge in the tree corresponds to a grammatical relationship between two words (e.g. subject, object, modifier). | e.g, "Lumos Networks Corp. stock purchase the Pamplona Entities"                                                                                                                                                                                                                                                                                                                                                                                                                                                  | X     |
| sdp_tok_idx  | list      | The indices of the tokens in the sentence that make up the shortest dependency path.                                                                                                                                                                                           | e.g, [7, 2]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | X     |
| token_test   | string    | The concatenated form of the token list.                                                                                                                                                                                                                                       | e.g, "warrantstopurchaselumosnetworkscorpcommonstockthepamplonaentities"                                                                                                                                                                                                                                                                                                                                                                                                                                          | X     |
| e1           | string    | The text of entity 1.                                                                                                                                                                                                                                                          | e.g, "thepamplonaentities"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | X     |
| e2           | string    | The text of entity 2.                                                                                                                                                                                                                                                          | e.g, "lumosnetworkscorp"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | X     |

## Detailed definitions and descriptions

*The spacy_pos variable contains a list of part-of-speech (POS) tags for each token in the sentence.
Part-of-speech tagging is the process of labeling the words in a text corpus with their
corresponding part of speech. The tags are defined as follows:

| POS tag | Description               | Examples                                        |
|---------|---------------------------|-------------------------------------------------|
| ADJ     | adjective                 | *big, old, green, incomprehensible, first*      |
| ADP     | adposition                | *in, to, during*                                |
| ADV     | adverb                    | *very, tomorrow, down, where, there*            |
| AUX     | auxiliary                 | *is, has (done), will (do), should (do)*        |
| CONJ    | conjunction               | *and, or, but*                                  |
| CCONJ   | coordinating conjunction  | *and, or, but*                                  |
| DET     | determiner                | *a, an, the*                                    |
| INTJ    | interjection              | *psst, ouch, bravo, hello*                      |
| NOUN    | noun                      | *girl, cat, tree, air, beauty*                  |
| NUM     | numeral                   | *1, 2017, one, seventy-seven, IV, MMXIV*        |
| PART    | particle                  | *’s, not,*                                      |
| PRON    | pronoun                   | *I, you, he, she, myself, themselves, somebody* |
| PROPN   | proper noun               | *Mary, John, London, NATO, HBO*                 |
| PUNCT   | punctuation               | *., (, ), ?*                                    |
| SCONJ   | subordinating conjunction | *if, while, that*                               |
| SYM     | symbol                    | *$, %, §, ©, +, −, ×, ÷, =, :), 😝*             |
| VERB    | verb                      | *run, runs, running, eat, ate, eating*          |
| X       | other                     | *sfpksdpsxmsa*                                  |
| SPACE   | space                     |                                                 |


**The space_ner variable contains named entity recognition (NER) tags for each token in the text.
Named entities are words or phrases that refer to specific types of objects or concepts,
such as people, organizations, locations, etc. The NER tags in space_ner indicate whether each token
is part of a named entity and what type of entity it is. 
The possible NER tags and their descriptions are as follows:

| NER tag | Description                             |
|---------|-----------------------------------------|
| O       | None of the below                       |
| ORG     | Companies, agencies, institutions, etc. |
| DATE    | Absolute or relative dates or periods   |
| PERSON  | People, including fictional             |
| GOV_AGY | Government agencies and departments     |
| UNIV    | Universities, colleges, etc.            |
| MONEY   | Monetary values, including unit         |
| GPE     | Countries, cities, states               |
| TITLE   | Positions or titles, including military |


***The Spacy dependency parser constructs a tree structure that represents the syntactic structure of the sentence,
where each node in the tree represents a token in the sentence and the edges between nodes represent the 
syntactic relationships between the tokens.
Each token in the sentence has a corresponding spacy_deprel value that indicates the dependency 
relation between that token and its parent token. The possible values for spacy_deprel 
include various types of grammatical relationships such as subject, object, adjectival modifier, and more.
The possible spacy_deprel values and their descriptions are as follows:

| deprel values | Description                                  |
|---------------|----------------------------------------------|
| acl           | clausal modifier of noun (adjectival clause) |
| acomp         | adjectival complement                        |
| advcl         | adverbial clause modifier                    |
| advmod        | adverbial modifier                           |
| agent         | agent                                        |
| amod          | adjectival modifier                          |
| appos         | appositional modifier                        |
| attr          | attribute                                    |
| aux           | auxiliary                                    |
| auxpass       | auxiliary (passive)                          |
| case          | case marking                                 |
| ccomp         | clausal complement                           |
| compound      | compound                                     |
| conj          | conjunct                                     |
| cop           | copula                                       |
| csubj         | clausal subject                              |
| csubjpass     | clausal subject (passive)                    |
| dative        | dative                                       |
| dep           | unclassified dependent                       |
| det           | determiner                                   |
| dobj          | direct object                                |
| expl          | expletive                                    |
| intj          | interjection                                 |
| mark          | marker                                       |
| meta          | meta modifier                                |
| neg           | negation modifier                            |
| nounmod       | modifier of nominal                          |
| npmod         | noun phrase as adverbial modifier            |
| nsubj         | nominal subject                              |
| nsubjpass     | nominal subject (passive)                    |
| nummod        | numeric modifier                             |
| oprd          | object predicate                             |
| obj           | object                                       |
| obl           | oblique nominal                              |
| parataxis     | parataxis                                    |
| pcomp         | complement of preposition                    |
| pobj          | object of preposition                        |
| poss          | possession modifier                          |
| preconj       | preconjunt                                   |
| predet        | predeterminer                                |
| prep          | prepositional modifier                       |
| prt           | particle                                     |
| punct         | punctuation                                  |
| quantmod      | modifier of quantifier                       |
| relcl         | relative clause modifier                     |
| ROOT          | root of the dependency tree                  |
| xcomp         | open clausal complement                      |
