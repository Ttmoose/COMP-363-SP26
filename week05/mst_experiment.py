import random
import time
import pandas as pd
import matplotlib.pyplot as plt
from mst import MST  # Import the MST class from mst.py

# Generate a symmetric adjacency matrix for an undirected graph
def make_graph(n: int, density: float, max_w: int, seed: int) -> list[list[int]]:
    random.seed(seed)
    graph = [[0] * n for _ in range(n)]

    # Ensure the graph is connected by creating a spanning tree
    for i in range(1, n):
        weight = random.randint(1, max_w)
        j = random.randint(0, i - 1)
        graph[i][j] = weight
        graph[j][i] = weight  # Ensure symmetry

    # Add additional edges based on density
    for i in range(n):
        for j in range(i + 1, n):
            if random.random() < density:
                weight = random.randint(1, max_w)
                graph[i][j] = weight
                graph[j][i] = weight  # Ensure symmetry

    return graph

# Compute the total weight of an MST
def mst_weight(T: list[list[int]], no_edge: int = 0) -> int:
    total_weight = 0
    n = len(T)
    for i in range(n):
        for j in range(i + 1, n):
            if T[i][j] != no_edge:
                total_weight += T[i][j]
    return total_weight

# Verify that the MSTs computed by Borůvka and Kruskal match in weight
def verify_mst(graph: list[list[int]]):
    test = MST(graph)
    T_b = test.boruvka()
    T_k = test.kruskal()

    weight_boruvka = mst_weight(T_b)
    weight_kruskal = mst_weight(T_k)

    assert weight_boruvka == weight_kruskal, f"Borůvka weight: {weight_boruvka}, Kruskal weight: {weight_kruskal}"
    print(f"MST weight (Borůvka): {weight_boruvka}")
    print(f"MST weight (Kruskal): {weight_kruskal}")

# Time Borůvka's and Kruskal's algorithms for various graph sizes
def time_mst_algorithms(n_values: list[int], density: float, max_w: int, trials: int, seed: int):
    results = []

    for n in n_values:
        boruvka_times = []
        kruskal_times = []

        for trial in range(trials):
            graph = make_graph(n, density, max_w, seed + trial)
            test = MST(graph)

            # Time Borůvka's algorithm
            start_time = time.time()
            test.boruvka()
            end_time = time.time()
            boruvka_times.append(end_time - start_time)

            # Time Kruskal's algorithm
            start_time = time.time()
            test.kruskal()
            end_time = time.time()
            kruskal_times.append(end_time - start_time)

        results.append({
            "n": n,
            "trials": trials,
            "avg_boruvka_time": sum(boruvka_times) / trials,
            "avg_kruskal_time": sum(kruskal_times) / trials,
            "std_boruvka_time": (sum((t - (sum(boruvka_times) / trials)) ** 2 for t in boruvka_times) / trials) ** 0.5,
            "std_kruskal_time": (sum((t - (sum(kruskal_times) / trials)) ** 2 for t in kruskal_times) / trials) ** 0.5,
        })

    return results

# Display timing results as a table and plot
def display_results(results: list[dict]):
    df = pd.DataFrame(results)
    print(df)

    plt.figure(figsize=(10, 6))
    plt.plot(df["n"], df["avg_boruvka_time"], label="Borůvka", marker="o")
    plt.plot(df["n"], df["avg_kruskal_time"], label="Kruskal", marker="o")
    plt.fill_between(df["n"],
                        df["avg_boruvka_time"] - df["std_boruvka_time"],
                        df["avg_boruvka_time"] + df["std_boruvka_time"],
                        alpha=0.2)
    plt.fill_between(df["n"],
                        df["avg_kruskal_time"] - df["std_kruskal_time"],
                        df["avg_kruskal_time"] + df["std_kruskal_time"],
                        alpha=0.2)
    plt.xlabel("Number of Vertices (n)")
    plt.ylabel("Average Time (seconds)")
    plt.title("Average Time for Borůvka's and Kruskal's Algorithms")
    plt.legend()
    plt.grid()
    plt.show()

# Main execution
if __name__ == "__main__":
    # Parameters
    n_values = [10, 20, 30, 40, 50]
    density = 0.5
    max_w = 100
    trials = 5
    seed = 42

    # Run experiments
    results = time_mst_algorithms(n_values, density, max_w, trials, seed)

    # Display results
    display_results(results)