import streamlit as st
import random
import time
import sys


def insertion_sort(arr):
    """Sorts an array using Insertion Sort."""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def selection_sort(arr):
    """Sorts an array using Selection Sort."""
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def test_sort(sort_func, arr):
    """Measures the execution time and space complexity of a sorting function."""
    start_time = time.time()
    sorted_arr = sort_func(arr.copy())
    end_time = time.time()
    space_complexity = sys.getsizeof(sorted_arr) / (1024 * 1024)  # Convert to MB
    return sorted_arr, end_time - start_time, space_complexity


def main():
    st.title("Sorting Algorithm Comparison")

    size = st.number_input("Enter array size:", min_value=1, step=1, value=10)
    sort_button = st.button("Run Comparison")

    if sort_button:
        arr = [random.randint(0, 1000) for _ in range(size)]

        with st.spinner("Running comparison..."):
            insertion_result = test_sort(insertion_sort, arr)
            selection_result = test_sort(selection_sort, arr)

        st.success("Comparison completed successfully.")

        st.write("### Insertion Sort:")
        st.write(f"Time: {insertion_result[1]:.4f} seconds")
        st.write(f"Space Complexity: {insertion_result[2]:.4f} MB")
        st.write("Sorted Array:", insertion_result[0])

        st.write("### Selection Sort:")
        st.write(f"Time: {selection_result[1]:.4f} seconds")
        st.write(f"Space Complexity: {selection_result[2]:.4f} MB")
        st.write("Sorted Array:", selection_result[0])


if __name__ == "__main__":
    main()