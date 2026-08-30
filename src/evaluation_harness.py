"""
Evaluation pipeline for the document QA system.
"""
import time

def run_rag_evaluation(evaluation_dataset, retriever, ask_rag_fn, verbose=True):

    results = []

    for i, item in enumerate(evaluation_dataset, start=1):
        question = item["question"]
        expected = item.get("expected", "N/A")
        category = item.get("category", "Uncategorized")


        context = retriever(question)


        start = time.time()
        answer = ask_rag_fn(question, context)
        elapsed = time.time() - start

        result = {
            "index": i,
            "category": category,
            "question": question,
            "expected": expected,
            "context": context,
            "model_answer": answer,
            "time_sec": round(elapsed, 2),
        }
        results.append(result)

        if verbose:
            print("=" * 70)
            print(f"QUESTION {i} [{category}]")
            print("=" * 70)
            print(f"Question: {question}")
            print(f"Expected: {expected}")
            print(f"Model Answer: {answer}")
            print(f"Time: {elapsed:.2f}s")
            print()

    return results


def summarize_results(results, save_csv_path=None):
    
    from collections import defaultdict

    by_category = defaultdict(list)
    for r in results:
        by_category[r["category"]].append(r)

    print("\n" + "=" * 70)
    print("SUMMARY BY CATEGORY")
    print("=" * 70)
    for category, items in by_category.items():
        print(f"\n{category} ({len(items)} questions):")
        for r in items:
            print(f"  Q{r['index']}: {r['question'][:60]}...")
            print(f"    -> {r['model_answer'][:100]}")

    if save_csv_path:
        import csv
        with open(save_csv_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["index", "category", "question", "expected", "model_answer", "time_sec"])
            writer.writeheader()
            for r in results:
                writer.writerow({k: r[k] for k in writer.fieldnames})
        print(f"\nSaved results to {save_csv_path}")

    return by_category


