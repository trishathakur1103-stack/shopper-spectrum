import streamlit as st
import joblib

similarity_df = joblib.load("similarity_matrix.pkl")

st.title("🎁 Product Recommendation")

product = st.text_input("Enter Product Name")

def recommend_products(product_name, top_n=5):

    if product_name not in similarity_df.index:
        return None

    recommendations = (
        similarity_df[product_name]
        .sort_values(ascending=False)
        .iloc[1:top_n+1]
    )

    return recommendations.index.tolist()

if st.button("Recommend"):

    products = recommend_products(product)

    if products is None:
        st.error("Product not found!")

    else:
        st.subheader("Top 5 Recommended Products")

        for i, item in enumerate(products, start=1):
            st.success(f"{i}. {item}")