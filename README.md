[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity) [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)


# Relation Extraction on Financial Documents (REFinD) Challenge

<b>KDF@SIGIR2023 Shared Task</b> <br>

Sponsored by <br>
<img src="https://github.com/Dim10p/relation-extraction-on-financial-documents/assets/120978979/bab8a7c9-fa7d-4c56-8be6-86727ee77af6" width="250">

The competition was a part of the [Fourth Workshop on Knowledge Discovery from Unstructured Data in Financial Services](https://kdf-workshop.github.io/kdf23/), co-located with SIGIR 2023.<br> The competition was hosted here: [CodaLab](https://codalab.lisn.upsaclay.fr/competitions/11770#learn_the_details)


## The REFinD Dataset
Relation extraction (RE) from text is a core problem in NLP and information retrieval that aids in various tasks such as building knowledge graphs, question answering and semantic search. Most available large-scale RE datasets are compiled using general knowledge sources such as Wikipedia, web texts and news articles. However, these datasets often fail to capture domain-specific challenges. In particular, financial text documents such as financial reports and various Securities and Exchange Commission (SEC) filings are significantly different from general English language documents and require extracting entities and relations containing numbers, currencies, dates, legal facts, and claims, and that have much longer and more complex sentences with large distances between entities. To address financial domain-specific challenges, we build the largest-scale relation extraction dataset over financial documents to-date, REFinD, with 29K instances and 22 relations amongst 8 types of entity pairs. REFinD is a domain specific financial relation-extraction dataset built using raw text from various 10-X (10-K, 10-Q, etc. broadly known as 10-X) reports of publicly traded companies that were obtained from US Securities and Exchange Commission (SEC).<br>
An example instance from the dataset is shown below:
![image](https://github.com/Dim10p/relation-extraction-on-financial-documents/assets/120978979/c93256a3-7353-4183-aa93-e39de8c03d63)
More information about the REFinD dataset can be found here: [REFinD](https://refind-re.github.io/index.html)


## Structure

The repository is structured as follows: 

 - [`data`](data/) contains the public datasets, the private dataset, and the output data
 - [`utils`](utils/) contains all the utility functions and constants
 - [`main.ipynb`](main.ipynb) is a jupyter notebook with the core code
 - [`requirements.txt`](requirements.txt) contains the requirements for the project
 - [`DEFINITIONS.md`](DEFINITIONS.md) briefly describes the dataset, the variables, and the model


## Authors

<i>[Dimitrios Petridis](https://github.com/dim10P) - Data Analyst & BI

[Stefan Pasch](https://github.com/Stefan-Pasch) - Data Scientist

Team: DataMonkeys</i><br>
<img src="https://github.com/Dim10p/relation-extraction-on-financial-documents/assets/120978979/afa8bcbd-bab6-42dc-9d88-025719f55642" width="250">
