referrals = {
    "Asha": ["Binu", "Chitra"],
    "Binu": ["Deepa", "Eshan"],
    "Chitra": ["Farah"],
    "Deepa": ["Gopal"],
    "Eshan": ["Gopal", "Hari"],
    "Farah": [],
    "Gopal": [],
    "Hari": ["Ira"],
    "Ira": [],
    "Jaya": []
}

# 1. Validation, No Outgoing Referrals, and Never Referred Members
def analyze_network(graph):
    all_members = set(graph.keys())
    all_targets = set(target for targets in graph.values() for target in targets)
    all_nodes = all_members.union(all_targets)
    
    no_outgoing = [m for m, targets in graph.items() if not targets]
    never_referred = [m for m in all_nodes if m not in all_targets]
    
    return all_nodes, no_outgoing, never_referred

# 2. Function to find all unique reachable members from a starting member
def get_reachable_members(start, graph):
    visited = set()
    queue = [start]
    while queue:
        curr = queue.pop(0)
        for neighbor in graph.get(curr, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return visited

# 3. Calculate minimum referral depth from "Asha"
def get_min_depths(start, graph):
    depths = {start: 0}
    queue = [start]
    while queue:
        curr = queue.pop(0)
        curr_depth = depths[curr]
        for neighbor in graph.get(curr, []):
            if neighbor not in depths:
                depths[neighbor] = curr_depth + 1
                queue.append(neighbor)
    return depths

# 4. Total downstream members for each starting member and max reach
def calculate_all_reaches(graph):
    all_nodes = set(graph.keys()).union(set(t for targets in graph.values() for t in targets))
    reaches = {}
    for node in all_nodes:
        reaches[node] = len(get_reachable_members(node, graph))
    max_person = max(reaches, key=reaches.get)
    return reaches, max_person

# Execution and Output
if __name__ == "__main__":
    nodes, no_out, never_ref = analyze_network(referrals)
    print("--- 1. Network Validation ---")
    print(f"Total members: {sorted(list(nodes))}")
    print(f"Members with no outgoing referrals: {no_out}")
    print(f"Members never referred to by others: {never_ref}")
    
    print("\n--- 2 & 3. Reachable Members & Depths from Asha ---")
    asha_depths = get_min_depths("Asha", referrals)
    for member, depth in sorted(asha_depths.items(), key=lambda x: x[1]):
        print(f"{member}: Depth {depth}")
        
    print("\n--- 4. Downstream Reach per Member ---")
    reaches, top_person = calculate_all_reaches(referrals)
    for person, count in sorted(reaches.items(), key=lambda x: x[1], reverse=True):
        print(f"{person}: {count} downstream members")
    print(f"\nMember with the greatest referral reach: {top_person} ({reaches[top_person]} downstream members)")