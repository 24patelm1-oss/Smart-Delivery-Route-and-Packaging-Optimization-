import matplotlib.pyplot as plt
import pandas as pd

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i][0] > R[j][0]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr


def display_merge_sort_results(st, package_data):
    st.subheader("Sorting Delivery Requests")
    st.dataframe(package_data.sort_values(by='Profit/Weight Ratio', ascending=False))

    # Profit-to-Weight Ratio Graph
    st.subheader("Profit-to-Weight Ratio Graph")
    fig, ax = plt.subplots()
    ax.bar(package_data['Package'], package_data['Profit/Weight Ratio'])
    ax.set_xlabel("Packages")
    ax.set_ylabel("Profit/Weight Ratio")
    st.pyplot(fig)
