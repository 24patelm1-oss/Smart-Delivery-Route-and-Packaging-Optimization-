import streamlit as st
import pandas as pd
import time

from merge_sort_task import merge_sort, display_merge_sort_results
from knapsack_task import fractional_knapsack, display_knapsack_results
from tsp_task import tsp, display_tsp_results

st.set_page_config(page_title="Smart Delivery Optimizer", page_icon="🚚", layout="centered")

st.title("🚚 Smart Delivery Route & Packaging Optimization System")

# User Inputs
num_packages = st.number_input("Enter number of packages", min_value=2, max_value=10, value=5)
truck_capacity = st.number_input("Enter Truck Capacity (kg)", min_value=10, max_value=100, value=50)

profits, weights = [], []
for i in range(num_packages):
    col1, col2 = st.columns(2)
    with col1:
        profit = st.number_input(f"Profit of Package {i+1}", min_value=1, max_value=100, value=10*(i+1))
    with col2:
        weight = st.number_input(f"Weight of Package {i+1}", min_value=1, max_value=50, value=5*(i+1))
    profits.append(profit)
    weights.append(weight)

if st.button(" Optimize Delivery"):
    start_time = time.time()

    packages = list(zip(profits, weights))
    ratios = [p/w for p, w in packages]
    package_data = pd.DataFrame({
        'Package': [f'P{i+1}' for i in range(num_packages)],
        'Profit': profits,
        'Weight': weights,
        'Profit/Weight Ratio': ratios
    })

    # --- Task 1 ---
    sorted_data = merge_sort(list(zip(ratios, profits, weights)))
    display_merge_sort_results(st, package_data)

    # --- Task 2 ---
    max_profit, selected_items = fractional_knapsack(truck_capacity, sorted_data)
    display_knapsack_results(st, package_data, max_profit, selected_items)

    # --- Task 3 ---
    cities = ["Warehouse", "City A", "City B", "City C"]
    dist_matrix = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    shortest_distance = tsp(dist_matrix, 0)
    display_tsp_results(st, cities, dist_matrix, shortest_distance)

    # --- Total Time ---
    end_time = time.time()
    total_time = end_time - start_time
    st.metric(label="⏱️ Total Time Taken (seconds)", value=f"{total_time:.4f}")
    st.success(" Smart Delivery Optimization Completed Successfully!")
