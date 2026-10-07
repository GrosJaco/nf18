# Projet NF18 - CrowdFundr
## Rendu 1 : Notes de clarification (NDC)

**Auteurs :** Alexandre JEFFERY, Hugo GOSSE, Rafael REIS, Jaime GOMES-PARENTE

### 1. Clarifications conceptuelles et prises de décision concernant les règles de gestion

### 2. Classe / Entités et associations

### Classes / Entités et Associations

| Classe / Entité | Attributs | Contraintes / Associations |
| :--- | :--- | :--- |
| Projet (abstraite) | - id_projet {clé}<br>- titre<br>- description<br>- objectif_financier (€)<br>- date_lancement<br>- /montant_collecte (€) {dérivé : somme des contributions} | - Héritage par partition (exclusion mutuelle et complétude) vers Projet technologique, Projet artistique et Projet social.<br>- Accompagné par 0 ou 1 Incubateur.<br>- Porté par 1 ou plusieurs Membres d'équipe (via classe-association Participation).<br>- Propose 0, 1 ou plusieurs Contreparties.<br>- Reçoit 0, 1 ou plusieurs Contributions financières.<br>- Reçoit 0, 1 ou plusieurs Avis. |
| Projet technologique | - type_innovation | - Héritage de Projet. |
| Projet artistique | - medium_principal | - Héritage de Projet. |
| Projet social | - region_cible | - Héritage de Projet.<br>- Soutenu officiellement par 0, 1 ou plusieurs ONG. |
| Incubateur | - id_incubateur {clé}<br>- nom<br>- annee_creation<br>- budget_accompagnement | - Accompagne 0, 1 ou plusieurs Projets. |
| ONG | - numero_enregistrement {clé}<br>- nom<br>- pays_origine | - Soutient 0, 1 ou plusieurs Projets sociaux. |
| Membre d'équipe | - id_membre {clé}<br>- nom<br>- prenom<br>- pays_residence<br>- date_naissance | - Participe à 0, 1 ou plusieurs Projets via la classe-association Participation. |
| Utilisateur | - pseudo {clé}<br>- email {unique}<br>- nom<br>- date_naissance | - Effectue 0, 1 ou plusieurs Contributions financières.<br>- Dépose 0, 1 ou plusieurs Avis (sous condition de contribution préalable). |
| Contribution financière | - id_contribution {clé}<br>- date_heure (DATETIME)<br>- montant (€) | - Réalisée par 1 Utilisateur sur 1 Projet.<br>- Plusieurs contributions possibles du même utilisateur sur le même projet (distinguées par date_heure).<br>- Liée à 0 ou 1 Contrepartie (qui doit appartenir au projet concerné).<br>- Contrainte : montant > 0. |
| Contrepartie (abstraite) | - id_contrepartie {clé}<br>- libelle | - Proposée par exactement 1 Projet (Projet 1 — 0..* Contrepartie).<br>- Héritage par partition (exclusion mutuelle et complétude) vers Contrepartie numérique et Contrepartie physique.<br>- Peut être choisie dans 0, 1 ou plusieurs Contributions financières. |
| Contrepartie numérique | - format_fichier<br>- taille_mo | - Héritage de Contrepartie. |
| Contrepartie physique | - poids_estime<br>- frais_livraison | - Héritage de Contrepartie.<br>- Expédiée par exactement 1 Transporteur partenaire. |
| Transporteur | - nom {clé}<br>- delai_livraison_moyen (jours) | - Expédie 0, 1 ou plusieurs Contreparties physiques. |


### 3. Classes-association / Relations speciales