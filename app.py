import streamlit as st
from streamlit_option_menu import option_menu
from numpy.core.fromnumeric import prod
#import tensorflow as tf
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from PIL import Image

# Import the Dataset 
skincare = pd.read_csv("export_skincare.csv", encoding='utf-8', index_col=None)

# Header
st.set_page_config(page_title="Glowcare", page_icon=":sunflower:", layout="wide",)
st.markdown(
    """
    <style>
        .stApp {
            background-color: #e6f0ff;
        }
    </style>
    """,
    unsafe_allow_html=True
)


# 1=sidebar menu, 2=horizontal menu, 3=horizontal menu w/ custom menu
EXAMPLE_NO = 2

def streamlit_menu(example=1):
    if example == 1:
        # 1. as sidebar menu
        with st.sidebar:
            selected = option_menu(
                menu_title="Main Menu",  # required
                options=["Glowcare", "Product Recommendation", "Skincare"],  # required
                icons=["house", "stars", "book"],  # optional
                menu_icon="cast",  # optional
                default_index=0,  # optional
            )
        return selected

    if example == 2:
        # 2. horizontal menu without custom style
        selected = option_menu(
            menu_title=None,  # required
            options=["Skin Care", "Get Recommendation", "Skin Care 101"],  # required
            icons=["house", "stars", "book"],  # optional
            menu_icon="cast",  # optional
            default_index=0,  # optional
            orientation="horizontal",
        )
        return selected

    if example == 3:
        # 3. horizontal menu with custom style
        selected = option_menu(
            menu_title=None,  # required
            options=["Skin Care", "Get Recommendation", "Skin Care 101"],  # required
            icons=["house", "stars", "book"],  # optional
            menu_icon="cast",  # optional
            default_index=0,  # optional
            orientation="horizontal",
            styles={
                "container": {"padding": "0!important", "background-color": "#fafafa"},
                "icon": {"color": "black", "font-size": "25px"},
                "nav-link": {
                    "font-size": "25px",
                    "text-align": "left",
                    "margin": "0px",
                    "--hover-color": "#eee",
                },
                "nav-link-selected": {"background-color": "green"},
            },
        )
        return selected


selected = streamlit_menu(example=EXAMPLE_NO)

if selected == "Skin Care":
    st.title(f"{selected} Glowcare :sparkles:")
    st.write('---') 

    st.write(
        """
        ##### **This Skin Care Product Recommendation Application is an implementation of Machine Learning that recommends skin care products based on your skin type and concerns.**
        """)
    
    # displaying a local video file
    video_file = open("skincare.mp4", "rb").read()
    st.video(video_file, start_time = 1)  # displaying the video 
    
    st.write(' ') 
    st.write(' ')
    st.write(
        """
        ##### You will get recommendations from over 1200+ products across various cosmetic brands tailored to your skin needs.
        ##### There are 5 categories of skin care products, 5 skin types, and various concerns and benefits to choose from. This recommendation tool is just a system based on your input — not professional consultation.
        ##### Go to the *Get Recommendation* page to start, or view *Skin Care 101* for skin care tips and guidance.
        """)
    st.write('---')

st.markdown("""
### 🌟 Why Use GlowCare?

GlowCare is your smart skincare buddy that helps you discover products tailored to your unique skin profile — no confusion, no wasted money.

- 🧴 **Explore 1200+ curated skincare products** from top brands
- 🔍 **Filter by skin type, problems, and goals** (acne, anti-aging, etc.)
- 🤖 **AI-powered** recommendations using machine learning
- 🛍️ Personalized suggestions — just like shopping with a beauty expert
""")

st.markdown("""
### 🧠 How It Works

GlowCare uses content-based filtering, meaning it analyzes product benefits (not ratings) and compares them to your needs.

1. You choose your **skin type**, **concerns**, and **desired effects**
2. GlowCare compares these to the product database using **TF-IDF + cosine similarity**
3. You get **5 intelligent recommendations** based on your selected product
""")

st.markdown("""
### 💡 Tips to Get the Best Results

- Be specific with your selections — choose multiple skin concerns and benefits
- Try out different product categories (e.g., serum, toner)
- Check the **Skin Care 101** tab to build your daily routine
""")

st.markdown("""
---
Ready to glow? ✨  
Head to **Get Recommendation** and start your skincare journey with GlowCare!
""")


