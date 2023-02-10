# Online prediction with Vertex AI andBigQuery ML

**Dans ce tuto, vous allez apprendre à former et à déployer un modèle de prédiction de churn pour l'inférence en temps réel, avec les données dans BigQuery et le modèle formé à l'aide de BigQuery ML, enregistré dans Vertex AI Model Registry et déployé sur un Endpoint sur Vertex AI pour une utilisation  de prédiction en ligne.**

- Ce tutoriel utilise les services d'analyse de données et de ML Google Cloud suivants :

  - BigQuery
  - BigQuery ML
  - Vertex AI Model Registry
  - Vertex endpoints

- Les étapes effectuées comprennent :

  - Utiliser Python et SQL pour interroger les données publiques dans BigQuery
  - Préparation des données pour la modélisation
  - Entraîner un modèle de classification à l'aide de BigQuery ML et l'enregistrer dans Vertex AI Model Registry
  - Inspecter le modèle sur Vertex AI Model Registry
  - Déploiement du modèle sur un endpoint sur Vertex AI
  - Réalisation d'exemples de prédictions en ligne vers le point de terminaison du modèle


- On va travailler avec ce notebook dans ce tuto :



![a](https://user-images.githubusercontent.com/78825764/207851323-e650c847-e680-481a-bdd8-cff50900894c.PNG)


- Liser et exécuter les cellules en faisant attention à les instructions .

- Ignorer cette étape
 
![a](https://user-images.githubusercontent.com/78825764/207851823-ab681f4a-9abd-4b32-9dcb-da373c6d5eaa.PNG)

- ignorez également cette étape puisque nous travaillons dans Vertex AI Workbench Notebooks


![a](https://user-images.githubusercontent.com/78825764/207852308-7ff8a39a-bfa7-4550-9b48-03bf97d6fe12.PNG)

- Dans la partie **Train a classification model using BigQuery ML** quand vous allez executer cette cellule pour entrainer et enregistrer votre model :


![a](https://user-images.githubusercontent.com/78825764/207860373-a0262e9a-888a-42ea-b425-bb05e35e0f35.PNG)

- Executer les autres cellules d'evalution de modèle et de Batch prediction .

- Lorsque vous allez executer cette cellule vous pouvez inspecter le modèle sur Vertex AI Model Registry :

![a](https://user-images.githubusercontent.com/78825764/207865216-4ac469fc-569e-45f8-ba66-8d1af282d523.PNG)


- Go to Model Registry , vous allez trouver le modèle qu'on a enregistré :
 

![a](https://user-images.githubusercontent.com/78825764/207861076-3cb587f1-dfde-40a8-a699-df63aa8a9b9e.PNG)

- Cliquer sur le modèle ensuite sur la version , normalement on a juste une seul version :

![a](https://user-images.githubusercontent.com/78825764/207862099-b0791cb4-fcf7-4188-9fef-ecc5b78d027b.PNG)

- Vous pouvez visualiser les différants metrics pour évaluer le modèle :



![a](https://user-images.githubusercontent.com/78825764/207863158-cdfe6ab1-2c77-4451-a535-30535870ce4e.PNG)

## Deploy the model to an endpoint

- Après avoir entrainer et enregistrer notre modèle , on peut maintenant passer à l'étape de déploiement .

- Exécuter ces cellules : 


![a](https://user-images.githubusercontent.com/78825764/207865830-5056c218-2482-406f-9496-12bfe58ef149.PNG)

- On remarque qu'on a créer un endpoint pour notre modèle, on peut checker que le point de terminaison a bien été créer en cliquant sur Points de Terminaison sur le menu de Vertex AI :

![a](https://user-images.githubusercontent.com/78825764/207867356-ff0c1b82-fb92-44b0-adfa-2d9350a6557c.PNG)

- Maintenant on peut déployer notre modèle en éxecutant cette cellule , ça peut prendre entre 10-15 minutes  :

![a](https://user-images.githubusercontent.com/78825764/207867870-6aa3d5aa-a100-42ee-bc60-dff83d039ed9.PNG)

## Make online predictions to the endpoint :

- À l'aide d'un échantillon des données d'entraînement, vous pouvez tester le point de terminaison pour effectuer des prédictions en ligne.

- Exécuter ces deux cellules :

![a](https://user-images.githubusercontent.com/78825764/207879802-65320725-22a9-444b-ae9c-bc864a23c867.PNG)

![a](https://user-images.githubusercontent.com/78825764/207880537-95abebd7-761f-4dac-bc49-0b11fca11458.PNG)
