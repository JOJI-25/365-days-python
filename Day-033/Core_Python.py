searches = [
    ["laptop", "wireless mouse", "laptop bag"],
    ["iphone", "phone case", "iphone charger"],
    ["laptop", "ssd", "ram"],
    ["headphones", "bluetooth speaker", "headphones"],
    ["iphone", "airpods", "phone case"],
    ["laptop", "laptop stand", "wireless mouse"],
]


def analyse_searches(searches):
    # 1. Unique search terms across all sessions
    unique_terms = set(term for session in searches for term in session)

    # Counts for total frequency and session presence
    term_frequencies = {}
    session_counts = {}
    session_unique_counts = []
    pair_counts = {}

    for session in searches:
        unique_session_terms = sorted(set(session))

        # 5. Number of unique search terms in this session
        session_unique_counts.append(len(unique_session_terms))

        # Overall frequency of each term
        for term in session:
            term_frequencies[term] = term_frequencies.get(term, 0) + 1

        # 2. Number of sessions containing each term
        for term in unique_session_terms:
            session_counts[term] = session_counts.get(term, 0) + 1

        # 6. Generate term pairs in this session
        for i in range(len(unique_session_terms)):
            for j in range(i + 1, len(unique_session_terms)):
                pair = (unique_session_terms[i], unique_session_terms[j])
                pair_counts[pair] = pair_counts.get(pair, 0) + 1

    # 3. Top 5 most frequently searched terms
    top_5_searches = sorted(
        term_frequencies.items(), key=lambda item: item[1], reverse=True
    )[:5]

    # 4. Search term appearing in the greatest number of sessions
    most_common_in_sessions = max(
        session_counts.items(), key=lambda item: item[1]
    )

    # 6. Pairs appearing together in at least 2 sessions
    frequent_pairs = {
        pair: count for pair, count in pair_counts.items() if count >= 2
    }

    total_sessions = len(searches)
    avg_unique = (
        sum(session_unique_counts) / total_sessions if total_sessions else 0
    )

    return {
        "unique_terms": unique_terms,
        "session_counts": session_counts,
        "top_5_searches": top_5_searches,
        "most_common_term_by_session": most_common_in_sessions,
        "unique_terms_per_session": session_unique_counts,
        "frequent_pairs": frequent_pairs,
        "term_frequencies": term_frequencies,
        "session_statistics": {
            "total_sessions": total_sessions,
            "avg_unique_terms_per_session": round(avg_unique, 2),
        },
    }


# Execute analysis and print results
results = analyse_searches(searches)

print("1. All Unique Search Terms:")
print(results["unique_terms"])

print("\n2. Session Count for Each Term:")
for term, count in results["session_counts"].items():
    print(f"   {term}: {count} session(s)")

print("\n3. Top 5 Most Frequently Searched Terms:")
for term, count in results["top_5_searches"]:
    print(f"   {term}: {count} searches")

print("\n4. Term Appearing in the Most Sessions:")
term, count = results["most_common_term_by_session"]
print(f"   '{term}' (appears in {count} sessions)")

print("\n5. Unique Search Terms per Session:")
for idx, count in enumerate(results["unique_terms_per_session"], start=1):
    print(f"   Session {idx}: {count} unique terms")

print("\n6. Pairs Appearing Together in At Least 2 Sessions:")
for pair, count in results["frequent_pairs"].items():
    print(f"   {pair[0]} + {pair[1]}: {count} sessions")