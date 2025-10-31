# 🎬 Lucky – The Movie Recommendation System  

**Developer:** Debashish Parida (debashish-5)  
**Internship Project:** Elevate Lab  
**Domain:** Full Stack Machine Learning  

---

##  Overview  

**Lucky** is an intelligent **Movie Recommendation System** that suggests movies based on user preferences and movie similarity analysis.  
It uses **Machine Learning (Content-Based Filtering and Cosine Similarity)** to understand relationships between movies and deliver personalized recommendations.  
The project integrates a complete **Full Stack ML pipeline** — from data preprocessing to web deployment — inside one application.  

---

##  Features  

- Personalized movie recommendations  
- Machine Learning–powered backend (Python + Flask)  
- Responsive frontend built using HTML, CSS, and JavaScript  
- Preprocessed and cleaned movie data for better accuracy  
- Content-based filtering with cosine similarity  
- Organized project structure with modular components  

---

## Project Structure  

```
movies recommendation.zip
│
├── app.py                          # Flask backend for ML integration
├── index.html                      # Frontend web interface
├── style.css                       # Frontend styling
├── cleaned_movie_metadata.csv       # Preprocessed movie dataset
├── cleaned_first_hero_name.csv      # Additional feature dataset
├── sample.csv                      # Test sample file
│
├── Credit Data Analysis & Preprocessing.ipynb
├── Movies Data Analysis & Cleaning.ipynb
├── Data Visualization.ipynb
├── ML.ipynb                        # Model building and testing notebook
├── 1_heroname.pkl      |
├── 1_model.pkl         |
├── 2_genre.pkl         |
├── 2_model.pkl         |  JOBLIB FILE
├── 3_title.pkl         |
├── 3_model.pkl         |
├── 4_model.pkl         |
├── 5_model.pkl         |
├── Screenshot 2025-10-25 131049.png
├── Screenshot 2025-10-25 132050.png
├── Screenshot 2025-10-25 132234.png
├── IMG_20251025_085227.jpg         # Preview or demo image
│
└── .gitattributes                  # Git LFS configuration for large files
```

---

## Tech Stack  

| Component | Technology |
|------------|-------------|
| **Programming Language** | Python, JavaScript |
| **Frameworks** | Flask |
| **Frontend** | HTML, CSS, JavaScript |
| **Machine Learning** | Pandas, NumPy, Scikit-learn, Tensorflow |
| **Visualization** | Matplotlib, Seaborn,PowerBI |
| **Version Control** | Git & GitHub (LFS for large files) |

---

## How to Run  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/debashish-5/Lucky-Movie-Recommendation.git
cd Lucky-Movie-Recommendation
```

### 2️⃣ Unzip the Project Files  
Extract the contents of `movies recommendation.zip` inside the project folder.

### 3️⃣ Install Dependencies  
```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Flask App  
```bash
python app.py
```

Then open your browser and visit:  
👉 **http://127.0.0.1:5000/**  

---

## Dataset Information  

The dataset used in this project contains details such as:  
- Movie titles  
- Genres  
- Cast & crew  
- Overview/description  
- Popularity and ratings  

It is preprocessed and cleaned using Python (Pandas, NumPy) to remove duplicates, null values, and inconsistencies.  

---

## Model Overview  

The **Lucky Model** uses:  
- **Content-Based Filtering:** To recommend similar movies based on features.  
- **Cosine Similarity:** To calculate similarity between movie feature vectors.  

---

## Results  

- Generates **top 10 most similar movies** for a selected film.  
- Smooth and responsive web interface for real-time recommendations.  
- Deployed locally via Flask backend integration.  

---

## Future Enhancements  

- Add **Collaborative Filtering** for user-based recommendations.  
- Include **user ratings & feedback system**.  
- Deploy on **Render / AWS / Hugging Face Spaces**.  
- Integrate with **TMDB API** for live movie data.  

---

## Conclusion  

**Lucky** combines **Data Science**, **Machine Learning**, and **Web Development** to create a smart, interactive, and scalable recommendation platform.  
It represents the final project milestone of my **internship at Elevate Lab**, reflecting the application of practical ML and full-stack principles in real-world use.

---

## Contact  

**👤 Debashish Parida**  
📩 Email: ddebashishparida@gmail.com  
🔗 GitHub: [debashish-5](https://github.com/debashish-5)  
💼 LinkedIn: [Debashish Parida](https://www.linkedin.com/in/debashish-parida-a260b1355)  

---

⭐ *“Lucky doesn’t just suggest movies — it understands your choices.”* 🎬🍀
