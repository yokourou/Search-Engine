# Woogle: Mini Wiki Search Engine

## Introduction

**Woogle** est un moteur de recherche minimaliste conçu pour explorer et indexer des documents à partir de sources Wikimedia, en utilisant des techniques classiques d'**Information Retrieval** (IR). Ce projet fait partie d'une session pratique dans le cadre du cours de Recherche d'Information, et il vise à construire un moteur de recherche efficace et optimisé pour les pages Wikipedia.

Le but principal de ce projet est de permettre aux utilisateurs de rechercher des documents Wikipédia pertinents en utilisant des modèles vectoriels et l'algorithme **PageRank**, tout en expérimentant diverses techniques pour améliorer la qualité et la pertinence des résultats.

## Objectifs du projet

- Collecter des pages à partir de Wikipedia via leur API.
- Traiter et analyser les données collectées pour en extraire des informations utiles.
- Implémenter l'algorithme **PageRank** pour évaluer l'importance des pages.
- Mettre en œuvre un modèle vectoriel pour effectuer des recherches dans les pages collectées.
- Explorer des améliorations possibles, telles que le **stemming**, la **sémantique latente**, ou l'usage d'**embeddings** pour améliorer la recherche.

## Prérequis

### Python Modules
Pour exécuter ce projet, tu auras besoin de certains modules Python. Si ces modules ne sont pas déjà installés sur ton système, tu peux les installer en utilisant la commande suivante :

```bash
pip3 install --user -r requirements.txt
