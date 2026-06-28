# LLM Visibility Morocco

**Recherche appliquée indépendante sur la visibilité des entités professionnelles marocaines dans les moteurs génératifs** (ChatGPT, Claude, Gemini, Perplexity, Copilot, Google AI Overviews).

> Applied research framework for measuring the visibility of Moroccan business entities in generative AI systems.

**Auteur :** Mohammed TETO — Consultant IA, SEO IA, AIO, GEO, Visibilité LLM (Casablanca, Maroc)
**Site :** [mohammedteto.com](https://mohammedteto.com) · **DOI :** [10.5281/zenodo.20820613](https://doi.org/10.5281/zenodo.20820613)
**Licence :** [CC BY 4.0](LICENSE)

---

## De quoi s'agit-il

La recherche d'information bascule des moteurs de recherche vers les moteurs de réponse. Pour une entreprise, une nouvelle question se pose : *quand une IA répond à la place de Google, suis-je cité — et correctement décrit ?*

Ce dépôt accompagne un **working paper** qui propose un cadre reproductible pour **mesurer, comparer et améliorer** la visibilité d'une entité professionnelle marocaine dans les réponses génératives. Il contient :

- une **matrice de 110 prompts** (8 catégories, 4 langues : FR / EN / arabe / darija) ;
- une **grille de scoring** sur 100 points (*LLM Visibility Score*) ;
- un **modèle de jeu de données** prêt à remplir ;
- un **script Python** de calcul du score ;
- le **framework COVE-LLM** (8 piliers d'optimisation) décrit dans le papier.

## Ce que ce dépôt n'est pas

Ce n'est ni une thèse, ni une publication validée par comité de lecture, ni une preuve définitive du fonctionnement interne des modèles. C'est une **recherche-pratique** menée par un praticien indépendant, conçue pour être reprise, exécutée et critiquée. **Aucun résultat de marché n'est inventé** : les sections de résultats sont des gabarits à remplir après collecte réelle.

## Structure

```
llm-visibility-morocco/
├── paper/
│   ├── visibilite-llm-maroc-recherche-appliquee.pdf   # working paper (34 p.)
│   └── visibilite-llm-maroc-recherche-appliquee.md    # source Markdown
├── prompts/
│   └── matrice-prompts.md                             # 110 prompts FR/EN/AR/DAR
├── methodology/
│   └── grille-scoring.md                              # LLM Visibility Score
├── datasets/
│   └── dataset-modele.csv                             # modèle (lignes d'exemple fictives)
├── scripts/
│   └── score_calculator.py                            # calcul du score (stdlib only)
├── LICENSE
└── README.md
```

## Démarrage rapide

```bash
python3 scripts/score_calculator.py datasets/dataset-modele.csv
```

Le script lit un CSV au format de `datasets/dataset-modele.csv` et calcule, par entité, le taux de mention, le taux de recommandation et le score global sur 100.

## Le framework COVE-LLM

Huit piliers, du plus interne au plus externe : **Clarté de l'entité · Cohérence publique · Autorité thématique · Preuves vérifiables · Validation tierce · Couverture des prompts · Accessibilité technique · Monitoring continu**. Détail et méthode d'application dans le working paper.

## Citation

```bibtex
@techreport{teto2026visibilitellm,
  author      = {Teto, Mohammed},
  title       = {Mesurer la visibilite LLM des entites professionnelles marocaines},
  year        = {2026},
  type        = {Working paper},
  number      = {v1.0},
  address     = {Casablanca, Maroc},
  doi         = {10.5281/zenodo.20820613},
  url         = {https://doi.org/10.5281/zenodo.20820613}
}
```

## Contribuer

Les retours méthodologiques, jeux de données anonymisés et réplications sont bienvenus via *issues* et *pull requests*. Merci de conserver la distinction entre observation, hypothèse, recommandation et limite.

---

*Working paper v1.0 — juin 2026. Réutilisation libre avec attribution (CC BY 4.0).*
