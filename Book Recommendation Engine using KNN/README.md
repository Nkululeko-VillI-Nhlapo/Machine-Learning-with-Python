# Book Recommendation System using K-Nearest Neighbors (KNN)
### Nhalpo Nkululeko

Welcome to the Book Recommendation System project! This project utilizes the Book-Crossings dataset and the K-Nearest Neighbors (KNN) algorithm to recommend books based on user ratings.

[Full Model Code (Click Here)](https://github.com/Nkululeko-VillI-Nhlapo/Machine-Learning-with-Python/blob/main/Book%20Recommendation%20Engine%20using%20KNN/book_recommendation_knn.ipynb)

## Project Overview

### Dataset
The dataset used in this project is the Book-Crossings dataset, which includes:
- **1.1 million ratings** on a scale of 1-10
- **270,000 books**
- **90,000 users**

### Objective
The goal is to build a book recommendation system that can suggest similar books based on a given book title using the KNN algorithm.

## Steps Involved

### 1. Data Import and Cleaning
We start by importing the dataset, which consists of two CSV files:
- `BX-Books.csv`: Contains information about books.
- `BX-Book-Ratings.csv`: Contains ratings given by users to books.

### 2. Data Preparation
To ensure statistical significance, we filter out:
- Users with fewer than 200 ratings.
- Books with fewer than 100 ratings.

### 3. Data Structuring
We create a user-item matrix (`piv`) where:
- Rows represent books.
- Columns represent users.
- Each cell contains the rating given by a user to a book.

### 4. Model Training
Using the KNN algorithm from `sklearn.neighbors`, we train a model (`model_knn`) on the user-item matrix (`piv`) using cosine similarity as the distance metric.

### 5. Recommendation Function
We develop a function (`get_recommends(book)`) that:
- Takes a book title as input.
- Retrieves similar books based on the trained KNN model.
- Returns a list of recommended books sorted by similarity distance.

## K-Nearest Neighbors (KNN)

KNN is a simple and effective algorithm for recommendation systems. It finds books that are most similar to a given book by measuring the distance (cosine similarity) between their rating vectors in the user-item matrix.

## Functionality

The `get_recommends(book)` function leverages the pre-trained KNN model to provide recommendations based on user ratings similarity. It handles:
1. Extraction of rating vectors.
2. Computation of nearest neighbors.
3. Formatting of recommendations for output.

## Conclusion
The KNN algorithm works very well as implemented and it is able to recommend books that are similar to the one you want. We ran multiple tests on the main model code in the Jupyter file. **GO SEE**.

## Getting Started

### Prerequisites
Make sure you have the following libraries installed:
- `numpy`
- `pandas`
- `scipy`
- `scikit-learn`
- `matplotlib`

### Running the Project

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/book-recommendation-system.git
   cd book-recommendation-system

