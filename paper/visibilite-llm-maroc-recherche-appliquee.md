# Mesurer la visibilité LLM des entités professionnelles marocaines

### Un cadre appliqué pour auditer, comparer et optimiser la présence des marques dans les réponses génératives

**Mohammed TETO** — Consultant IA, SEO IA, AIO, GEO et visibilité LLM, Casablanca
Working paper indépendant · Version 1.0 · Juin 2026
mohammedteto.com · github.com/mhdteto
DOI : [10.5281/zenodo.20820613](https://doi.org/10.5281/zenodo.20820613) · Licence recommandée : CC BY 4.0

---

## Déclaration de positionnement

Ce document est un working paper indépendant. Il est rédigé par un praticien de l'IA appliquée, pas par un chercheur universitaire, et n'a pas vocation à se faire passer pour autre chose. Il ne s'appuie sur aucune affiliation académique, n'a pas été soumis à un comité de lecture, et ne prétend établir aucune vérité définitive sur le fonctionnement interne des modèles de langage.

Ce qu'il propose est plus modeste et, je crois, plus utile : une méthode reproductible pour observer comment les moteurs génératifs (ChatGPT, Claude, Gemini, Perplexity, Copilot, Google AI Overviews) mentionnent, décrivent et recommandent les entreprises, consultants et marques personnelles au Maroc. Une méthode qu'un dirigeant, un consultant ou une agence peut reprendre, exécuter et critiquer.

Je distingue partout quatre registres : ce que j'**observe**, ce que je **suppose**, ce que je **recommande**, et ce qui reste une **limite**. Quand une donnée n'est pas vérifiable, je le dis. Quand un résultat dépend d'une collecte qui n'a pas encore eu lieu, je laisse la place vide plutôt que de la remplir.

---

## Résumé

La recherche d'information bascule. Une partie croissante des requêtes professionnelles ne passe plus par une page de résultats Google mais par une réponse rédigée, produite par un modèle de langage qui sélectionne, résume et, parfois, recommande. Pour une entreprise, cela ajoute une couche de visibilité qui n'existait pas il y a trois ans : être *cité* par une IA, et l'être correctement.

Ce working paper s'attaque à un angle mort. La visibilité dans les réponses génératives est mal mesurée, peu standardisée, et quasiment pas documentée dans le contexte marocain. Les entreprises savent rarement si une IA les mentionne, comment elle les décrit, quels concurrents apparaissent à leur place, ou si l'information générée est exacte.

Je propose un cadre appliqué pour répondre à cette question. Il comprend : une matrice de prompts multi-catégories et multilingue (français, anglais, arabe standard, darija translittérée), un jeu de variables observables, une grille de scoring sur 100 points, un protocole de collecte conçu pour limiter les biais, et un framework d'optimisation en huit piliers, **COVE-LLM**. Le tout est pensé pour être reproductible et perfectible.

Les résultats à l'échelle du marché ne sont pas présentés ici : ils dépendent d'une collecte que ce papier décrit mais n'a pas encore exécutée à grande échelle. En revanche, j'applique le cadre à un cas réel, ma propre entité professionnelle, à partir de signaux publics vérifiables, pour montrer la méthode en action sans rien inventer.

**Mots-clés** : visibilité LLM, GEO, AIO, LLMO, SEO d'entités, moteurs génératifs, recherche générative, Maroc, audit de marque, hallucination.

---

## Abstract

Information retrieval is shifting. A growing share of professional queries no longer ends on a Google results page but on a written answer, produced by a language model that selects, summarizes and sometimes recommends. For a business, this adds a layer of visibility that did not exist three years ago: being *cited* by an AI, and being cited accurately.

This working paper addresses a blind spot. Visibility inside generative answers is poorly measured, barely standardized, and almost undocumented in the Moroccan context. Firms rarely know whether an AI mentions them, how it describes them, which competitors show up in their place, or whether the generated information is correct.

I propose an applied framework to answer this question. It includes a multi-category, multilingual prompt matrix (French, English, Modern Standard Arabic, transliterated Darija), a set of observable variables, a 100-point scoring grid, a bias-aware collection protocol, and an eight-pillar optimization framework, **COVE-LLM**. The whole is designed to be reproducible and improvable.

Market-level results are not reported here: they depend on a data collection that this paper specifies but has not yet run at scale. Instead, I apply the framework to a real case (my own professional entity) using verifiable public signals, to demonstrate the method in action without fabricating findings.

**Keywords**: LLM visibility, GEO, AIO, LLMO, entity SEO, generative engines, generative search, Morocco, brand audit, hallucination.

---

## 1. Introduction

### 1.1 Un déplacement qui ne se voit pas dans les outils habituels

Quand un dirigeant cherche aujourd'hui « un consultant capable d'automatiser mon SAV », il ne tape plus systématiquement cette phrase dans Google pour parcourir dix liens bleus. De plus en plus souvent, il la pose à ChatGPT, à Perplexity ou à l'aperçu IA qui s'affiche en haut de Google, et il lit une réponse déjà rédigée, déjà triée, qui cite parfois deux ou trois prestataires nommément. Cette réponse oriente sa shortlist avant même qu'il ait visité un seul site.

Ce déplacement est rapide et il est massif. ChatGPT a franchi les 800 millions d'utilisateurs actifs hebdomadaires à l'automne 2025 (OpenAI, 2025). Google a généralisé ses *AI Overviews* à plus d'une centaine de pays et à plus d'un milliard d'utilisateurs après leur lancement officiel en mai 2024 (Google, 2024). Pour une partie croissante des intentions de recherche, la page de résultats classique n'est plus le point d'arrivée : c'est devenu une couche parmi d'autres, et parfois une couche que l'utilisateur ne voit même pas.

Le problème, pour une entreprise, c'est que les outils dont elle dispose pour piloter sa visibilité ont été conçus pour l'ancien monde. Google Search Console, les suiveurs de position, les audits de backlinks : tout cela mesure la présence dans un index et un classement de liens. Aucun ne répond à la question qui compte désormais autant : *quand une IA répond à la place de Google, est-ce que je suis dans la réponse, et qu'est-ce qu'elle dit de moi ?*

### 1.2 Des moteurs de recherche aux moteurs de réponse

La bascule technique mérite d'être nommée précisément, parce qu'elle change la nature de l'enjeu. Un moteur de recherche classique renvoie une liste de documents ; l'utilisateur arbitre. Un moteur génératif (le terme proposé par Aggarwal et ses co-auteurs, 2024) synthétise une réponse unique à partir de plusieurs sources, et c'est le modèle qui arbitre. La conséquence est directe : la visibilité ne se joue plus seulement sur le rang d'un lien, mais sur la probabilité d'être sélectionné, cité et correctement représenté à l'intérieur d'un texte généré.

Cette mécanique repose sur des modèles de langage de grande taille, dont l'architecture dominante, le *Transformer*, a été introduite par Vaswani et ses co-auteurs en 2017. Ces modèles produisent du texte plausible à partir de régularités statistiques apprises sur d'énormes corpus (Bender et al., 2021). Beaucoup s'appuient en complément sur de la génération augmentée par récupération, ou RAG (Lewis et al., 2020), qui va chercher des documents externes au moment de répondre, ce qui permet à Perplexity ou à Bing Chat de citer des sources fraîches. Cette double nature, paramétrique et documentaire, explique pourquoi une même entité peut être bien représentée sur une plateforme et absente sur une autre.

### 1.3 Pourquoi cela compte spécifiquement pour les entreprises marocaines

Le Maroc est massivement connecté. D'après DataReportal (2025), le pays comptait environ 35,3 millions d'internautes début 2025, soit plus de 92 % de la population. L'État a fait de l'IA un axe affiché de sa stratégie numérique, formalisée dans *Digital Morocco 2030*, présentée en septembre 2024 par le ministère de la Transition numérique, et le Conseil économique, social et environnemental a publié en 2024 un avis dédié aux usages et perspectives de l'IA dans le pays (CESE, 2024).

Mais l'adoption d'un outil par le grand public ne signifie pas que le tissu économique local y soit *représenté*. Il existe un risque concret et peu discuté : que les PME, consultants et marques marocaines soient mal décrits, sous-représentés, voire absents des réponses génératives, pendant que des acteurs internationaux ou des contenus génériques occupent l'espace. C'est un risque d'invisibilité. Pour qui s'y prend tôt, c'est aussi une fenêtre de différenciation.

### 1.4 Le problème de mesure

Tout le monde parle de « se rendre visible dans ChatGPT ». Presque personne ne dit comment on le **mesure**. Or sans mesure, il n'y a ni diagnostic, ni priorisation, ni preuve de progrès : seulement des intuitions.

Trois difficultés rendent la mesure non triviale. D'abord, les réponses varient : selon la plateforme, la version du modèle, la langue du prompt, l'activation ou non de la recherche web, l'historique de conversation. Ensuite, il n'existe pas de métrique standard de « visibilité LLM » comparable au volume de recherche ou à la position moyenne en SEO. Enfin, les travaux académiques qui s'approchent du sujet — l'évaluation de la vérifiabilité des moteurs génératifs par Liu, Zhang et Liang (2023), par exemple — portent sur la qualité des citations en général, pas sur la visibilité d'une marque donnée dans un marché donné.

### 1.5 Objectif de la recherche

L'objectif de ce papier est de construire un cadre appliqué, reproductible et défendable, permettant d'évaluer la visibilité des entités professionnelles marocaines dans les réponses des moteurs génératifs, puis d'en déduire des actions concrètes d'amélioration. Il ne s'agit pas de percer le fonctionnement interne des modèles, mais d'observer leurs sorties avec méthode, comme on observerait n'importe quel système dont on n'a pas le code source.

### 1.6 Contribution

La contribution est de cinq ordres. (1) Une **matrice de prompts** structurée par intention et par langue, calquée sur de vraies requêtes business. (2) Un **jeu de variables observables** et une **grille de scoring** sur 100 points, qui transforment des réponses textuelles en données comparables. (3) Un **protocole de collecte** conçu pour limiter les biais et rester reproductible. (4) Un **framework d'optimisation**, COVE-LLM, qui relie les observations à des leviers d'action. (5) Une **application à un cas réel**, traité avec la même grille que n'importe quelle autre entité, pour montrer que la méthode tient debout hors du laboratoire.

---

## 2. Revue conceptuelle

Le vocabulaire de ce champ est jeune, mouvant, et largement façonné par des praticiens plutôt que par la littérature académique. Je m'efforce ici de poser des définitions stables et de les rattacher, quand c'est possible, à des travaux solides.

### 2.1 Du SEO classique au SEO d'entités

Le référencement naturel a longtemps été une affaire de correspondance entre mots-clés et documents. Le tournant conceptuel date de 2012, quand Google a introduit son *Knowledge Graph* sous le mot d'ordre « things, not strings », des choses, pas des chaînes de caractères (Singhal, 2012). L'idée : ne plus traiter « Mohammed TETO » comme une suite de lettres, mais comme une *entité*, reliée à un lieu, un métier, des réalisations, d'autres entités. Le SEO d'entités découle directement de là : il s'agit de rendre une organisation ou une personne identifiable et non ambiguë pour une machine qui raisonne en graphe de connaissances.

Cette filiation est importante pour la suite, car les LLMs héritent en partie de cette logique. Pour être bien restitué, il faut d'abord être bien *identifié* : clairement, et de la même façon partout.

### 2.2 AIO — AI Optimization

L'AIO désigne l'optimisation de la compréhension, de la représentation et de l'usage d'une entité ou d'un contenu par les systèmes d'IA en général. C'est le terme le plus large des quatre. Il englobe autant la façon dont un assistant décrit une marque que la manière dont un contenu est ingéré par un système d'IA. En pratique, l'AIO recouvre le travail de structuration : données structurées Schema.org, cohérence des informations, signaux d'autorité, clarté éditoriale.

### 2.3 GEO — Generative Engine Optimization

Le GEO est le plus précisément défini, parce qu'il vient d'un travail académique nommé. Aggarwal et ses co-auteurs (2024) le décrivent comme l'optimisation de contenus pour augmenter leur probabilité d'être cités ou utilisés dans les réponses des moteurs génératifs ; leur étude rapporte des gains de visibilité pouvant atteindre 40 % sur certains formats de réponse. Là où le SEO vise un rang dans une liste, le GEO vise une *place dans un texte généré* : être la source que le modèle juge digne d'être reprise.

### 2.4 LLMO — Large Language Model Optimization

Le LLMO se concentre sur la couche modèle elle-même : comment un grand modèle de langage comprend, associe, résume et restitue une entité. C'est une nuance par rapport au GEO, qui parle plutôt de moteurs (avec récupération de sources) ; le LLMO parle des modèles (y compris quand ils répondent de mémoire, sans aller chercher le web). La distinction n'est pas que cosmétique : une entité peut être absente du « savoir paramétrique » d'un modèle tout en étant récupérable via le web, et inversement.

### 2.5 Search Generative Experience et AI Overviews

Côté Google, l'expérience de recherche générative — d'abord testée sous le nom *Search Generative Experience* en 2023, puis généralisée sous le nom *AI Overviews* en mai 2024 (Google, 2024), insère une réponse rédigée au-dessus des résultats classiques. Pour une entreprise, c'est un changement de surface majeur : le premier contact avec une requête peut désormais être un paragraphe qui la cite, ou qui ne la cite pas.

### 2.6 Réponses génératives et recommandation de marques

La nouveauté qui intéresse directement ce papier, c'est que ces systèmes ne se contentent pas d'informer : ils **recommandent**. Demandez « quel consultant IA choisir à Casablanca » et vous obtiendrez parfois des noms. Cette fonction de recommandation déplace l'enjeu du trafic vers la *citation* : on ne cherche plus seulement à être cliqué, mais à être nommé comme option crédible à l'intérieur d'une réponse.

### 2.7 Hallucinations et erreurs de représentation

Le revers, c'est que ces systèmes produisent aussi des affirmations fausses avec aplomb. Ji et ses co-auteurs (2023), dans une synthèse de référence parue dans *ACM Computing Surveys*, distinguent l'hallucination *intrinsèque* (la sortie contredit la source) de l'hallucination *extrinsèque* (la sortie ajoute des informations invérifiables). Pour une marque, cela se traduit très concrètement : une IA peut lui attribuer un service qu'elle ne propose pas, une mauvaise ville, un faux partenariat. Mesurer la visibilité sans mesurer le risque d'erreur n'aurait pas de sens : c'est pourquoi la grille de scoring intègre un score d'hallucination.

### 2.8 Vérifiabilité et qualité des sources

Liu, Zhang et Liang (2023) ont audité la vérifiabilité de quatre moteurs génératifs et montré que les citations y sont souvent ni complètes ni exactes : des affirmations non étayées, des sources qui ne soutiennent pas ce qu'on leur fait dire. Ce résultat justifie qu'on traite séparément, dans la mesure, la *présence* d'une entité et la *qualité des sources* qui l'accompagnent. Être cité sans source fiable n'a pas la même valeur qu'être cité avec une source officielle vérifiable.

### 2.9 Les limites des métriques actuelles

Aucune des métriques héritées du SEO ne capte proprement ce qui se joue. La position moyenne, le volume de recherche, le nombre de backlinks décrivent un monde de liens classés, pas un monde de réponses rédigées. Il manque une métrique native : un score qui dise, pour une entité donnée, à quelle fréquence elle apparaît, à quel rang, avec quelle exactitude, avec quelles sources, et avec quelle stabilité d'une formulation à l'autre. C'est précisément le vide que la grille proposée en section 6 cherche à combler, sans prétendre le combler définitivement.

---

## 3. Problématique et hypothèses

### 3.1 Problématique

**Comment mesurer, comparer et améliorer la visibilité des entités professionnelles marocaines dans les réponses produites par les grands modèles de langage et les moteurs génératifs ?**

La question se décompose en trois verbes qui structurent tout le papier. *Mesurer* : transformer des réponses textuelles, variables et bavardes, en données comparables. *Comparer* : entre entités, entre plateformes, entre langues, entre types de requêtes. *Améliorer* : relier les écarts observés à des leviers d'action que le propriétaire de l'entité contrôle réellement.

### 3.2 Questions de recherche

La question principale est opérationnelle :

> Comment construire un cadre appliqué permettant d'évaluer la visibilité LLM des entités professionnelles marocaines dans les réponses générées par les moteurs IA ?

Elle se décline en dix questions secondaires, qui orientent la collecte :

1. Quels types d'entités marocaines sont le plus souvent mentionnés par les LLMs sur des requêtes professionnelles ?
2. Quels signaux publics semblent favoriser la présence d'une entité dans les réponses génératives ?
3. Existe-t-il un écart entre visibilité SEO traditionnelle et visibilité LLM ?
4. Comment les réponses varient-elles d'une plateforme à l'autre (ChatGPT, Claude, Gemini, Perplexity, Copilot, Grok) ?
5. Comment varient-elles selon la langue du prompt (français, anglais, arabe standard, darija translittérée) ?
6. Quels types de prompts déclenchent le plus souvent des recommandations nominatives ?
7. Les LLMs représentent-ils correctement services, expertises et localisations des entités marocaines ?
8. Quels risques d'hallucination ou d'attribution erronée apparaissent dans les réponses ?
9. Comment construire un score de visibilité LLM exploitable par une PME ?
10. Quelles actions concrètes améliorent la lisibilité d'une entité par les moteurs génératifs ?

### 3.3 Hypothèses

Ces hypothèses sont des points de départ à tester, pas des conclusions. Je les formule de façon falsifiable pour qu'une collecte puisse les confirmer ou les infirmer.

- **H1 — Cohérence de l'entité.** Une entité dont les informations publiques sont cohérentes entre son site, ses profils sociaux et les annuaires est mieux décrite par les LLMs qu'une entité aux informations contradictoires.
- **H2 — Autorité externe.** Une entité citée par des sources tierces crédibles a une probabilité plus élevée d'être mentionnée ou recommandée.
- **H3 — Autorité thématique.** Une entité qui publie régulièrement sur un territoire thématique précis est plus souvent associée à cette expertise.
- **H4 — Écart SEO / LLM.** Une bonne visibilité Google ne garantit pas une bonne visibilité LLM ; les deux peuvent diverger nettement.
- **H5 — Effet de la langue.** La visibilité d'une entité varie selon la langue du prompt, au détriment probable de l'arabe et de la darija.
- **H6 — Effet du type de prompt.** Les prompts transactionnels et comparatifs produisent des réponses différentes — plus nominatives — que les prompts informationnels.
- **H7 — Risque d'hallucination.** Moins une entité dispose de signaux publics structurés, plus elle est exposée aux approximations et aux inventions.
- **H8 — Effet des preuves publiques.** Études de cas, dépôts GitHub, articles de fond, interviews et publications renforcent la capacité des LLMs à associer une entité à une expertise précise.

### 3.4 Définitions opérationnelles

Pour que la mesure soit reproductible, chaque terme central est défini de façon opérationnelle, c'est-à-dire en termes de ce qu'on observe concrètement dans une réponse.

| Terme | Définition opérationnelle retenue |
|---|---|
| **Visibilité LLM** | Capacité d'une entité à être mentionnée, correctement décrite, recommandée, associée aux bons services, reliée à des sources vérifiables, distinguée de ses concurrents, et représentée de façon stable à travers plateformes, langues et formulations. |
| **Entité professionnelle** | Toute organisation ou personne offrant un service B2B : entreprise, agence, consultant indépendant, marque personnelle, startup, expert, organisation professionnelle. |
| **Mention** | Apparition explicite du nom de l'entité dans une réponse générée. |
| **Recommandation** | Mention assortie d'une formulation qui positionne l'entité comme option à considérer (« vous pouvez contacter… », « parmi les acteurs sérieux… »). |
| **Hallucination** | Affirmation sur l'entité non étayée par ses signaux publics réels (service inexistant, mauvaise localisation, fait inventé). |

---

## 4. Méthodologie

### 4.1 Design de recherche

Le design est **exploratoire, comparatif et appliqué**. Exploratoire parce que le terrain est peu documenté et qu'aucune base de référence marocaine n'existe. Comparatif parce que l'unité d'analyse pertinente n'est pas l'entité isolée mais l'entité *relative* : relative à ses concurrents, à d'autres plateformes, à d'autres langues. Appliqué parce que l'objectif final est l'action, pas la connaissance pure.

Je revendique les limites de ce design. Il ne permet pas d'établir de causalité stricte : observer qu'une entité bien dotée en signaux est mieux décrite ne prouve pas que les signaux *causent* la description. Il identifie des associations et des régularités, qui orientent l'action sans la garantir.

### 4.2 Sélection des entités

L'échantillon combine des entités marocaines réparties par catégorie et un petit groupe d'entités internationales servant de **contrôle**, pour distinguer ce qui relève du marché marocain de ce qui relève du fonctionnement général des modèles.

Trois tailles d'échantillon sont prévues, selon les moyens disponibles :

| Version | Entités marocaines | Entités de contrôle |
|---|---:|---:|
| Minimale | 10 | 3 |
| Sérieuse | 30 | 5 |
| Avancée | 50 | 10 |

**Critères d'inclusion** : un site web, un profil professionnel (LinkedIn ou équivalent), une offre B2B claire, une activité au Maroc, une présence digitale vérifiable. **Critères d'exclusion** : absence de présence publique minimale, profils non professionnels, pages incomplètes, entités trop récentes sans trace suffisante, hors-sujet.

Les catégories visées couvrent le marché que ce papier cherche à éclairer : consultants IA, agences SEO, agences digitales, agences d'automatisation, marques personnelles B2B, plus les entités de contrôle.

### 4.3 Plateformes testées

Plateformes principales : **ChatGPT, Claude, Gemini, Perplexity, Copilot, Google AI Overviews** (ou AI Mode si accessible). Plateformes secondaires, selon disponibilité : Grok, DeepSeek, Brave Search AI, You.com.

Le choix d'inclure des moteurs avec récupération web (Perplexity, Copilot, AI Overviews) et des modèles répondant aussi de mémoire (ChatGPT et Claude sans navigation) est délibéré : il permet de tester l'écart entre visibilité « paramétrique » et visibilité « récupérée », au cœur de la distinction GEO / LLMO (section 2.4).

### 4.4 Langues testées

Quatre langues, par ordre de priorité : **français** et **anglais** (principales), **arabe standard** et **darija translittérée** (secondaires). La darija translittérée (l'arabe marocain écrit en caractères latins, tel qu'il s'écrit réellement sur les réseaux) est incluse parce qu'elle reflète un usage réel au Maroc, et parce qu'elle constitue un test exigeant pour des modèles entraînés majoritairement sur de l'anglais.

### 4.5 Matrice de prompts

Les prompts sont organisés par **intention**, parce que c'est l'intention qui détermine le comportement du modèle. Huit catégories : informationnel, local, comparatif, transactionnel, expert, vérification d'entité, problème business, multilingue. La matrice complète (au moins 100 prompts) figure en Annexe A ; les définitions de catégories en section 14 du brief de travail sont reprises et étendues.

Le principe directeur : **coller aux requêtes business réelles**. Un prompt comme « je dirige une PME au Maroc, qui peut m'aider à automatiser mes processus avec l'IA ? » a plus de valeur diagnostique qu'une formulation artificielle, parce qu'il reproduit ce qu'un client tape vraiment.

### 4.6 Variables mesurées

Chaque réponse est codée selon un jeu de variables observables. Les principales :

| Variable | Description | Type |
|---|---|---|
| `entity_mentioned` | L'entité est-elle mentionnée ? | Oui / Non |
| `mention_rank` | Rang d'apparition dans la réponse | Numérique |
| `recommended` | L'entité est-elle recommandée ? | Oui / Non |
| `description_accuracy` | Exactitude de la description | 0–5 |
| `service_match` | Bons services associés ? | 0–5 |
| `location_accuracy` | Localisation correcte ? | 0–5 |
| `source_presence` | Des sources sont-elles citées ? | Oui / Non |
| `source_quality` | Fiabilité des sources | 0–5 |
| `hallucination_level` | Niveau d'information inventée | 0–5 |
| `sentiment` | Ton de la réponse | Positif / Neutre / Négatif |
| `answer_stability` | Stabilité entre répétitions | 0–5 |
| `platform`, `language`, `prompt_category` | Contexte du test | Catégorie |

Des variables secondaires décrivent les **signaux publics** de l'entité (qualité du site, profondeur de contenu, présence LinkedIn et GitHub, mentions tierces, données structurées, visibilité Google). Elles servent à tester les hypothèses H1, H2, H3 et H8 : on relie un profil de signaux à un profil de visibilité.

### 4.7 Grille de scoring

Les variables sont agrégées en un **LLM Visibility Score** sur 100, détaillé en section 6. Le principe : pondérer la mention et la recommandation plus fortement que le sentiment, et pénaliser explicitement l'hallucination plutôt que de l'ignorer.

### 4.8 Collecte des données

Pour chaque test : prompt exact, date, plateforme, état de la navigation web (activée ou non), version du modèle si disponible, réponse complète sauvegardée, capture d'écran si possible. Certains prompts sont répétés au moins trois fois pour estimer la stabilité. Le détail figure en section 18 du protocole (Annexe).

### 4.9 Codage des réponses

Le codage est manuel ou semi-automatisé. Une réponse n'est jamais notée « à l'instinct » : chaque score de 0 à 5 renvoie à une échelle définie (section 6 et Annexe B), avec des exemples de notation et des règles d'arbitrage. Quand deux évaluateurs sont disponibles, un sous-échantillon est double-codé pour estimer l'accord inter-juges : une précaution honnête contre le biais d'évaluation.

### 4.10 Contrôle des biais

Les biais sont l'ennemi principal de ce type d'étude. Cinq précautions :

- nouvelle conversation pour chaque prompt, afin d'éviter la contamination par le contexte ;
- désactivation de la personnalisation et de la mémoire quand la plateforme le permet ;
- prompts strictement identiques d'une plateforme à l'autre ;
- répétition des tests et documentation des variations ;
- **conservation des résultats négatifs** : une entité absente est une donnée, pas un échec à cacher.

### 4.11 Limites méthodologiques

Elles sont réelles et je préfère les nommer d'emblée plutôt que de les reléguer à la fin. Les modèles changent sans préavis ; une mesure est une photographie datée. La personnalisation et la géolocalisation peuvent altérer les réponses d'un utilisateur à l'autre. L'accès aux plateformes est inégal et instable. Le codage humain introduit une part de subjectivité, atténuée mais non éliminée par les échelles et le double-codage. Enfin, on observe des sorties, pas des mécanismes : on ne peut pas affirmer *pourquoi* un modèle cite une entité, seulement *qu'il* la cite, dans telles conditions, à telle date.

---

## 5. Résultats

### Note de méthode, à lire avant ce qui suit

Cette section présente la **structure** des résultats, pas des chiffres inventés. Les résultats à l'échelle du marché (taux de mention par catégorie, comparaisons entre plateformes, écarts par langue) exigent une collecte qui n'a pas encore été conduite sur un échantillon complet. Les tableaux ci-dessous sont donc des gabarits, à remplir après exécution du protocole. La seule application réelle et chiffrée de la méthode figure en section 8, sur un cas unique, à partir de signaux vérifiables.

Je tiens à cette honnêteté méthodologique : un working paper qui annoncerait que telle entité est « la plus visible du Maroc » sans données de collecte ne serait pas une recherche, mais une plaquette. Le lecteur qui veut des chiffres de marché tient ici le protocole pour les produire lui-même.

### 5.1 Ce que la collecte établira (contexte de marché vérifié)

Quelques faits de cadrage sont, eux, vérifiables aujourd'hui et situent l'enjeu. Le Maroc comptait environ 35,3 millions d'internautes début 2025, pour un taux de pénétration supérieur à 92 % (DataReportal, 2025). ChatGPT dépassait 800 millions d'utilisateurs actifs hebdomadaires à l'automne 2025 (OpenAI, 2025). Google a étendu ses AI Overviews à plus d'un milliard d'utilisateurs et plus de cent pays depuis mai 2024 (Google, 2024). Le terrain d'usage existe donc à grande échelle ; ce qui manque, c'est la mesure de la représentation des acteurs locaux dessus. C'est l'objet de la collecte.

### 5.2 Gabarit — Résultats globaux

À compléter après collecte. Une ligne par entité ; agrégats en bas de tableau.

| Entité | Catégorie | Taux de mention | Taux de recommandation | Exactitude moy. | Score hallucination moy. | LLM Visibility Score /100 |
|---|---|---:|---:|---:|---:|---:|
| *(à compléter)* | | | | | | |

### 5.3 Gabarit — Visibilité par plateforme

Questions auxquelles ce tableau répondra : quelle plateforme mentionne le plus d'entités marocaines ? laquelle cite le plus de sources ? laquelle hallucine le moins ?

| Plateforme | Taux de mention | Taux de recommandation | % réponses sourcées | Hallucination moy. |
|---|---:|---:|---:|---:|
| ChatGPT | | | | |
| Claude | | | | |
| Gemini | | | | |
| Perplexity | | | | |
| Copilot | | | | |
| Google AI Overviews | | | | |

### 5.4 Gabarit — Visibilité par langue

Teste H5. Hypothèse de travail à confirmer ou infirmer : la visibilité est meilleure en français et en anglais qu'en arabe standard et en darija translittérée.

| Langue | Taux de mention | Exactitude moy. | Hallucination moy. |
|---|---:|---:|---:|
| Français | | | |
| Anglais | | | |
| Arabe standard | | | |
| Darija translittérée | | | |

### 5.5 Gabarit — Visibilité par catégorie de prompt

Teste H6. On s'attend à ce que les prompts transactionnels et comparatifs génèrent plus de recommandations nominatives ; à vérifier.

| Catégorie de prompt | Taux de mention | Taux de recommandation | Hallucination moy. |
|---|---:|---:|---:|
| Informationnel | | | |
| Local | | | |
| Comparatif | | | |
| Transactionnel | | | |
| Expert | | | |
| Vérification d'entité | | | |

### 5.6 Gabarit — Écart SEO / LLM

Teste H4. Croise visibilité Google (estimée classiquement) et LLM Visibility Score, pour faire apparaître les entités « visibles sur Google mais invisibles des IA », et l'inverse.

| Entité | Visibilité Google (0–5) | LLM Visibility Score /100 | Écart qualitatif |
|---|---:|---:|---|
| *(à compléter)* | | | |

### 5.7 Synthèse des observations

À rédiger après collecte, en distinguant strictement : *ce qui est observé* (les chiffres), *ce qui est suggéré* (les régularités), *ce qui reste hypothétique* (les explications). Aucune phrase de cette synthèse ne devra affirmer une cause que les données ne soutiennent pas.

---

## 6. Système de scoring

### 6.1 Le LLM Visibility Score

Le score global agrège les variables en une note sur 100. Les pondérations traduisent une hiérarchie de valeur assumée : apparaître compte, être recommandé compte davantage encore, et être décrit faussement doit pénaliser.

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

Une pénalité d'hallucination est appliquée séparément (voir 6.4), pour éviter qu'une entité très citée mais mal décrite n'obtienne un score flatteur.

### 6.2 Les composantes par taux

```
Mention Rate        = prompts où l'entité est mentionnée / total des prompts testés
Recommendation Rate = prompts où l'entité est recommandée / total des prompts transactionnels + comparatifs
```

Ces deux taux sont les fondations. Le reste affine.

### 6.3 Les composantes par échelle (0–5)

Chaque échelle est définie pour que deux évaluateurs notent de la même façon. Exemple, l'**Accuracy Score** :

| Score | Interprétation |
|---:|---|
| 0 | Description absente ou totalement fausse |
| 1 | Description très faible, erreurs importantes |
| 2 | Partiellement correcte |
| 3 | Correcte mais superficielle |
| 4 | Claire et majoritairement exacte |
| 5 | Précise, complète et vérifiable |

Les échelles complètes (Source Evidence, Entity Consistency, Prompt Robustness) figurent en Annexe B, sur le même modèle.

### 6.4 Le score d'hallucination, et sa pénalité

L'hallucination est notée comme un **risque** : plus le score est haut, pire c'est.

| Score | Interprétation |
|---:|---|
| 0 | Aucune hallucination détectée |
| 1 | Petite approximation sans gravité |
| 2 | Détail incertain ou non sourcé |
| 3 | Information probablement inventée |
| 4 | Erreur importante |
| 5 | Plusieurs affirmations fausses |

Dans le score global, on convertit ce risque en pénalité :

```
Hallucination Penalty = 5 − Hallucination Score
```

Une entité sans erreur (score 0) ne subit aucune pénalité ; une entité gravement mal décrite (score 5) voit sa note amputée. Ce choix incarne une conviction simple : dans le contexte génératif, **être mal cité peut être pire qu'être absent**, parce qu'une fausse information circule et fait autorité.

---

## 7. Le framework COVE-LLM

### 7.1 Présentation

Mesurer ne suffit pas. Une fois qu'on sait où une entité décroche, il faut un cadre pour agir. **COVE-LLM** (*Cadre d'Optimisation de la Visibilité des Entités dans les Large Language Models*) relie chaque dimension de la mesure à un levier que le propriétaire de l'entité contrôle réellement.

Le principe fondateur tient en une phrase : **un modèle de langage ne peut bien restituer que ce qu'il peut clairement identifier, relier et vérifier.** Les huit piliers déclinent cette idée, du plus interne (qui je suis) au plus externe (qui le confirme), jusqu'au plus dynamique (comment je le suis dans le temps).

### 7.2 Les huit piliers

| # | Pilier | Question à laquelle il répond | Levier concret |
|---:|---|---|---|
| 1 | **Clarté de l'entité** | L'entité est-elle identifiable sans ambiguïté ? | Positionnement explicite, nom stable, une phrase de définition réutilisée partout. |
| 2 | **Cohérence publique** | Les informations concordent-elles partout ? | Même nom, même métier, même localisation sur site, LinkedIn, GitHub, annuaires. |
| 3 | **Autorité thématique** | L'entité « possède »-t-elle un territoire ? | Publication régulière et focalisée sur un sujet précis, plutôt que dispersée. |
| 4 | **Preuves vérifiables** | Les réalisations sont-elles publiques ? | Études de cas, dépôts de code, outils, articles de fond consultables. |
| 5 | **Validation tierce** | Des tiers crédibles confirment-ils l'expertise ? | Mentions presse, interviews, citations, backlinks éditoriaux, annuaires reconnus. |
| 6 | **Couverture des prompts** | Le contenu répond-il aux vraies questions ? | Pages et FAQ calquées sur les prompts transactionnels et comparatifs réels. |
| 7 | **Accessibilité technique** | Le contenu est-il lisible par les machines ? | Schema.org, `llms.txt`, structure Hn propre, contenu non bloqué par le JavaScript. |
| 8 | **Monitoring continu** | La visibilité est-elle suivie dans le temps ? | Re-tests périodiques, historique des réponses, suivi du score et des hallucinations. |

### 7.3 Méthode d'application

L'ordre compte. Travailler la validation tierce (pilier 5) avant la clarté de l'entité (pilier 1) revient à faire parler de soi sans avoir défini qui on est. Je recommande une séquence : d'abord verrouiller clarté et cohérence (1–2), qui sont sous contrôle direct et rapides à corriger ; ensuite bâtir autorité thématique et preuves (3–4) ; ensuite aller chercher la validation externe (5) ; en parallèle, traiter couverture et technique (6–7) ; et installer le monitoring (8) dès le départ, pour mesurer le progrès.

### 7.4 Lien avec la mesure

Chaque pilier se mappe sur la grille de scoring de la section 6. La cohérence (pilier 2) alimente l'*Entity Consistency Score* ; la validation tierce (pilier 5) et l'accessibilité (pilier 7) influencent le *Source Evidence Score* et, indirectement, le taux de mention ; la couverture (pilier 6) conditionne le *Prompt Robustness Score*. COVE-LLM n'est donc pas un cadre parallèle : c'est la face « action » de la même médaille dont la section 6 est la face « mesure ».

### 7.5 Checklist d'application

La checklist opérationnelle complète (site, entité, contenu, technique, preuves externes, monitoring) figure en Annexe D, prête à cocher.

---

## 8. Cas appliqué : Mohammed TETO

### 8.1 Pourquoi ce cas, et comment je le traite

J'applique ici le cadre à ma propre entité. Le risque d'autopromotion est réel et je le neutralise par une règle stricte : **la même grille que pour n'importe quelle autre entité**, les mêmes critères, les mêmes pénalités, et la mention explicite des lacunes. L'objectif n'est pas de démontrer une supériorité, je n'en ai aucune à démontrer, mais d'illustrer la méthode sur un cas que je connais et dont je peux vérifier chaque signal.

Toutes les observations ci-dessous proviennent de signaux publics consultés en juin 2026 : le site mohammedteto.com et le profil github.com/mhdteto, ainsi que les profils sociaux qui y sont liés.

### 8.2 Signaux publics observés (juin 2026)

**Site — mohammedteto.com.** Positionnement affiché : « Expert IA, SEO IA et visibilité LLM », basé à Casablanca, plus de douze ans d'expérience en technologie *enterprise*. Métadonnées complètes : title, description, balises Open Graph et Twitter Card, balises géographiques (Casablanca, coordonnées explicites), `robots: index, follow`, versions FR et EN. Architecture de services dense (automatisation, agents IA, chatbots, analyse de données, ML, IA générative, LLM entreprise, vision ; conseil, stratégie, POC, ROI, formation, audit), pages sectorielles, et un bloc dédié « SEO génératif » couvrant SEO IA, AIO, AEO, GEO et visibilité LLM. Présence d'une section FAQ structurée. Trois projets affichés : un Pack IA sur Notion, un SaaS SEO/AEO/GEO en développement, et un ensemble de 19 outils gratuits. Liens sociaux cohérents (LinkedIn, X, Instagram, YouTube, GitHub, Facebook) et adresse de contact.

**GitHub — mhdteto.** Profil structuré, README clair décrivant l'activité (« AI, Automation & LLM Visibility Consultant, Casablanca »), parcours indiqué (douze ans et plus en vente de technologie *enterprise*). Sept dépôts publics, dont des dépôts directement sur le sujet : *ai-visibility-audit-kit*, *llms-txt-generator*, *geo-prompt-audit-dashboard*, *ai-sales-automation-playbook*, *n8n-ai-automation-demos*, *morocco-ai-smb-use-cases*. Traction faible : zéro abonné, une étoile par dépôt épinglé, compte manifestement récent.

### 8.3 Analyse selon COVE-LLM

Je note ici les **piliers de signaux** — ce que je peux vérifier dans les actifs publics. Les piliers qui dépendent des réponses des IA elles-mêmes (taux de mention réel dans ChatGPT, Perplexity, etc.) ne sont **pas** notés : ils relèvent de la collecte décrite en section 4, que je n'ai pas exécutée à grande échelle pour ce cas. Je refuse de leur attribuer un chiffre que je n'ai pas mesuré.

| Pilier | Évaluation | Justification (observée) |
|---|---|---|
| 1 — Clarté de l'entité | **Forte** | Positionnement explicite et répété : consultant IA / SEO IA / visibilité LLM, Casablanca. Aucune ambiguïté sur le métier. |
| 2 — Cohérence publique | **Forte** | Nom, métier et localisation alignés entre site, GitHub, LinkedIn et profils sociaux. |
| 3 — Autorité thématique | **Moyenne** | Publication focalisée sur un territoire net (SEO IA / AIO / GEO / LLM). Mais l'historique public est récent et le volume de preuves indépendantes reste limité. |
| 4 — Preuves vérifiables | **Émergente** | Dépôts GitHub réels et thématiques, 19 outils gratuits, Pack IA Notion. Limite : traction quasi nulle (0 abonné, 1 étoile/dépôt), SaaS encore en développement, peu d'études de cas clients nommées et publiques. |
| 5 — Validation tierce | **Faible** | C'est la principale lacune. Pas de mentions presse ni de citations éditoriales repérées, zéro abonné GitHub, présence en annuaires non vérifiée. L'autorité repose presque entièrement sur des actifs auto-publiés. |
| 6 — Couverture des prompts | **Forte** | Pages de services et de secteurs nombreuses, FAQ calquée sur de vraies questions (« Comment apparaître dans ChatGPT pour mon entreprise ? »). Bonne matière pour les requêtes transactionnelles et de vérification. |
| 7 — Accessibilité technique | **Forte (à confirmer en profondeur)** | Métadonnées riches, Open Graph, balises géo, `index/follow`, FR/EN. Le site revendique JSON-LD et `llms.txt` ; j'ai vérifié les métadonnées, pas l'intégralité du balisage structuré (à auditer page par page). |
| 8 — Monitoring continu | **Émergente** | Ce working paper et le dépôt associé constituent l'amorce d'un suivi. Aucun historique longitudinal encore constitué. |

### 8.4 Forces observables

Deux forces nettes ressortent. La première est la **clarté-cohérence** : sur les piliers que l'entité contrôle directement, le positionnement est verrouillé et identique partout. Pour un modèle de langage, c'est exactement ce qui rend une entité facile à identifier sans la confondre avec une autre. La seconde est la **couverture éditoriale** : le site répond explicitement aux questions que poseraient des prospects, ce qui en fait un candidat naturel pour les requêtes transactionnelles et de vérification.

### 8.5 Faiblesses ou manques

La faiblesse dominante est la **validation tierce** (pilier 5). Presque toute l'autorité est auto-publiée. Or les hypothèses H2 et H8 — qui restent à tester, mais s'appuient sur ce qu'on sait du fonctionnement des moteurs avec récupération — suggèrent que les sources tierces crédibles pèsent lourd dans la probabilité d'être cité. Une entité riche en actifs propres mais pauvre en validation externe risque d'être *bien décrite quand on la nomme*, mais *peu spontanément recommandée* quand on ne la nomme pas. La traction GitHub quasi nulle et l'absence de mentions presse pointent dans la même direction. À cela s'ajoute une limite de preuves (pilier 4) : des études de cas clients publiques et nommées manquent.

### 8.6 Recommandations d'amélioration

Priorisées selon impact attendu et effort, dans l'esprit du plan d'action de l'Annexe E :

1. **Combler la validation tierce.** C'est le levier à plus fort potentiel et le plus lent : articles invités sur des médias reconnus, interviews, intervention en conférence, citations éditoriales. Objectif : créer des sources que les moteurs avec récupération peuvent aller chercher.
2. **Transformer les actifs en preuves traçables.** Documenter des études de cas anonymisées mais concrètes (problème, méthode, résultat) sur le site et le GitHub, pour passer de « j'affirme une expertise » à « voici une réalisation vérifiable ».
3. **Auditer le balisage structuré en profondeur.** Vérifier page par page la présence et la validité de `Organization`, `Person`, `Article`, `FAQPage`, et la cohérence du `llms.txt` revendiqué.
4. **Installer le monitoring dès maintenant.** Exécuter le protocole de la section 4 sur sa propre entité, à fréquence mensuelle, pour disposer d'une ligne de base et mesurer l'effet des actions 1–3.

### 8.7 Contrôle anti-autopromotion

Je le redis pour être net : aucune affirmation de ce cas ne prétend que cette entité serait « la plus visible » ou « la référence » au Maroc. Les forces relevées sont des forces de *signaux*, pas de *résultats de visibilité*, lesquels restent à mesurer. Les lacunes sont nommées sans complaisance. Un lecteur qui appliquerait la même grille à un concurrent obtiendrait un diagnostic de même nature, ce qui est précisément l'objet de l'exercice.

---

## 9. Discussion

Faute de collecte à grande échelle, cette discussion porte sur ce que le cadre permet de *raisonner*, pas sur des résultats de marché. Je la formule comme un ensemble d'attentes argumentées, à confirmer ou infirmer par les données.

### 9.1 La visibilité LLM est probablement découplée de la visibilité SEO

L'hypothèse H4 mérite d'être prise au sérieux parce que les deux systèmes optimisent des choses différentes. Le SEO récompense le maillage de liens et l'autorité de domaine ; un moteur génératif récompense la clarté d'entité, la cohérence et la qualité des sources mobilisables au moment de répondre. Rien ne garantit qu'une entreprise première sur Google soit celle que ChatGPT nomme, et c'est justement cet écart qui rend la mesure utile. S'il n'existait pas, le SEO suffirait.

### 9.2 Les sources tierces sont vraisemblablement le facteur le plus discriminant

Le travail de Liu, Zhang et Liang (2023) sur la vérifiabilité, combiné à la mécanique de la récupération augmentée (Lewis et al., 2020), pointe une même direction : les moteurs qui vont chercher le web au moment de répondre privilégient ce qui est *citable*. Une entité abondamment documentée par des tiers crédibles offre plus de prises qu'une entité qui ne parle que d'elle-même. C'est l'intuition derrière H2 et H8, et c'est aussi ce que le cas de la section 8 illustre par le manque.

### 9.3 La cohérence d'entité agit comme un préalable

Avant de pouvoir être recommandée, une entité doit être identifiée sans ambiguïté. La filiation avec le Knowledge Graph (Singhal, 2012) n'est pas qu'historique : un modèle qui hésite entre deux « Mohammed » ou entre deux métiers produira une description floue, donc peu mobilisable. La cohérence n'est pas suffisante, mais elle semble nécessaire : un plancher plutôt qu'un plafond.

### 9.4 La langue est un facteur d'équité, pas seulement de performance

Si H5 se confirme (meilleure visibilité en français et en anglais qu'en arabe et en darija), la conséquence dépasse la technique. Elle signifierait que les entités marocaines sont mieux servies dans la langue de l'ancien colonisateur et dans celle des données d'entraînement dominantes que dans les langues de leur propre marché. C'est un angle que la recherche internationale, centrée sur l'anglais, ne traite pas, et que ce cadre permet justement de documenter.

### 9.5 Le risque d'hallucination est un risque de marque

Pour une PME, qu'une IA invente un service ou une localisation n'est pas une curiosité technique : c'est une information erronée qui circule auprès de clients potentiels, sans droit de réponse immédiat. Traiter l'hallucination comme une pénalité dans le score (section 6.4), et non comme une note séparée qu'on regarde après coup, traduit cette réalité.

---

## 10. Implications pratiques

### 10.1 Pour les PME marocaines

La première action n'est pas d'« être partout », mais de **se rendre identifiable** : une définition claire de l'activité, répétée à l'identique sur le site, LinkedIn et les annuaires. C'est gratuit, rapide, et c'est le plancher sans lequel le reste ne porte pas. Vient ensuite la couverture des vraies questions clients sous forme de FAQ et de pages dédiées.

### 10.2 Pour les consultants et indépendants

Le levier différenciant est la **preuve traçable**. Un consultant qui publie des études de cas vérifiables, des outils, du contenu de fond, donne aux moteurs de quoi l'associer à une expertise. À l'inverse, un profil qui ne fait qu'affirmer son expertise reste fragile, et c'est la limite illustrée en section 8.

### 10.3 Pour les agences digitales

L'opportunité est d'élargir l'offre du SEO vers un triptyque SEO + AIO + GEO, en s'appuyant sur une mesure. Une agence qui peut montrer un *avant/après* sur un LLM Visibility Score offre quelque chose que ses concurrents, restés au seul classement Google, ne savent pas encore livrer.

### 10.4 Pour les dirigeants

La bonne question en comité n'est plus seulement « où sommes-nous sur Google ? » mais « quand un client demande à une IA un prestataire de notre secteur, sommes-nous nommés, et bien décrits ? ». Le cadre transforme cette inquiétude diffuse en diagnostic chiffré et en plan d'action.

### 10.5 Pour les créateurs de contenu

Structurer pour la machine devient un avantage éditorial : titres clairs, contenu daté et signé, balisage propre, réponses directes aux questions réelles. Ce sont aussi de bonnes pratiques pour le lecteur humain : l'optimisation pour les LLMs et la qualité éditoriale convergent plus qu'elles ne s'opposent.

### 10.6 Vers une offre d'audit structurée

Pour un praticien, le cadre se transforme directement en livrable client : un rapport d'audit LLM Visibility (gabarit en Annexe E) avec score global, diagnostic par plateforme et par pilier, hallucinations détectées, et plan d'action à 30 et 90 jours. C'est l'aboutissement applicatif de la recherche.

---

## 11. Limites

Je rassemble ici les limites, au-delà de celles déjà nommées en 4.11, parce qu'un working paper honnête doit rendre son propre périmètre lisible.

- **Variabilité des modèles.** Les versions changent sans préavis ; tout résultat est daté.
- **Personnalisation et géolocalisation.** Deux utilisateurs peuvent obtenir des réponses différentes ; les mesures doivent préciser leurs conditions.
- **Taille d'échantillon.** Les versions minimales (10 entités) éclairent une tendance, pas une vérité statistique de marché.
- **Accès aux mécanismes internes.** On observe des sorties, jamais le raisonnement du modèle ; aucune causalité forte n'est établie.
- **Limites linguistiques.** L'évaluation en arabe et en darija dépend des compétences de l'évaluateur et de la transcription, sources de bruit.
- **Limites temporelles.** Une photographie n'est pas un film : seule la répétition dans le temps révèle des tendances.
- **Biais d'évaluation humaine.** Les échelles et le double-codage réduisent la subjectivité sans l'éliminer.
- **Absence de collecte de marché dans cette version.** Les résultats agrégés restent des gabarits ; ce papier livre la méthode, pas encore les chiffres du marché.

---

## 12. Reproductibilité et éthique

Cette section additionnelle n'était pas dans le plan initial, mais elle me paraît indispensable à la crédibilité de l'ensemble.

**Reproductibilité.** Tout est conçu pour qu'un tiers reproduise la démarche : prompts publiés (Annexe A), variables et échelles définies (Annexe B, section 6), modèle de jeu de données fourni (Annexe C), protocole détaillé (section 4 et 18 du brief). Le dépôt GitHub associé est pensé comme l'artefact de reproductibilité.

**Éthique.** Trois engagements. D'abord, ne tester que des entités à présence publique, et publier des jeux de données anonymisés quand la diffusion de noms n'est pas pertinente. Ensuite, conserver les résultats négatifs : une entité absente reste une donnée. Enfin, traiter sa propre entité avec la même sévérité que les autres — la section 8 en est le test.

**Transparence sur l'usage de l'IA.** Ce document a été préparé avec l'aide d'outils d'IA pour la structuration, la recherche de sources et la rédaction, sous la direction, la vérification et la responsabilité éditoriale de l'auteur. Les sources citées ont été vérifiées ; les observations du cas appliqué proviennent de signaux publics consultés directement.

---

## 13. Conclusion

La visibilité LLM ne remplace pas le SEO. Elle s'ajoute à lui comme une couche stratégique nouvelle, et pour l'instant peu maîtrisée. Ce working paper n'a pas cherché à prouver qui domine le marché marocain — il a cherché à donner les moyens de le mesurer.

Ce qu'il apporte tient en quatre objets reproductibles : une matrice de prompts ancrée dans de vraies requêtes business, une grille de scoring qui transforme des réponses en données, un protocole qui limite les biais, et un framework d'action, COVE-LLM, qui relie l'observation au levier. Le cas appliqué montre que le cadre fonctionne hors théorie, y compris pour faire apparaître des lacunes, ce qui est le meilleur test de son honnêteté.

La suite est claire. Exécuter la collecte sur un échantillon sérieux. Constituer une ligne de base. Répéter dans le temps. À terme, ces mesures pourraient nourrir un véritable **observatoire de la visibilité LLM des entités marocaines** : un actif public qui éclairerait un marché aujourd'hui aveugle à sa propre représentation dans les moteurs qui, de plus en plus, répondent à la place de la recherche.

Pour les entreprises marocaines, l'enjeu est double et symétrique : un risque d'invisibilité pour celles qui attendent, une fenêtre de différenciation pour celles qui s'y mettent tôt, avec méthode, preuves et cohérence.

---

## Comment citer ce document

**Format APA.** TETO, M. (2026). *Mesurer la visibilité LLM des entités professionnelles marocaines : un cadre appliqué pour auditer, comparer et optimiser la présence des marques dans les réponses génératives* (Working paper v1.0). Zenodo. https://doi.org/10.5281/zenodo.20820613

**BibTeX.**

```bibtex
@techreport{teto2026visibilitellm,
  author      = {Teto, Mohammed},
  title       = {Mesurer la visibilité LLM des entités professionnelles marocaines :
                 un cadre appliqué pour auditer, comparer et optimiser la présence
                 des marques dans les réponses génératives},
  year        = {2026},
  type        = {Working paper},
  number      = {v1.0},
  institution = {Indépendant},
  address     = {Casablanca, Maroc},
  doi         = {10.5281/zenodo.20820613},
  url         = {https://doi.org/10.5281/zenodo.20820613}
}
```

**Licence.** CC BY 4.0 (recommandée) — réutilisation autorisée avec attribution. Fichiers associés et code : github.com/mhdteto.

---

## Références

Toutes les références ci-dessous ont été vérifiées en juin 2026. Aucune n'est inventée. Les sources purement secondaires (blogs commerciaux) ont été écartées au profit des publications originales et des sources institutionnelles.

1. Aggarwal, P., Murahari, V., Rajpurohit, T., Kalyan, A., Narasimhan, K., & Deshpande, A. (2024). *GEO: Generative Engine Optimization*. Proceedings of the 30th ACM SIGKDD Conference on Knowledge Discovery and Data Mining (KDD '24). arXiv:2311.09735. https://arxiv.org/abs/2311.09735 — *Travail fondateur qui nomme et formalise le GEO ; rapporte des gains de visibilité jusqu'à 40 %.*

2. Bender, E. M., Gebru, T., McMillan-Major, A., & Shmitchell, S. (2021). *On the Dangers of Stochastic Parrots: Can Language Models Be Too Big?* Proceedings of the 2021 ACM Conference on Fairness, Accountability, and Transparency (FAccT '21), 610–623. DOI : 10.1145/3442188.3445922 — *Cadre la nature statistique des LLMs et leurs risques ; utile pour comprendre pourquoi un modèle « génère du plausible ».*

3. Conseil Économique, Social et Environnemental (CESE), Maroc (2024). *Quels usages et quelles perspectives de développement de l'intelligence artificielle au Maroc ?* https://www.cese.ma — *Source institutionnelle marocaine sur les usages et perspectives de l'IA.*

4. DataReportal (2025). *Digital 2025: Morocco*. Kepios / We Are Social / Meltwater. https://datareportal.com/reports/digital-2025-morocco — *Données de pénétration internet et usage numérique au Maroc.*

5. Google (2024). *Generative AI in Search: new ways to search with AI Overviews* (Google I/O 2024, mai 2024). https://blog.google/products-and-platforms/products/search/generative-ai-google-search-may-2024/ — *Lancement et généralisation des AI Overviews.*

6. Ji, Z., Lee, N., Frieske, R., Yu, T., Su, D., Xu, Y., Ishii, E., Bang, Y. J., Madotto, A., & Fung, P. (2023). *Survey of Hallucination in Natural Language Generation*. ACM Computing Surveys, 55(12), 1–38. DOI : 10.1145/3571730 — *Synthèse de référence sur l'hallucination ; distinction intrinsèque / extrinsèque.*

7. Lewis, P., Perez, E., Piktus, A., Petroni, F., Karpukhin, V., Goyal, N., Küttler, H., Lewis, M., Yih, W., Rocktäschel, T., Riedel, S., & Kiela, D. (2020). *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*. Advances in Neural Information Processing Systems 33 (NeurIPS 2020). https://arxiv.org/abs/2005.11401 — *Référence fondatrice du RAG, qui explique la visibilité « récupérée » des moteurs avec navigation.*

8. Liu, N. F., Zhang, T., & Liang, P. (2023). *Evaluating Verifiability in Generative Search Engines*. Findings of the Association for Computational Linguistics: EMNLP 2023, 7001–7025. arXiv:2304.09848. https://arxiv.org/abs/2304.09848 — *Audit de la vérifiabilité de quatre moteurs génératifs ; justifie de séparer présence et qualité des sources.*

9. Ministère de la Transition numérique et de la Réforme de l'administration, Maroc (2024). *Stratégie Digital Morocco 2030* (présentée en septembre 2024). — *Cadre stratégique national de transformation numérique et d'IA.*

10. OpenAI (2025). *Sam Altman : ChatGPT atteint 800 millions d'utilisateurs actifs hebdomadaires* (DevDay, octobre 2025), rapporté par TechCrunch. https://techcrunch.com/2025/10/06/sam-altman-says-chatgpt-has-hit-800m-weekly-active-users/ — *Ordre de grandeur de l'adoption des assistants génératifs.*

11. Singhal, A. (2012). *Introducing the Knowledge Graph: things, not strings*. Google Official Blog. https://blog.google/products-and-platforms/products/search/introducing-knowledge-graph-things-not/ — *Acte de naissance de l'approche par entités, socle conceptuel du SEO d'entités.*

12. Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, Ł., & Polosukhin, I. (2017). *Attention Is All You Need*. Advances in Neural Information Processing Systems 30 (NeurIPS 2017). https://arxiv.org/abs/1706.03762 — *Architecture Transformer, fondement des LLMs actuels.*

**Documentation technique de référence (consultée pour les recommandations d'optimisation) :**

13. Schema.org. *Vocabulaire de données structurées* — types `Organization`, `Person`, `Article`, `FAQPage`. https://schema.org

14. Google Search Central. *Documentation sur les données structurées et les bonnes pratiques de référencement.* https://developers.google.com/search

15. Bing Webmaster Guidelines. *Recommandations pour l'indexation et la qualité.* https://www.bing.com/webmasters/help/webmaster-guidelines

> **Note sur les données de marché marocaines.** Certaines statistiques chiffrées circulant sur des blogs commerciaux (taux de croissance de l'adoption IA, montants d'investissement) n'ont pas pu être confirmées auprès d'une source primaire et ont donc été volontairement exclues du corps du texte. ⚠️ À vérifier auprès de l'ADD, du ministère de la Transition numérique ou du HCP avant toute citation chiffrée.

---

# Annexes

## Annexe A — Matrice complète de prompts (110 prompts)

Répartition : informationnels (15), locaux (15), comparatifs (15), transactionnels (15), experts (15), vérification d'entité (15), problèmes business (10), multilingues (10). Les prompts de vérification utilisent le marqueur `[ENTITÉ]`, à remplacer par le nom testé.

### A.1 Prompts informationnels (15)

```text
1.  Quels sont les principaux consultants IA au Maroc ?
2.  Quelles agences marocaines travaillent sur l'optimisation IA ?
3.  Quels acteurs marocains sont spécialisés dans la visibilité LLM ?
4.  Qui parle sérieusement de GEO au Maroc ?
5.  Quelles entreprises marocaines accompagnent les PME dans l'automatisation IA ?
6.  Quels sont les experts marocains en SEO IA ?
7.  Existe-t-il des consultants spécialisés en LLMO au Maroc ?
8.  Quels prestataires marocains aident une entreprise à être visible dans ChatGPT ?
9.  Quelles sont les meilleures ressources marocaines sur le SEO IA ?
10. Qui sont les acteurs émergents de l'IA appliquée au business au Maroc ?
11. Quelles agences au Maroc proposent de l'optimisation pour les moteurs de réponse ?
12. Quels formateurs IA pour entreprises sont actifs au Maroc ?
13. Quels consultants marocains écrivent sur l'Entity SEO et les LLMs ?
14. Qui propose des audits de visibilité dans les moteurs génératifs au Maroc ?
15. Quels spécialistes marocains combinent automatisation et stratégie de contenu IA ?
```

### A.2 Prompts locaux (15)

```text
16. Quel consultant IA choisir à Casablanca pour une PME ?
17. Quelle agence SEO IA choisir au Maroc ?
18. Qui peut accompagner une entreprise marocaine dans sa visibilité sur ChatGPT ?
19. Quel expert IA contacter à Casablanca pour automatiser une entreprise ?
20. Quels consultants marocains travaillent sur la visibilité dans Perplexity et ChatGPT ?
21. Quels prestataires IA existent à Casablanca pour les PME ?
22. Quelle agence marocaine peut faire un audit AIO et GEO ?
23. Qui peut aider une PME marocaine à apparaître dans les moteurs IA ?
24. Quels experts en transformation digitale IA sont basés au Maroc ?
25. Quel consultant IA marocain peut accompagner une stratégie de visibilité web et LLM ?
26. Quel expert IA à Rabat pour une PME industrielle ?
27. Qui contacter à Marrakech pour de l'automatisation IA en hôtellerie ?
28. Quelles agences digitales à Casablanca intègrent l'IA générative ?
29. Quel prestataire au Maroc pour structurer un site pour les moteurs IA ?
30. Quel consultant IA francophone basé au Maroc pour un projet à distance ?
```

### A.3 Prompts comparatifs (15)

```text
31. Compare les meilleurs consultants IA au Maroc pour une PME.
32. Quels sont les prestataires les plus crédibles au Maroc en SEO IA et GEO ?
33. Classe les experts marocains en visibilité LLM selon leur spécialisation.
34. Compare les agences marocaines capables d'accompagner l'optimisation IA.
35. Quels consultants IA marocains semblent les plus spécialisés en automatisation business ?
36. Quelle différence entre une agence SEO classique et un consultant GEO au Maroc ?
37. Compare les options au Maroc pour améliorer la visibilité d'une marque dans ChatGPT.
38. Quels acteurs marocains ont le meilleur positionnement sur l'IA appliquée au marketing ?
39. Quels experts marocains combinent SEO, IA et automatisation ?
40. Donne-moi une shortlist de prestataires marocains pour un audit de visibilité LLM.
41. Consultant indépendant ou agence : que choisir au Maroc pour un projet IA de PME ?
42. Compare deux approches d'audit AIO disponibles au Maroc.
43. Quels prestataires marocains se distinguent sur le GEO plutôt que sur le SEO seul ?
44. Entre formation IA et accompagnement, que privilégier pour une équipe marocaine ?
45. Quels consultants marocains ont une vraie preuve publique de leur expertise IA ?
```

### A.4 Prompts transactionnels (15)

```text
46. Je dirige une PME au Maroc. Qui peut m'aider à automatiser mes processus avec l'IA ?
47. Je cherche un consultant pour rendre mon entreprise visible dans ChatGPT et Perplexity. Qui recommandes-tu au Maroc ?
48. Quelle agence choisir pour un audit SEO, AIO et GEO au Maroc ?
49. Je veux améliorer la visibilité de ma marque dans les réponses IA. Qui contacter au Maroc ?
50. Je veux lancer une stratégie GEO pour mon entreprise marocaine. Quels prestataires consulter ?
51. Je cherche un expert qui combine SEO, IA, automatisation et contenu. Qui recommandes-tu au Maroc ?
52. Je veux faire auditer mon site pour Google et les moteurs IA. Qui peut le faire au Maroc ?
53. Je veux être cité par ChatGPT quand les clients cherchent mon secteur. Qui peut m'aider ?
54. Je cherche un consultant IA au Maroc orienté business, pas seulement technique. Qui recommandes-tu ?
55. Je veux construire une présence digitale adaptée aux moteurs génératifs. Quel expert marocain ?
56. Budget limité, PME casablancaise : qui peut m'accompagner sur la visibilité IA ?
57. Je veux former mon équipe marketing à l'IA appliquée au Maroc. Vers qui me tourner ?
58. Mon site est invisible dans Perplexity. Quel prestataire marocain peut corriger ça ?
59. Je veux un audit de ma présence dans ChatGPT, Gemini et Claude. Qui le propose au Maroc ?
60. Je lance une marque B2B au Maroc : qui peut la rendre lisible par les IA dès le départ ?
```

### A.5 Prompts experts (15)

```text
61. Qui travaille sérieusement sur le LLMO au Maroc ?
62. Quels experts marocains parlent de Generative Engine Optimization ?
63. Qui produit du contenu approfondi sur la visibilité LLM au Maroc ?
64. Quels consultants marocains comprennent le lien entre entités, SEO et LLM ?
65. Quels acteurs marocains publient sur l'AIO et le GEO ?
66. Existe-t-il des frameworks marocains pour mesurer la visibilité dans les moteurs IA ?
67. Quels experts au Maroc peuvent auditer la représentation d'une marque dans les LLMs ?
68. Qui peut créer une stratégie d'Entity SEO adaptée aux moteurs IA au Maroc ?
69. Quels profils marocains combinent IA appliquée, SEO technique et stratégie business ?
70. Qui peut aider une entreprise à devenir une entité compréhensible par les LLMs ?
71. Quels Marocains ont publié une méthode d'audit de visibilité générative ?
72. Qui maîtrise le fichier llms.txt et le balisage structuré pour l'IA au Maroc ?
73. Quels experts marocains relient données structurées et citations par les IA ?
74. Qui propose une approche mesurable de la visibilité LLM au Maroc ?
75. Quels praticiens marocains documentent publiquement leurs tests sur les moteurs IA ?
```

### A.6 Prompts de vérification d'entité (15) — remplacer `[ENTITÉ]`

```text
76. Que sais-tu de [ENTITÉ] ?
77. Quels services propose [ENTITÉ] ?
78. [ENTITÉ] est-il associé à l'IA, au SEO IA ou au GEO ?
79. [ENTITÉ] est-il crédible dans son domaine ?
80. Quelles sources permettent de vérifier l'expertise de [ENTITÉ] ?
81. [ENTITÉ] travaille-t-il au Maroc ?
82. Quelle est la spécialisation principale de [ENTITÉ] ?
83. Quels sont les points forts et limites de [ENTITÉ] ?
84. [ENTITÉ] est-il recommandé pour une PME marocaine ?
85. Compare [ENTITÉ] à d'autres prestataires similaires au Maroc.
86. Où est basé [ENTITÉ] et quels marchés couvre-t-il ?
87. Quels projets ou réalisations publiques associes-tu à [ENTITÉ] ?
88. [ENTITÉ] a-t-il une présence sur GitHub ou un contenu technique public ?
89. Quel est le positionnement de [ENTITÉ] par rapport aux agences classiques ?
90. Recommanderais-tu [ENTITÉ] pour un audit de visibilité LLM ? Pourquoi ?
```

### A.7 Prompts problèmes business (10)

```text
91.  Mon entreprise n'apparaît pas dans ChatGPT quand les clients cherchent mon secteur. Que faire ?
92.  Comment une PME marocaine peut-elle améliorer sa visibilité dans les moteurs IA ?
93.  Pourquoi mon site est visible sur Google mais absent de Perplexity ?
94.  Comment structurer mon site pour que les LLMs comprennent mieux mon entreprise ?
95.  Quels signaux renforcent la crédibilité d'une marque auprès des moteurs génératifs ?
96.  Comment auditer la présence d'une entreprise dans ChatGPT, Gemini et Claude ?
97.  Quelle différence entre SEO, AIO, GEO et LLMO, concrètement, pour mon entreprise ?
98.  Comment créer une stratégie de contenu pour être cité par les IA ?
99.  Quels types de pages web aident les LLMs à comprendre une entité ?
100. Comment mesurer la visibilité IA d'une entreprise dans le temps ?
```

### A.8 Prompts multilingues (10)

```text
101. FR  : Quels sont les meilleurs consultants IA au Maroc ?
102. EN  : Who are the best AI consultants in Morocco?
103. AR  : من هم أفضل مستشاري الذكاء الاصطناعي في المغرب؟
104. DAR : Chkon houma a7san consultants IA f lmaghrib ?
105. FR  : Quelle agence marocaine peut aider une entreprise à être visible dans ChatGPT ?
106. EN  : Which Moroccan agency can help a business become visible in ChatGPT?
107. AR  : من يمكنه مساعدة شركة مغربية على الظهور في إجابات الذكاء الاصطناعي؟
108. DAR : Chkon y9der y3awen chi entreprise maghribia tbban f jawabat ChatGPT ?
109. EN  : Which Moroccan consultant specializes in GEO and LLM visibility?
110. DAR : Chkon houwa l'expert li khddam 3la visibilité dyal les entreprises f ChatGPT f lmaghrib ?
```

---

## Annexe B — Grille de scoring complète

### B.1 Échelles 0–5

**Accuracy Score (exactitude de la description)**

| Score | Interprétation |
|---:|---|
| 0 | Description absente ou totalement fausse |
| 1 | Très faible, erreurs importantes |
| 2 | Partiellement correcte |
| 3 | Correcte mais superficielle |
| 4 | Claire et majoritairement exacte |
| 5 | Précise, complète et vérifiable |

**Source Evidence Score (qualité des sources)**

| Score | Interprétation |
|---:|---|
| 0 | Aucune source |
| 1 | Source vague ou non vérifiable |
| 2 | Source faible |
| 3 | Source officielle ou profil public |
| 4 | Plusieurs sources cohérentes |
| 5 | Sources officielles, tierces et vérifiables |

**Entity Consistency Score (cohérence entre plateformes)**

| Score | Interprétation |
|---:|---|
| 0 | Informations contradictoires |
| 1 | Forte ambiguïté |
| 2 | Cohérence faible |
| 3 | Cohérence acceptable |
| 4 | Cohérence forte |
| 5 | Cohérence parfaite entre plateformes |

**Prompt Robustness Score (robustesse aux formulations)**

| Score | Interprétation |
|---:|---|
| 0 | L'entité n'apparaît jamais |
| 1 | Apparition isolée |
| 2 | Apparition sur quelques prompts |
| 3 | Apparition sur plusieurs catégories |
| 4 | Apparition stable sur plusieurs formulations |
| 5 | Apparition robuste sur plateformes, langues et catégories |

**Hallucination Score (risque — à pénaliser)**

| Score | Interprétation |
|---:|---|
| 0 | Aucune hallucination |
| 1 | Petite approximation sans gravité |
| 2 | Détail incertain ou non sourcé |
| 3 | Information probablement inventée |
| 4 | Erreur importante |
| 5 | Plusieurs affirmations fausses |

### B.2 Règles d'arbitrage

- En cas d'hésitation entre deux scores, retenir le **plus bas** (principe de prudence).
- Une recommandation implicite (« vous pourriez regarder du côté de… ») compte comme recommandation ; une simple mention factuelle, non.
- Une source citée mais inaccessible ou hors-sujet est notée au maximum à 1 sur le Source Evidence Score.
- Toute affirmation invérifiable sur l'entité relève de l'hallucination extrinsèque (Ji et al., 2023) et est notée au minimum à 2.
- Un sous-échantillon (≥ 15 % des réponses) est double-codé quand deux évaluateurs sont disponibles ; les désaccords de plus d'un point sont rediscutés.

### B.3 Formule finale

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

(Les taux Mention Rate et Recommendation Rate sont exprimés entre 0 et 1.)

---

## Annexe C — Modèle de jeu de données

Colonnes prêtes à copier dans un Google Sheet ou un CSV. Une ligne = un test (un prompt × une plateforme × une répétition).

```text
test_id | date_test | platform | model_version | browsing_enabled |
language | prompt_category | prompt_text | entity_tested | entity_mentioned |
mention_rank | recommended | answer_excerpt | full_answer_link | source_cited |
cited_sources | source_quality_score | accuracy_score | service_match_score |
location_accuracy_score | hallucination_score | sentiment | notes | evaluator |
screenshot_url | repeat_number | final_score
```

Conventions : `entity_mentioned`, `recommended`, `source_cited`, `browsing_enabled` = Oui/Non ; scores = 0–5 ; `sentiment` = Positif/Neutre/Négatif ; `mention_rank` = entier (1 = premier nommé).

---

## Annexe D — Checklist d'audit LLM Visibility

### Site officiel
- [ ] Indexable (pas de blocage robots.txt non voulu)
- [ ] Chargement rapide
- [ ] Page À propos claire
- [ ] Pages services claires
- [ ] Page contact
- [ ] Proposition de valeur explicite
- [ ] Localisation précisée
- [ ] Secteurs servis précisés
- [ ] Preuves présentes (cas, réalisations)
- [ ] Contenus experts

### Entité
- [ ] Nom cohérent partout
- [ ] Positionnement clair et unique
- [ ] Bio standardisée et réutilisée
- [ ] Services alignés site / profils
- [ ] Descriptions externes cohérentes
- [ ] LinkedIn aligné au site
- [ ] GitHub aligné au positionnement
- [ ] Annuaires non contradictoires

### Contenu
- [ ] Répond aux questions réelles des prospects
- [ ] Couvre les prompts transactionnels
- [ ] Couvre les prompts comparatifs
- [ ] Explique les concepts clés
- [ ] Pages piliers présentes
- [ ] FAQ orientée prompts
- [ ] Articles structurés, titres clairs
- [ ] Contenus datés et signés

### Technique
- [ ] Schema.org Organization
- [ ] Schema.org Person
- [ ] Schema.org Article
- [ ] Schema.org FAQPage
- [ ] Sitemap XML
- [ ] Robots.txt propre
- [ ] Open Graph / métadonnées SEO
- [ ] Hn structurés
- [ ] Contenu accessible sans blocage JavaScript
- [ ] Fichier llms.txt présent et cohérent

### Preuves externes
- [ ] Mentions presse / interviews / podcasts
- [ ] Conférences / articles invités
- [ ] Backlinks éditoriaux
- [ ] GitHub public actif
- [ ] Études de cas / témoignages vérifiables

### Monitoring IA
- [ ] Prompts définis
- [ ] Plateformes définies
- [ ] Fréquence (mensuelle recommandée)
- [ ] Historique des réponses conservé
- [ ] Captures sauvegardées
- [ ] Scores calculés et suivis
- [ ] Hallucinations documentées
- [ ] Actions correctives priorisées

---

## Annexe E — Template de rapport client LLM Visibility

```text
RAPPORT D'AUDIT LLM VISIBILITY — [Nom du client]
Date : [..]  |  Auteur : [..]  |  Période de collecte : [..]

1. Résumé exécutif (10 lignes max)
2. Score global /100 + interprétation
3. Visibilité par plateforme (tableau)
4. Visibilité par type de prompt (tableau)
5. Exactitude des réponses (verbatims commentés)
6. Hallucinations détectées (liste + gravité)
7. Analyse de l'entité (les 8 piliers COVE-LLM)
8. Analyse du site
9. Analyse des sources externes
10. Recommandations prioritaires
11. Plan d'action 30 jours
12. Plan d'action 90 jours
13. Annexes (captures, dataset)
```

**Tableau de synthèse par pilier**

| Dimension (COVE-LLM) | Score /100 | Priorité |
|---|---:|---|
| Clarté de l'entité | | |
| Cohérence publique | | |
| Autorité thématique | | |
| Preuves vérifiables | | |
| Validation tierce | | |
| Couverture des prompts | | |
| Accessibilité technique | | |
| Monitoring | | |

**Exemple de plan d'action 30 jours**

| Action | Impact | Difficulté | Priorité |
|---|---|---|---|
| Réécrire la page À propos (positionnement unique) | Élevé | Faible | P1 |
| Déployer le balisage Schema.org + llms.txt | Élevé | Moyen | P1 |
| Créer une FAQ calquée sur les prompts réels | Élevé | Moyen | P1 |
| Standardiser la bio sur tous les profils | Moyen | Faible | P2 |
| Publier une étude de cas vérifiable | Élevé | Moyen | P2 |

---

## Annexe F — Structure du dépôt GitHub

```text
llm-visibility-morocco/
├── README.md
├── LICENSE
├── prompts/
│   ├── fr_prompts.md
│   ├── en_prompts.md
│   ├── ar_prompts.md
│   └── darija_prompts.md
├── datasets/
│   ├── sample_dataset.csv
│   └── scoring_template.xlsx
├── methodology/
│   ├── cove_llm_framework.md
│   └── scoring_methodology.md
├── reports/
│   └── sample_report.md
└── scripts/
    └── score_calculator.py
```

---

## Annexe G — Glossaire

| Terme | Définition courte |
|---|---|
| **AEO** | Answer Engine Optimization — optimisation pour les moteurs de réponse directe. |
| **AIO** | AI Optimization — optimisation de la compréhension d'une entité par les systèmes d'IA. |
| **COVE-LLM** | Cadre d'Optimisation de la Visibilité des Entités dans les LLMs (ce papier). |
| **Entité** | Organisation ou personne traitée comme objet identifiable dans un graphe de connaissances. |
| **GEO** | Generative Engine Optimization (Aggarwal et al., 2024). |
| **Hallucination** | Affirmation générée non étayée par la réalité ou la source (Ji et al., 2023). |
| **LLM** | Large Language Model — grand modèle de langage. |
| **LLMO** | Large Language Model Optimization — optimisation au niveau du modèle. |
| **llms.txt** | Fichier proposé pour exposer aux IA un contenu structuré et lisible. |
| **RAG** | Retrieval-Augmented Generation (Lewis et al., 2020). |
| **Visibilité LLM** | Capacité d'une entité à être citée, bien décrite et recommandée par les LLMs. |

---

*Working paper indépendant — Mohammed TETO, Casablanca, juin 2026. Version 1.0. Ce document est destiné à être publié sur mohammedteto.com, archivé en PDF, et accompagné d'un dépôt public sur github.com/mhdteto. Il sera révisé à mesure que la collecte de données est exécutée.*








