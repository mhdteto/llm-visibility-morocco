#!/usr/bin/env python3
"""
LLM Visibility Score — calcul du score de visibilité générative par entité.

Lit un CSV au format de datasets/dataset-modele.csv et calcule, pour chaque
entité testée, les composantes du LLM Visibility Score puis le score global /100.

Sans dépendance externe (csv de la stdlib).

Usage:
    python3 score_calculator.py datasets/dataset-modele.csv
    python3 score_calculator.py mon_dataset.csv --consistency 4

Méthodologie : voir methodology/grille-scoring.md et le working paper
(DOI 10.5281/zenodo.20820613). Aucun résultat n'est inventé : le script ne
calcule que ce que contient le CSV fourni.
"""
import csv, sys, argparse
from collections import defaultdict

YES = {"oui", "yes", "y", "1", "true", "vrai"}
REC_CATEGORIES = {"transactionnel", "comparatif"}
SENTIMENT_MAP = {"positif": 5, "neutre": 3, "negatif": 0, "négatif": 0}


def is_yes(v):
    return str(v).strip().lower() in YES


def num(v):
    try:
        return float(str(v).strip().replace(",", "."))
    except (ValueError, AttributeError):
        return None


def mean(xs):
    xs = [x for x in xs if x is not None]
    return sum(xs) / len(xs) if xs else 0.0


def compute(rows, consistency_default):
    total = len(rows)
    mentioned = [r for r in rows if is_yes(r.get("entity_mentioned"))]
    mention_rate = len(mentioned) / total if total else 0.0

    rec_base = [r for r in rows if (r.get("prompt_category", "").strip().lower() in REC_CATEGORIES)]
    rec_yes = [r for r in rec_base if is_yes(r.get("recommended"))]
    rec_rate = len(rec_yes) / len(rec_base) if rec_base else 0.0

    accuracy = mean([num(r.get("accuracy_score")) for r in mentioned])
    source_ev = mean([num(r.get("source_quality_score")) for r in mentioned])
    halluc = mean([num(r.get("hallucination_score")) for r in rows])

    sentiment = mean([SENTIMENT_MAP.get(str(r.get("sentiment", "")).strip().lower())
                      for r in mentioned]) if mentioned else 0.0

    cats = {r.get("prompt_category", "").strip().lower() for r in mentioned if r.get("prompt_category")}
    robustness = min(5.0, len(cats))                      # proxy : diversité des catégories
    langs = {r.get("language", "").strip().lower() for r in mentioned if r.get("language")}
    multilingual = min(5.0, len(langs) * 1.25)            # proxy : diversité linguistique

    consistency = consistency_default                     # non dérivable du CSV : placeholder

    accuracy_pen = accuracy * (5 - halluc) / 5            # pénalité hallucination

    score = (25 * mention_rate
             + 20 * rec_rate
             + 15 * (accuracy_pen / 5)
             + 10 * (source_ev / 5)
             + 10 * (consistency / 5)
             + 10 * (robustness / 5)
             + 5 * (multilingual / 5)
             + 5 * (sentiment / 5))

    return {
        "tests": total,
        "mention_rate": round(mention_rate, 3),
        "recommendation_rate": round(rec_rate, 3),
        "accuracy": round(accuracy, 2),
        "accuracy_penalisee": round(accuracy_pen, 2),
        "source_evidence": round(source_ev, 2),
        "hallucination": round(halluc, 2),
        "robustesse_prompts": round(robustness, 2),
        "multilingue": round(multilingual, 2),
        "sentiment": round(sentiment, 2),
        "consistance(placeholder)": consistency,
        "LLM_Visibility_Score_/100": round(score, 1),
    }


def main():
    ap = argparse.ArgumentParser(description="LLM Visibility Score calculator")
    ap.add_argument("csv_path", help="chemin du fichier CSV (format dataset-modele.csv)")
    ap.add_argument("--consistency", type=float, default=3.0,
                    help="Entity Consistency Score 0-5 (non dérivable du CSV, défaut 3)")
    args = ap.parse_args()

    by_entity = defaultdict(list)
    with open(args.csv_path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            ent = (row.get("entity_tested") or "").strip()
            if ent:
                by_entity[ent].append(row)

    if not by_entity:
        print("Aucune entité trouvée dans le CSV."); sys.exit(1)

    print(f"\nLLM Visibility Score — {args.csv_path}\n" + "=" * 60)
    for ent in sorted(by_entity):
        res = compute(by_entity[ent], args.consistency)
        print(f"\n● {ent}")
        for k, v in res.items():
            print(f"    {k:30s} : {v}")
    print("\nNote : 'consistance' est un placeholder (à coder manuellement) ;")
    print("'robustesse' et 'multilingue' sont des proxys dérivés du CSV.")
    print("Méthodologie complète : methodology/grille-scoring.md\n")


if __name__ == "__main__":
    main()
