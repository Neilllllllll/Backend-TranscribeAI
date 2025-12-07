# 📚 Documentation Technique du Backend

> Ce document fournit un aperçu de l'architecture, du flux de requêtes, des conventions de développement de notre service backend, et les étapes pour le récupérer et l'utiliser.

---

## ⚙️ Architecture Générale et Flux de Requête

Le diagramme ci-dessous illustre comment une requête HTTP transite à travers les différents composants logiciels :

![Diagramme d'architecture Backend](assets/Architecture_backend.png)

---

## 🧭 Routes (Le Régulateur de Trafic)

### Définition
Le composant **Routes** est le point d'entrée qui associe l'URL de la requête entrante au gestionnaire approprié (**Controller**).

> **🚦 Fonction Principale :** Contient la logique d'aiguillage et de distribution des requêtes HTTP vers les bonnes destinations.

---

## 🛡️ Middlewares (Les Agents de Contrôle)

### Définition
Les **Middlewares** sont une suite de fonctions exécutées successivement lors du traitement d’une requête HTTP.

> **✅ Fonction Principale :** Gérer des tâches transversales (authentification, journalisation, validation, etc.) **avant** que la requête n'atteigne le contrôleur final. ( c'est un filtre )

* **Pipeline de Traitement :** Plusieurs Middlewares peuvent s'enchaîner pour former un **pipeline** de traitement.
* **Réutilisabilité :** Ils sont conçus pour être réutilisés sur plusieurs routes.
* **Organisation :** Ils sont regrouper dans un répertoire dédié (`/middlewares`).
* **🛑 Prérogative Atypique :** Un Middleware peut **avorter** le traitement d'une requête et retourner immédiatement une réponse (ex: `401 Unauthorized`) sans jamais exécuter le Controller.

---

## 🎬 Controllers (Le Gestionnaire d'Opérations)

### Définition
Le **Controller** est chargé d'orchestrer la réponse en utilisant les **Services**. Il est le lien entre le protocole HTTP et la logique métier.

> **🤝 Fonction Principale :** Traiter la requête entrante, déléguer la logique métier, et **construire la réponse** appropriée à retourner au client.

### Rôles et Conventions

1.  **Prérogative I (Aller) :** Chaque méthode reçoit la requête et **transmet les données utiles** à un ou plusieurs Services.
2.  **Prérogative II (Retour) :** **Retourne la réponse finale** (JSON, statut HTTP) attendue par le client.

#### ⚠️ Points Cruciaux
* **Limitation :** Le Controller devrait se limiter strictement aux deux prérogatives ci-dessus (Réception et Retour).
* **Délégation :** Toute la **logique métier complexe** doit être déléguée aux **Services**.
* **Structure :** Un Controller gère généralement l’ensemble des méthodes associées aux routes d'une même ressource.

---

## 🛠️ Services (Le Cœur de la Logique Métier)

### Définition
Les **Services** centralisent la logique métier et les traitements complexes pour garantir un code modulaire, réutilisable et facile à maintenir.

> **🧠 Fonction Principale :** Centraliser l'essentiel de la **logique métier** et les interactions avec les données (Models/Repositories).

### Principe de Conception

* **Prérogative :** Le Service **exécute** les actions et les transformations nécessaires.
* **SOLID (SRP) :** Un Service ne doit posséder qu'une **unique responsabilité** (une seule raison d'être modifié), conformément au **Single Responsibility Principle**.

---