# Glow care 

<div align="center">
<img src="Glowcare.jpg" alt="eCommerce" style="width:800px;height:500px;" align="center">
</div> 

# SkinCare Recommendation System

With skincare becoming an increasingly important part of daily life, the number of products available on the market has grown significantly. This abundance, while offering variety, often creates confusion for consumers trying to find products that truly match their individual skin concerns. To address this, we present a content-based skincare product recommendation system that helps users discover suitable products based on their specific skin needs.

This web-based recommendation system is built using a **content-based filtering approach**. Unlike collaborative filtering, it does not rely on user ratings or reviews. Instead, it uses **TF-IDF (Term Frequency-Inverse Document Frequency)** and **cosine similarity** to measure the relevance between product features and the user’s selected keyword. The system identifies similar products based on descriptive attributes and recommends the closest matches.

The recommendation process works in two stages. First, it identifies the most relevant product based on user input. This result is then used as historical data to generate a list of similar products using content-based filtering, ensuring that users receive suggestions tailored to their preferences.

The dataset used for this system was independently scraped from multiple skincare product websites. Each product entry includes several key attributes:

Each product is defined by its URL, name, type (e.g., facial wash, toner, serum, moisturizer, or sunscreen), brand, key benefits or notable effects, and recommended skin type (such as normal, dry, oily, combination, or sensitive). Additional data includes product price (in Indonesian Rupiah), a textual description of the product, and a link to the product image.

This recommendation engine enables users to explore and choose skincare products with greater confidence and personalization—delivering results that align with their specific skin concerns and preferences.

# Data Overview  

<br>
### Why Use GlowCare?

GlowCare is a smart recommendation system that helps you find skin care products tailored to your unique skin type and concerns. It's built to simplify the overwhelming choices in the skincare world.

- Explore over 1,200 carefully curated products from various trusted brands
- Filter by skin type, skin concerns, and desired benefits
- Backed by a machine learning engine that understands your needs
- Offers clear, personalized product suggestions based on your selections


<br>
### About the Data

The product dataset contains 1,224 entries that were carefully scrapped and organized to ensure clarity and consistency.

- All entries are clean with no missing values
- 14 duplicate rows were identified and removed
- The dataset covers five major product types, with serums being the most popular
- About 150 products offer a combination of benefits including pore care, brightening, and anti-aging
- A significant number of products are formulated for oily skin types, reflecting market demand
<br>>


### How GlowCare Works

GlowCare uses a content-based filtering approach powered by machine learning.

1. You select your skin type, problems, and desired effects
2. The system compares your input with product descriptions using TF-IDF vectorization
3. It calculates product similarity and recommends the most relevant options

This approach ensures that you receive personalized results even if you've never used the products before.



### Tips for Best Use

- Be specific with your choices to improve recommendation accuracy
- Try exploring different product categories and effects
- Visit the "Skin Care 101" section to learn more about effective skincare routines





# App  
App in overall  
<br>
<img width="881" alt="image" src="home1.jpg">
<br>
<img width="881" alt="image" src="home2.jpg">
----
<img width="857" alt="image" src="recommendation.jpg">
<br>
-----
<img width="856" alt="image" src="skincare.jpg">
<br>

Thank You!
