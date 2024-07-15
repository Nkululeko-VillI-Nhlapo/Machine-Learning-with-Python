# Linear Regression Health Costs Calculator
### Nhlapo Nkululeko
<hr>

## Introduction
Welcome to the **Linear Regression Health Costs Calculator** project. This project demonstrates the application of neural networks to predict medical expenses based on various patient data. This project is part of the FreeCodeCamp Machine Learning certification.
- We build a linear regression model using a neural network. A neural network is  configured to perform linear regression by designing it with the appropriate architecture and activation functions.

[Full Model Code (Click Here)](https://github.com/Nkululeko-VillI-Nhlapo/Machine-Learning-with-Python/blob/main/Linear%20Regression%20Health%20Costs%20Calculator/Nhlapo_predict_health_costs_with_regression.ipynb)

## Project Overview
- **Objective**: The primary goal of this project was to develop a predictive model that  predict medical expenses based on various demographic and lifestyle factors using a neural network model.
- **Dataset**: We used a dataset containing information such as age, sex, BMI, number of children, smoking status, region, and medical expenses. This dataset was crucial for training and evaluating our predictive model.


## Tool Used
- Python, Tensorflow, Keras, Pandas, Matplotlib

### Objective:
1. **Problem Statement:** The objective was to build a model that accurately predicts medical expenses based on individual characteristics.
2. **Importance:** Predicting medical expenses can help insurance companies better assess risk and tailor premiums accordingly, as well as aid individuals in financial planning.

## Methodology

### Data Preprocessing
1. **Data Cleaning and Preparation**:
   - We began by preprocessing the dataset, handling missing values, encoding categorical variables like sex, smoker status, and region, and scaling numerical features like age and BMI to ensure the neural network could effectively learn from the data.

### Model Development
2. **Neural Network Construction**:
   - Constructed a neural network architecture using TensorFlow and Keras.
   - Designed the neural network with multiple layers, including dense layers with ReLU activation functions to capture non-linear relationships in the data and also learn complex patterns between input features and medical expenses.

### Model Training
3. **Training the Model**:
   - The dataset was split into training and testing sets. The model was trained using the training data, where it learned to minimize the Mean Absolute Error (MAE) loss function, indicating how well predictions matched actual expenses.

### Model Evaluation
4. **Evaluating the Model**:
   - We evaluated the model's performance on the test set, achieving a Mean Absolute Error (MAE) of approximately 2078.07, which indicates that our model predicts medical expenses with a reasonable degree of accuracy.

## Results and Performance

### Performance Metrics
- The model achieved an MAE of 2078.07 on the test dataset, indicating that, on average, predictions were within $2078.07 of the actual expense values.

**Key Findings** The neural network effectively learned relationships between input features (such as age, BMI, smoking status) and medical expenses.
**Generalization:** Our model generalizes well to unseen data, as evidenced by its performance on the test set.
**Implications:** These results suggest that predictive models can assist in estimating medical costs, potentially optimizing insurance pricing and assisting individuals in financial planning.
### Visualizing Predictions
- Plotted the predicted expenses against the true values to visualize the model's performance, showing a strong correlation between predicted and actual expenses.

## Conclusion
In conclusion, this project illustrates my capability to apply machine learning techniques to real-world financial prediction tasks effectively. By leveraging neural networks and rigorous data preprocessing, I've developed a robust model for predicting expenses with considerable accuracy. This project not only showcases technical proficiency but also highlights my ability to handle complex datasets and deliver actionable insights through machine learning.

## Next Steps
Moving forward, I aim to enhance this project by exploring advanced neural network architectures, incorporating more features, and possibly deploying the model in a production environment for real-time expense predictions.



