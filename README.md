# Mlops 🌸 My Beautiful App Iris

Il s'agit d'un mini projet Docker avec docker compose avec les données IRIS 

Ce projet est une application web interactive développée avec **Streamlit** pour classifier les fleurs **Iris** en fonction de leurs caractéristiques. L'application permet aux utilisateurs de tester des exemples prédéfinis ou d'entrer leurs propres paramètres pour prédire l'espèce de la fleur.

## 🚀 Fonctionnalités

- **Exemples rapides à tester** : Sélectionnez des exemples prédéfinis pour voir les prédictions instantanément.
- **Entrées personnalisées** : Ajustez les caractéristiques de la fleur via des sliders interactifs.
- **Prédiction en temps réel** : Envoyez les données à une API pour obtenir la classe prédite.
- **Affichage visuel** : Affichez une image de la fleur prédite avec des animations.

## 🛠️ Installation

1. Clonez ce dépôt via ligne de commande ou en utilisant Github Desktop :

   ```bash
   git clone https://github.com/Sahm269/Mlops
   
2. Ensuite placez vous sur le dossier la racine du dossier et tapez la commande suivante:
   
    ```bash
    docker compose up --build
   
   
## 📦 API
L'application envoie une requête POST à une API pour obtenir la prédiction. Assurez-vous que l'API est en cours d'exécution à l'adresse suivante :

   ```bash
   http://server:8000/predict
   
