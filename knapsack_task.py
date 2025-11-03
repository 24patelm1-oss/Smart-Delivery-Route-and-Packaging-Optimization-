import matplotlib.pyplot as plt
import pandas as pd

def fractional_knapsack(capacity, items):
    total_profit = 0
    selected = []
    for ratio, profit, weight in items:
        if capacity <= 0:
            break
        if weight <= capacity:
            capacity -= weight
            total_profit += profit
            selected.append((profit, weight, 1))
        else:
            fraction = capacity / weight
            total_profit += profit * fraction
            selected.append((profit, weight, fraction))
            break
    return total_profit, selected

def display_knapsack_results(st, package_data, max_profit, selected_items):
    st.subheader(" Package Selection")
    st.write(f"*Maximum Profit:* {max_profit:.2f}")
    st.write(f"*Selected Items (Profit, Weight, Fraction):* {selected_items}")

    # Cumulative Profit Graph
    st.subheader("Cumulative Profit Graph")
    sorted_df = package_data.sort_values(by='Profit/Weight Ratio', ascending=False)
    sorted_df['Cumulative Profit'] = sorted_df['Profit'].cumsum()
    fig1, ax1 = plt.subplots()
    ax1.plot(sorted_df['Package'], sorted_df['Cumulative Profit'], marker='o')
    ax1.set_xlabel("Packages (sorted by ratio)")
    ax1.set_ylabel("Cumulative Profit")
    st.pyplot(fig1)

    # Profit Contribution Pie Chart
    st.subheader("Profit Contribution Pie Chart")
    fig2, ax2 = plt.subplots()
    ax2.pie(package_data['Profit'], labels=package_data['Package'], autopct='%1.1f%%')
    st.pyplot(fig2)
