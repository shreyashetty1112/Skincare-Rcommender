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
st.set_page_config(page_title="Skin Care Product Recommendation App", page_icon=":blossom:", layout="wide",)

# Display the main page
st.title("Glowcare :sparkles:")

st.write('---') 

# Displaying a local video file
video_file = open("skincare.mp4", "rb").read()
st.video(video_file, start_time = 1)  # displaying the video 

st.write('---') 

st.write(
    """
    ##### **The Skin Care Product Recommendation App is a Machine Learning project implementation that provides recommendations for skin care products based on your skin type and concerns. You can enter your skin type, issues, and desired effects to get the most suitable product recommendations.**
    """)  
st.write('---') 

first,last = st.columns(2)

# Choose a product type category
category = first.selectbox(label='Product Category : ', options= skincare['tipe_produk'].unique() )
category_pt = skincare[skincare['tipe_produk'] == category]

# Choose a skin type
skin_type = last.selectbox(label='Your Skin Type : ', options= ['Normal', 'Dry', 'Oily', 'Combination', 'Sensitive'] )
category_st_pt = category_pt[category_pt[skin_type] == 1]

# Select concerns
prob = st.multiselect(label='Your Skin Problems : ', options= ['Kulit Kusam', 'Jerawat', 'Bekas Jerawat','Pori-pori Besar', 'Flek Hitam', 'Garis Halus dan Kerutan', 'Komedo', 'Warna Kulit Tidak Merata', 'Kemerahan', 'Kulit Kendur'] )

# Choose notable_effects
# From the products already filtered by product type and skin type (category_st_pt), we get the unique values from the notable_effects column
opsi_ne = category_st_pt['notable_effects'].unique().tolist()
# The unique notable_effects are stored in opsi_ne and used in the multiselect options below in selected_options
selected_options = st.multiselect('Desired Effects : ',opsi_ne)
# The selected_options result is filtered and stored in category_ne_st_pt
category_ne_st_pt = category_st_pt[category_st_pt["notable_effects"].isin(selected_options)]

# Choose product
# Products that have been filtered in filtered_df are then further filtered for unique product_name values and stored in opsi_pn
opsi_pn = category_ne_st_pt['product_name'].unique().tolist()
# Create a selectbox with filtered product options above
product = st.selectbox(label='Recommended Product for You', options = sorted(opsi_pn))
# The product variable will hold a product and show similar recommendations

## MODELLING with Content Based Filtering
# Initialize TfidfVectorizer
tf = TfidfVectorizer()

# Perform idf calculation on the 'notable_effects' column
tf.fit(skincare['notable_effects']) 

# Mapping array from integer feature index to feature name
tf.get_feature_names()

# Fit then transform to matrix form
tfidf_matrix = tf.fit_transform(skincare['notable_effects']) 

# Check matrix size
shape = tfidf_matrix.shape

# Convert the tf-idf vector to a dense matrix
tfidf_matrix.todense()

# Create a dataframe to view the tf-idf matrix
# Columns contain desired effects
# Rows contain product names
pd.DataFrame(
    tfidf_matrix.todense(), 
    columns=tf.get_feature_names(),
    index=skincare.product_name
).sample(shape[1], axis=1).sample(10, axis=0)

# Calculate cosine similarity on the tf-idf matrix
cosine_sim = cosine_similarity(tfidf_matrix) 

# Create a dataframe from cosine_sim with rows and columns as product names
cosine_sim_df = pd.DataFrame(cosine_sim, index=skincare['product_name'], columns=skincare['product_name'])

# View similarity matrix for each product name
cosine_sim_df.sample(7, axis=1).sample(10, axis=0)

# Function to get recommendations
def skincare_recommendations(nama_produk, similarity_data=cosine_sim_df, items=skincare[['product_name', 'produk-href','price', 'description']], k=5):
    
    # Use argpartition to indirectly partition along a given axis    
    # Convert dataframe to numpy
    # Range(start, stop, step)
    index = similarity_data.loc[:,nama_produk].to_numpy().argpartition(range(-1, -k, -1))
    
    # Get data with highest similarity from the index
    closest = similarity_data.columns[index[-1:-(k+2):-1]]
    
    # Drop the selected product name so it doesn't appear in the recommendations
    closest = closest.drop(nama_produk, errors='ignore')
    df = pd.DataFrame(closest).merge(items).head(k)
    return df

# Create a button to show recommendations
model_run = st.button('Find Other Recommended Products!')
# Get recommendations
if model_run:
    st.write('Here are some other product recommendations based on your selection')
    st.write(skincare_recommendations(product))
    st.snow()