if selected == "Get Recommendation":
    st.title(f"Let's {selected}")
    
    st.write(
        """
        ##### **To get recommendations, please enter your skin type, concerns, and desired effects to get the most suitable products**
        """) 
    
    st.write('---') 

    first,last = st.columns(2)

    # Choose a product type category
    category = first.selectbox(label='Product Category : ', options= skincare['product_type'].unique() )
    category_pt = skincare[skincare['product_type'] == category]

    # Choose a skin type
    skin_type = last.selectbox(label='Your Skin Type : ', options= ['Normal', 'Dry', 'Oily', 'Combination', 'Sensitive'] )
    category_st_pt = category_pt[category_pt[skin_type] == 1]

    # Choose skin concerns
    prob = st.multiselect(label='Skin Problems : ', options= ['Acne', 'Hyper pigmentation', 'Acne Scars','Dark spots', 'Dark circles', 'Fine Lines and Wrinkles', 'Blackheads', 'Uneven Skin Tone', 'Redness', 'Sagging Skin'] )

    # Choose notable_effects
    # From the filtered data based on product type and skin type, we take unique values of notable_effects
    opsi_ne = category_st_pt['notable_effects'].unique().tolist()
    # These unique notable_effects are shown as options in a multiselect field
    selected_options = st.multiselect('Notable Effects : ',opsi_ne)
    # Filter again based on selected notable_effects
    category_ne_st_pt = category_st_pt[category_st_pt["notable_effects"].isin(selected_options)]

    # Choose product
    # Filter unique product names from filtered dataset
    opsi_pn = category_ne_st_pt['product_name'].unique().tolist()
    # Create a selectbox for product selection
    product = st.selectbox(label='Recommended Product for You', options = sorted(opsi_pn))

    ## MODELING with Content Based Filtering
    # Initialize TfidfVectorizer
    tf = TfidfVectorizer()

    # Fit the vectorizer on the 'notable_effects' data
    tf.fit(skincare['notable_effects']) 

    # Get feature names
    tf.get_feature_names_out()

    # Transform the data into tf-idf matrix
    tfidf_matrix = tf.fit_transform(skincare['notable_effects']) 

    # View matrix shape
    shape = tfidf_matrix.shape

    # Convert matrix to dense format
    tfidf_matrix.todense()

    # Create dataframe from the tf-idf matrix
    pd.DataFrame(
        tfidf_matrix.todense(), 
        columns=tf.get_feature_names_out(),
        index=skincare.product_name
    ).sample(shape[1], axis=1).sample(10, axis=0)

    # Compute cosine similarity
    cosine_sim = cosine_similarity(tfidf_matrix) 

    # Create a DataFrame from the cosine similarity matrix with product names as index and columns
    cosine_sim_df = pd.DataFrame(cosine_sim, index=skincare['product_name'], columns=skincare['product_name'])

    # View similarity matrix
    cosine_sim_df.sample(7, axis=1).sample(10, axis=0)

    # Define a function to get recommendations
    def skincare_recommendations(nama_produk, similarity_data=cosine_sim_df, items=skincare[['product_name', 'brand', 'description']], k=5):

        # Find the k most similar items using argpartition
        index = similarity_data.loc[:,nama_produk].to_numpy().argpartition(range(-1, -k, -1))

        # Select top-k similar items
        closest = similarity_data.columns[index[-1:-(k+2):-1]]

        # Remove the selected product itself
        closest = closest.drop(nama_produk, errors='ignore')
        df = pd.DataFrame(closest).merge(items).head(k)
        return df

    # Button to show recommendations
    model_run = st.button('Find Other Recommended Products!')
    
    if model_run:
        st.write('Here are similar product recommendations based on your choice')
        st.write(skincare_recommendations(product))
    
    
if selected == "Skin Care 101":
    st.title(f"Take a Look at {selected}")
    st.write('---') 

    st.write(
        """
        ##### **Here are tips and tricks to help you maximize your skincare routine**
        """) 
    
    image = Image.open('imagepic.jpg')
    st.image(image, caption='Skin Care 101')

    st.write("### **1. Facial Wash**")
    st.write("**- Use a facial wash that suits your skin or is recommended for you**")
    st.write("**- Wash your face at most twice daily — in the morning and before bed. Overwashing can strip natural oils. Dry skin? Morning rinse with water is fine.**")
    st.write("**- Don’t scrub harshly — it can damage your skin barrier**")
    st.write("**- Cleanse using fingertips in circular motions for 30–60 seconds**")

    st.write("### **2. Toner**")
    st.write("**- Use a toner that suits your skin or is recommended**")
    st.write("**- Apply with a cotton pad, then layer again with hands for better absorption**")
    st.write("**- Apply toner after cleansing**")
    st.write("**- Sensitive skin? Avoid toners with fragrance**")

    st.write("### **3. Serum**")
    st.write("**- Choose a serum that suits your goals: anti-acne, brightening, anti-aging, etc.**")
    st.write("**- Apply to clean skin for better absorption**")
    st.write("**- Use morning and night**")
    st.write("**- Pat into the skin gently and wait until absorbed**")

    st.write("### **4. Moisturizer**")
    st.write("**- Use a moisturizer that fits your skin type**")
    st.write("**- Moisturizer locks in hydration and nutrients from your serum**")
    st.write("**- Use a different moisturizer for day (with SPF) and night (with actives)**")
    st.write("**- Wait 2–3 minutes after serum before applying**")

    st.write("### **5. Sunscreen**")
    st.write("**- Use a sunscreen suited for your skin**")
    st.write("**- This is the most crucial step to protect your skin from UVA/UVB/light blue rays**")
    st.write("**- Use 2 fingers worth of product**")
    st.write("**- Reapply every 2–3 hours**")
    st.write("**- Wear sunscreen indoors too — sunlight still enters through windows**")

    st.write("### **6. Avoid Changing Products Often**")
    st.write("**Frequent switching stresses the skin. Stay consistent with products for best results.**")

    st.write("### **7. Be Consistent**")
    st.write("**Skincare is about consistency — not instant results.**")

    st.write("### **8. Your Face is Your Asset**")
    st.write("**Treat your face with care and gratitude. Proper skincare is a long-term investment.**")
