# Grille de scoring — Visibilité LLM des entités professionnelles marocaines

**Annexe du working paper** · Mohammed TETO · v1.0 · Juin 2026
DOI du document principal : 10.5281/zenodo.20820613 · Licence : CC BY 4.0
mohammedteto.com · github.com/mhdteto

> Grille complète pour transformer des réponses génératives en données comparables. À utiliser avec la matrice de prompts et le modèle de jeu de données associés.

---

## 1. Le LLM Visibility Score (sur 100)

Les pondérations traduisent une hiérarchie de valeur assumée : apparaître compte, être recommandé compte davantage, être décrit faussement doit pénaliser.

```
LLM Visibility Score =
  25 % × Mention Rate
+ 20 % × Recommendation Rate
+ 15 % × Accuracy Score (ramené sur 100)
+ 10 % × Source Evidence Score (ramené sur 100)
+ 10 % × Entity Consistency Score (ramené sur 100)
+ 10 % × Prompt Robustness Score (ramené sur 100)
+  5 % × Multilingual Visibility Score (ramené sur 100)
+  5 % × Sentiment Score (ramené sur 100)
```

## 2. Composantes par taux

```
Mention Rate        = prompts où l'entité est mentionnée / total des prompts testés
Recommendation Rate = prompts où l'entité est recommandée / total des prompts transactionnels + comparatifs
```

(Taux exprimés entre 0 et 1.)

## 3. Échelles 0–5

### Accuracy Score (exactitude de la description)

| Score | Interprétation |
|---:|---|
| 0 | Description absente ou totalement fausse |
| 1 | Très faible, erreurs importantes |
| 2 | Partiellement correcte |
| 3 | Correcte mais superficielle |
| 4 | Claire et majoritairement exacte |
| 5 | Précise, complète et vérifiable |

### Source Evidence Score (qualité des sources)

| Score | Interprétation |
|---:|---|
| 0 | Aucune source |
| 1 | Source vague ou non vérifiable |
| 2 | Source faible |
| 3 | Source officielle ou profil public |
| 4 | Plusieurs sources cohérentes |
| 5 | Sources officielles, tierces et vérifiables |

### Entity Consistency Score (cohérence entre plateformes)

| Score | Interprétation |
|---:|---|
| 0 | Informations contradictoires |
| 1 | Forte ambiguïté |
| 2 | Cohérence faible |
| 3 | Cohérence acceptable |
| 4 | Cohérence forte |
| 5 | Cohérence parfaite entre plateformes |

### Prompt Robustness Score (robustesse aux formulations)

| Score | Interprétation |
|---:|---|
| 0 | L'entité n'apparaît jamais |
| 1 | Apparition isolée |
| 2 | Apparition sur quelques prompts |
| 3 | Apparition sur plusieurs catégories |
| 4 | Apparition stable sur plusieurs formulations |
| 5 | Apparition robuste sur plateformes, langues et catégories |

### Service Match Score (services correctement associés)

| Score | Interprétation |
|---:|---|
| 0 | Aucun service correct |
| 1 | Services majoritairement faux |
| 2 | Un service correct sur plusieurs |
| 3 | Services globalement corrects mais incomplets |
| 4 | Services corrects et représentatifs |
| 5 | Services exacts, complets et bien hiérarchisés |

### Location Accuracy Score (localisation)

| Score | Interprétation |
|---:|---|
| 0 | Localisation fausse |
| 1 | Pays correct, ville fausse |
| 2 | Vague (« Afrique du Nord ») |
| 3 | Pays correct |
| 4 | Ville correcte |
| 5 | Ville + zone d'intervention exactes |

### Sentiment Score (ton de la réponse)

| Score | Interprétation |
|---:|---|
| 0 | Négatif marqué |
| 2 | Plutôt négatif / réservé |
| 3 | Neutre factuel |
| 4 | Plutôt positif |
| 5 | Positif et valorisant (sans flagornerie) |

### Multilingual Visibility Score (constance entre langues)

| Score | Interprétation |
|---:|---|
| 0 | Visible dans une seule langue |
| 1 | Visible dans 1 langue, traces ailleurs |
| 2 | Visible dans 2 langues, inégalement |
| 3 | Visible dans 2 langues de façon stable |
| 4 | Visible dans 3 langues |
| 5 | Visible et cohérent dans les 4 langues testées |

## 4. Score d'hallucination (risque — à pénaliser)

| Score | Interprétation |
|---:|---|
| 0 | Aucune hallucination |
| 1 | Petite approximation sans gravité |
| 2 | Détail incertain ou non sourcé |
| 3 | Information probablement inventée |
| 4 | Erreur importante |
| 5 | Plusieurs affirmations fausses |

Conversion en pénalité :

```
Hallucination Penalty = 5 − Hallucination Score
```

Appliquée sur la composante Accuracy avant agrégation. Principe : être mal cité peut être pire qu'être absent.

## 5. Règles d'arbitrage

- En cas d'hésitation entre deux scores, retenir le **plus bas** (prudence).
- Une recommandation implicite (« vous pourriez regarder du côté de… ») compte comme recommandation ; une simple mention factuelle, non.
- Une source citée mais inaccessible ou hors-sujet est notée au maximum à 1 sur le Source Evidence Score.
- Toute affirmation invérifiable sur l'entité relève de l'hallucination extrinsèque et est notée au minimum à 2.
- Un sous-échantillon (≥ 15 % des réponses) est double-codé quand deux évaluateurs sont disponibles ; les désaccords de plus d'un point sont rediscutés.
- Distinguer toujours : observation (le score), suggestion (la tendance), interprétation (l'explication).

## 6. Formule finale (rappel)

```
Score sur 100 =
  25 × Mention Rate
+ 20 × Recommendation Rate
+ 15 × (Accuracy Score / 5)
+ 10 × (Source Evidence Score / 5)
+ 10 × (Entity Consistency Score / 5)
+ 10 × (Prompt Robustness Score / 5)
+  5 × (Multilingual Visibility Score / 5)
+  5 × (Sentiment Score / 5)

Pénalité = ajustement proportionnel à (Hallucination Score / 5)
appliqué sur la composante Accuracy avant agrégation.
```

---

*Cette grille fait partie du working paper « Mesurer la visibilité LLM des entités professionnelles marocaines » (DOI : 10.5281/zenodo.20820613). Réutilisation libre avec attribution (CC BY 4.0).*
