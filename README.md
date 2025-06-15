# Glow care a Skincare Recommender System Based on Skin Problem Using Content-Based Filtering  

<div align="center">
<img src="Glowcare.jpg" alt="eCommerce" style="width:800px;height:500px;" align="center">
</div> 

<br>
Nowadays, skin care is becoming one of the most essential things in our lives. Skincare products have grown rapidly everywhere and tend to increase year by year. So do not be surprised if there are so many skin care products circulating in the community. However, the large number of product choices makes it difficult for people to choose the product that best suits their facial needs. Therefore, the author took the initiative to create a system that is able to recommend skin care products based on facial skin problems. In this study, the author uses the method of content-based filtering in making the recommendation system. This recommendation system is made without using rating data, so the algorithm approach used is cosine similarity and TF-IDF in finding similarity features. Then, the first output that appears will be used by the machine as historical data to then enter the content-based filtering stage. So, users will get recommendations according to the selected keywords and similar products.   
</br>

<br>
This website uses datasets scraped independently from various skincare product websites with details:  
<br></br>

| Feature Name | Description | 
| --- | --- | 
|**product_href** | Product URL link |
|**product_name** | Product name |
|**product_type** |Type of product (Facial wash, Toner, Serum, Moisturizer, Sunscreen) |
|**brand** | Product brand |
|**notable_effects** | What it's good for |
|**skin type** | The suitable type of skin for the product (Normal, Dry, Oily, Combination, Sensitive) |
|**price** | Product price (in IDR Rp) |
|**description** | Product description |
|**picture_src** | Product image URL link |

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
