# 🎬 Movie Recommendation System

Welcome to the Movie Recommendation System project! This repository contains the code and files for building a content-based movie recommendation system using Jupyter Notebook and deploying it with Streamlit.
[![Movie Recommendation System](https://i.ibb.co/Kqcx3XX/Capture.png)](https://ibb.co/R0GTV99)

## 📁 Project Structure

```
├── Jupyter Notebook
│   └── movie-recommendation-system.ipynb
├── Streamlit Files
│   ├── app.py
│   └── movies.pkl
└── README.md
```

## 📝 Project Overview

The Movie Recommendation System is designed to provide personalized movie recommendations to users based on their preferences and past interactions with movies. The recommendation system uses content-based filtering, leveraging movie attributes such as genres, keywords, cast, and crew to suggest similar movies.

## 🚀 Setup Instructions

1. Clone the repository to your local machine:

```bash
git clone https://github.com/I-AdityaGoyal/Movie_Recommendation_System.git
```

2. Change into the project directory:

```bash
cd movie-recommendation-system
```

3. Run the Jupyter Notebook:

```bash
jupyter notebook
```

4. Open the `movie-recommendation-system.ipynb` notebook in Jupyter and follow the instructions to explore the project, analyze data, train the model, and generate movie recommendations.

5. After running the notebook, two files will be generated: `movies.pkl` and `similar.pkl`. These files contain the processed movie data and the similarity information, respectively.


6. You can use these downloaded files for deploying the Streamlit app and generating movie recommendations.

7. To run the Streamlit app

```bash
streamlit run app.py
```

8. Open your web browser and visit `http://localhost:8501` to access the Movie Recommendation System web application.


Feel free to explore the code, experiment with the data, and make improvements to the recommendation system! If you have any questions or feedback, please don't hesitate to reach out. Happy movie watching! 🍿🎉
