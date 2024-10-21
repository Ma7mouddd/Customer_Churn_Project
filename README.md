Customer Churn Prediction

Overview

This project aims to predict customer churn by analyzing various customer attributes such as demographics, usage patterns, and payment behavior. Understanding and predicting customer churn helps companies reduce revenue loss by improving customer retention strategies. Machine learning models like LightGBM and Gradient Boosting Classifier have been implemented to provide accurate churn predictions.

Features

Data Analysis: Exploratory data analysis (EDA) using libraries such as matplotlib and seaborn for visualizations.
Churn Prediction: Predict customer churn using machine learning algorithms, including Gradient Boosting Classifier, LightGBM, and AdaBoost.
Model Evaluation: Various metrics like Accuracy, Precision, Recall, and ROC-AUC were used to evaluate model performance. The LightGBM model achieved the highest accuracy of 93.6% and an ROC-AUC score of 0.992.
Real-time Prediction: A Streamlit dashboard allows users to input customer data and predict churn in real time.
Dataset
The dataset contains customer information with the following key features:


CustomerID: Unique identifier for each customer.
Age: Age of the customer.
Gender: Gender of the customer.
Tenure: The duration (in months) the customer has been subscribed to the service.
Usage Frequency: How often the customer uses the service.
Support Calls: Number of calls the customer made to customer support.
Payment Delay: Instances of payment delays by the customer.
Subscription Type: The subscription plan (e.g., Basic, Standard, Premium).
Contract Length: The length of the customer's contract (Monthly, Quarterly, Annual).
Total Spend: Total amount spent by the customer.
Last Interaction: The last recorded interaction with the customer.
Churn: Indicates if the customer has churned (1 = Yes, 0 = No).

Installation

To run this project, ensure you have the following libraries installed:


pip install matplotlib seaborn pandas scikit-learn numpy

Usage

Open the Jupyter notebook:

jupyter notebook customer_churn_analysis.ipynb

3.Run the Streamlit dashboard for real-time predictions:

streamlit run Customer_Churn_Streamlit.py

Follow the notebook's steps to explore the data, visualize customer segments, and understand churn indicators.

Machine Learning Models

We have explored several machine learning algorithms, and the performance of each model is evaluated using various metrics:

Gradient Boosting Classifier:

Accuracy: 93.1%
ROC-AUC: 0.990

LightGBM:

Accuracy: 93.6%
ROC-AUC: 0.992

AdaBoost Classifier:

Accuracy: 93.1%
ROC-AUC: 0.989

Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes or suggestions.

License

This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgements

Libraries: matplotlib, seaborn, scikit-learn, pandas, numpy

Special thanks to the community for inspiration and dataset resources.
