import matplotlib.pyplot as plt

def tsp(graph, start):
    n = len(graph)
    all_points = range(n)
    memo = {}

    def visit(mask, pos):
        if (mask, pos) in memo:
            return memo[(mask, pos)]
        if mask == (1 << n) - 1:
            return graph[pos][start]
        ans = float('inf')
        for city in all_points:
            if mask & (1 << city) == 0:
                new_cost = graph[pos][city] + visit(mask | (1 << city), city)
                ans = min(ans, new_cost)
        memo[(mask, pos)] = ans
        return ans

    return visit(1 << start, start)


def display_tsp_results(st, cities, dist_matrix, shortest_distance):
    st.subheader(" Route Optimization ")
    st.write(f"**Shortest Route Distance:** {shortest_distance} units")

    st.subheader(" Route Distance Graph")
    fig, ax = plt.subplots()
    for i in range(len(cities)):
        for j in range(i+1, len(cities)):
            ax.plot([i, j], [dist_matrix[i][j], dist_matrix[j][i]], 'bo--')
    ax.set_xticks(range(len(cities)))
    ax.set_xticklabels(cities)
    ax.set_ylabel("Distance")
    st.pyplot(fig)
