import streamlit as st
import numpy as np

st.set_page_config(page_title="Matrix Operations Tool", layout="centered")

st.title("🧮 Matrix Operations Tool")

st.write("Enter matrices (rows separated by `;`, elements separated by spaces). Example:")
st.code("1 2 3; 4 5 6; 7 8 9", language="text")


matrixA_text = st.text_area("Matrix A:")
matrixB_text = st.text_area("Matrix B:")

def parse_matrix(text):
    try:
        rows = text.strip().split(";")
        matrix = [list(map(float, row.split())) for row in rows]
        return np.array(matrix)
    except Exception:
        st.error("❌ Invalid matrix format. Use spaces for elements, ';' for rows.")
        return None

A = parse_matrix(matrixA_text)
B = parse_matrix(matrixB_text)



operation = st.selectbox(
    "Choose an operation:",
    ["Addition (A + B)", "Subtraction (A - B)", "Multiplication (A × B)",
     "Transpose", "Determinant"]
)

if st.button("Compute"):
    if operation == "Addition (A + B)":
        if A is not None and B is not None:
            if A.shape == B.shape:
                st.success("✅ Result (A + B):")
                st.write(A + B)
            else:
                st.error("❌ Matrices must have the same dimensions for addition.")

    elif operation == "Subtraction (A - B)":
        if A is not None and B is not None:
            if A.shape == B.shape:
                st.success("✅ Result (A - B):")
                st.write(A - B)
            else:
                st.error("❌ Matrices must have the same dimensions for subtraction.")

    elif operation == "Multiplication (A × B)":
        if A is not None and B is not None:
            if A.shape[1] == B.shape[0]:
                st.success("✅ Result (A × B):")
                st.write(np.dot(A, B))
            else:
                st.error("❌ Number of columns in A must equal rows in B for multiplication.")

    elif operation == "Transpose":
        choice = st.radio("Transpose which matrix?", ["A", "B"])
        if choice == "A" and A is not None:
            st.success("✅ Transpose of A:")
            st.write(A.T)
        elif choice == "B" and B is not None:
            st.success("✅ Transpose of B:")
            st.write(B.T)

    elif operation == "Determinant":
        choice = st.radio("Determinant of which matrix?", ["A", "B"])
        if choice == "A" and A is not None:
            if A.shape[0] == A.shape[1]:
                st.success(f"✅ det(A) = {np.linalg.det(A):.2f}")
            else:
                st.error("❌ Determinant only defined for square matrices.")
        elif choice == "B" and B is not None:
            if B.shape[0] == B.shape[1]:
                st.success(f"✅ det(B) = {np.linalg.det(B):.2f}")
            else:
                st.error("❌ Determinant only defined for square matrices.")
