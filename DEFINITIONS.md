| Variable     | Definition                                                 | Values                                                  |
|--------------|--------------------------------------------------------    |---------------------------------------------------------|
| id           | Unique identifier for each data point.                     | 1                                                       |
| docid        | Identifier for the document the data point belongs to.     | "2016/2017"                                             |
| relation     | The type of relationship between the two entities.         | "no_relation"                                           |
| rel_group    | A grouping of the relation type for evaluation.            | "ORG-ORG"                                               |
| token        | The list of tokens for the sentence.                       | ["warrants", "to", "purchase", "Lumos", "Networks", ...] |
| e1_start     | The starting index of entity 1 in the token list.          | 9                                                       |
| e1_end       | The ending index of entity 1 in the token list.            | 12                                                      |
| e2_start     | The starting index of entity 2 in the token list.          | 3                                                       |
| e2_end       | The ending index of entity 2 in the token list.            | 6                                                       |
| e1_type      | The type of entity 1.                                      | "ORG"                                                   |
| e2_type      | The type of entity 2.                                      | "ORG"                                                   |
| spacy_pos    | The list of part-of-speech tags for the sentence.          | ["NNS", "TO", "VB", "NNP", "NNP", "NNP", "JJ", "NN", ...] |
| spacy_ner    | The list of named entity recognition tags for the sentence. | ["O", "O", "O", "ORG", "ORG", "ORG", "O", "O", ...]     |
| spacy_head   | The list of dependency parsing head indices for each token. | [0, 2, 0, 5, 5, 7, 7, 2, ...]                        |
| spacy_deprel | The list of dependency parsing dependency relation labels for each token. | ["ROOT", "aux", "acl", "nmod", ...]         |
| sdp          | The shortest dependency path between the two entities.     | "Lumos Networks Corp. stock purchase the Pamplona Entities" |
| sdp_tok_idx  | The indices of the tokens in the sentence that make up the shortest dependency path. | [7, 2] |
| token_test   | The concatenated form of the token list.                   | "warrantstopurchaselumosnetworkscorpcommonstockthepamplonaentities" |
| e1           | The text of entity 1.                                      | "thepamplonaentities"                                   |
| e2           | The text of entity 2.                                      | "lumosnetworkscorp"                                     |