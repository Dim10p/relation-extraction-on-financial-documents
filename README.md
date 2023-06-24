[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity) [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

# Relation Extraction on Financial Documents Challenge (REFinD)

KDF@SIGIR2023 Shared Task
Sponsored by J.P. Morgan

The shared task is a part of the Fourth Workshop on Knowledge Discovery from Unstructured Data in Financial Services, co-located with SIGIR 2023. The competition was hosted here: [CodaLab](https://codalab.lisn.upsaclay.fr/competitions/11770#learn_the_details)


The main file is a jupyter notebook that trains the model on the public datasets, generates the predictions on the private datasets, and further processes the final data: [`main.ipynb`](main.ipynb).


## The REFinD Dataset
Relation extraction (RE) from text is a core problem in NLP and information retrieval that aids in various tasks such as building knowledge graphs, question answering and semantic search. Most available large-scale RE datasets are compiled using general knowledge sources such as Wikipedia, web texts and news articles. However, these datasets often fail to capture domain-specific challenges. In particular, financial text documents such as financial reports and various Securities and Exchange Commission (SEC) filings are significantly different from general English language documents and require extracting entities and relations containing numbers, currencies, dates, legal facts, and claims, and that have much longer and more complex sentences with large distances between entities. To address financial domain-specific challenges, we build the largest-scale relation extraction dataset over financial documents to-date, REFinD, with 29K instances and 22 relations amongst 8 types of entity pairs. REFinD is a domain specific financial relation-extraction dataset built using raw text from various 10-X (10-K, 10-Q, etc. broadly known as 10-X) reports of publicly traded companies that were obtained from US Securities and Exchange Commission (SEC).


### Structure
The repository is structured as follows: 

 - [`data`](data/) contains the public datasets, the private dataset and the output data
 - [`utils`](utils/) contains all the utility functions and constants
 - [`README.md`] (README.md) describes
 - [`main.ipynb`](main.ipynb) is a jupyter notebook that trains the model on the public datasets, performs the predictions on the private dataset, and further processes the output
 - [`requirements.txt`](requirements.txt) contains the requirements for the project


### Authors

[Dimitrios Petridis](https://github.com/dim10P)

[Stefan Pasch](https://github.com/Stefan-Pasch)