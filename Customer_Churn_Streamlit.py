

import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import KMeans

# Load dataset
file_path = 'combained_data.csv'  # Path to your uploaded dataset
combained_df = pd.read_csv(file_path)

# Function to add background image
def add_bg_from_url():
    st.markdown(
        f"""
        <style>
        .stApp {{ 
            background-image: url("https://i.pinimg.com/originals/c5/92/cd/c592cd7e5df0bfaa574011387f6e84e4.jpg");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        .title {{
            color: black;
            font-size: 2.5em;
        }}
        .subheader {{
            color: black;
            font-size: 1.5em;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
# Apply background image
add_bg_from_url()

# Display dataset on page load
st.markdown('<p class="title">Customer Churn Dashboard</p>', unsafe_allow_html=True)

# Sidebar
st.sidebar.title("Choose Visualization")
options = st.sidebar.selectbox("Select a visualization", [
    "None",  # Default option 
    "Contract Length Distribution (Pie Chart)",
    "Data Distribution (Histogram)",
    "3D Scatter Plot (Age, Total Spend, and Churn)",
    "K-Means Clustering (Tenure vs Total Spend)",
    "Subscription Type & Contract Length (Bar Plot)",
    "Total Spend by Gender & Churn (Box Plot)",
    "Contract Length by Gender & Churn (Bar Plot)",
    "Payment Delay by Churn Status (Box Plot)",
    "Subscription Type Pie Chart",
    "Churn Category Pie Chart",
    "Churn Distribution (Pie Chart)",
    "Tenure vs Churn Rate (Line Chart)",
    "Age vs Churn (Line Chart)",
    "Support Calls by Subscription Type and Churn Status",
    "Average Support Calls by Churn Status",
    "Total Spend vs. Contract Length (Scatter Plot)",
    "Churn Over Tenure (Line Chart)",
    "Average Last Interaction by Churn Status",
    "Correlation Heatmap (Support Calls, Churn, Payment Delay)",
    "Payment Delay Range (Customer Count)"
],
index=0
)

# Visualizations based on sidebar selection
if options == "None":
    st.markdown('<p class="subheader">Please select a visualization from the dropdown menu</p>', unsafe_allow_html=True)
elif options == "Contract Length Distribution (Pie Chart)":
    contract_length_counts = combained_df['Contract Length'].value_counts()
    fig, ax = plt.subplots()
    ax.pie(contract_length_counts, labels=contract_length_counts.index, autopct='%1.1f%%', colors=['lightblue', 'lightgreen', 'lightcoral', 'orange'])
    ax.set_title('Contract Length Distribution')
    st.pyplot(fig)

elif options == "Data Distribution (Histogram)":
    fig, ax = plt.subplots(figsize=(10, 8))
    combained_df.hist(ax=ax, edgecolor='black')
    plt.tight_layout()
    st.pyplot(fig)

elif options == "3D Scatter Plot (Age, Total Spend, and Churn)":
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    x = combained_df['Age']
    y = combained_df['Total Spend']
    z = combained_df['Churn']
    scatter = ax.scatter(x, y, z, c=z, cmap='coolwarm', marker='o')
    ax.set_xlabel('Age')
    ax.set_ylabel('Total Spend')
    ax.set_zlabel('Churn (0 or 1)')
    plt.title('3D Scatter Plot of Age, Total Spend, and Churn')
    fig.colorbar(scatter, ax=ax, label='Churn (0 = No, 1 = Yes)')
    st.pyplot(fig)

elif options == "K-Means Clustering (Tenure vs Total Spend)":
    # Handle missing values by dropping rows with NaNs
    X = combained_df[['Tenure', 'Total Spend']].dropna()
    kmeans = KMeans(n_clusters=3, random_state=0)
    combained_df.loc[X.index, 'Cluster'] = kmeans.fit_predict(X)
    
    fig, ax = plt.subplots()
    sns.scatterplot(x='Tenure', y='Total Spend', hue='Cluster', data=combained_df, palette='viridis', s=100, ax=ax)
    ax.set_title('Customer Segments Based on Tenure and Total Spend')
    st.pyplot(fig)

elif options == "Subscription Type & Contract Length (Bar Plot)":
    fig, ax = plt.subplots()
    sns.countplot(x='Subscription Type', hue='Contract Length', data=combained_df, palette='Set2', ax=ax)
    ax.set_title('Subscription Type & Contract Length')
    st.pyplot(fig)

elif options == "Total Spend by Gender & Churn (Box Plot)":
    combained_df['Churn_Label'] = combained_df['Churn'].map({0: 'Not Churned', 1: 'Churned'})
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.boxplot(x='Gender', y='Total Spend', hue='Churn_Label', data=combained_df, ax=ax)
    ax.set_title('Distribution of Total Spend by Gender and Churn Status')
    ax.set_xlabel('Gender')
    ax.set_ylabel('Total Spend')
    ax.legend(title='Churn Status', loc='upper right')
    st.pyplot(fig)

elif options == "Contract Length by Gender & Churn (Bar Plot)":
    contract_length_counts = combained_df.groupby(['Gender', 'Churn'])['Contract Length'].value_counts().unstack(fill_value=0)
    fig, ax = plt.subplots(figsize=(12, 6))
    contract_length_counts.plot(kind='bar', stacked=True, ax=ax)
    ax.set_title('Contract Length Distribution by Gender and Churn Status')
    ax.set_xlabel('Gender')
    ax.set_ylabel('Count')
    ax.legend(title='Contract Length', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.text(1.05, 0.5, 'Churn Status: 0 = Not Churned 1 = Churned',
             transform=plt.gca().transAxes, fontsize=10, verticalalignment='center')
    st.pyplot(fig)
    
elif options == "Payment Delay by Churn Status (Box Plot)":
    payment_delay_by_churn = combained_df.groupby('Churn')['Payment Delay'].mean()
    st.write(payment_delay_by_churn)  # Display the mean payment delay
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(x='Churn', y='Payment Delay', data=combained_df, ax=ax)
    ax.set_title('Distribution of Payment Delay by Churn Status')
    ax.set_xlabel('Churn')
    ax.set_ylabel('Payment Delay (Days)')
    ax.set_xticklabels(['Not Churned', 'Churned'])
    st.pyplot(fig)


elif options == "Subscription Type Pie Chart":
    subscription_type_counts = combained_df['Subscription Type'].value_counts()
    fig, ax = plt.subplots()
    ax.pie(subscription_type_counts, labels=subscription_type_counts.index, autopct='%1.1f%%')
    ax.set_title('Subscription Type Distribution')
    st.pyplot(fig)

elif options == "Churn Category Pie Chart":
    churn_category_counts = combained_df['Churn'].value_counts()
    fig, ax = plt.subplots()
    ax.pie(churn_category_counts, labels=churn_category_counts.index, autopct='%1.1f%%')
    ax.set_title('Churn Category Distribution')
    st.pyplot(fig)

elif options == "Churn Distribution (Pie Chart)":
    filtered = combained_df.copy()
    filtered['churn_category'] = ['Churn' if x == 1 else 'Not Churned' for x in filtered['Churn']]
    dict_of_val_counts = dict(filtered['churn_category'].value_counts())
    data = list(dict_of_val_counts.values())
    keys = list(dict_of_val_counts.keys())
    palette_color = sns.color_palette('bright')
    plt.pie(data, labels=keys, colors=palette_color, autopct='%.0f%%')
    plt.title("Distribution of Customer's Churn Status:")
    plt.axis('equal')  # Ensures the pie chart is circular
    st.pyplot(plt)  # This line will render the plot in Streamlit

elif options == "Tenure vs Churn Rate (Line Chart)":
    fig, ax = plt.subplots()
    sns.lineplot(x='Tenure', y='Churn', data=combained_df, ax=ax)
    ax.set_title('Tenure vs Churn Rate')
    st.pyplot(fig)

elif options == "Age vs Churn (Line Chart)":
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.lineplot(data=combained_df, x='Age', y='Churn', hue='Gender', ci=None, ax=ax)
    ax.set_title('Age vs Churn for Different Genders (Line Chart)')
    ax.set_xlabel('Age')
    ax.set_ylabel('Average Churn Rate')
    st.pyplot(fig)
    
elif options == "Support Calls by Subscription Type and Churn Status":
    # Create a pivot table for Subscription Type, Churn status, and the average number of Support Calls
    heatmap_data = combained_df.pivot_table(index='Subscription Type', columns='Churn', values='Support Calls', aggfunc='mean')
    plt.figure(figsize=(10, 6))
    sns.heatmap(heatmap_data, annot=True, fmt=".1f", cmap='coolwarm')
    plt.title('Support Calls Across Subscription Types and Churn Status')
    plt.xlabel('Churn Status')
    plt.ylabel('Subscription Type')
    plt.tight_layout()
    st.pyplot(plt)

elif options == "Average Support Calls by Churn Status":
    plt.figure(figsize=(10, 6))
    sns.barplot(data=combained_df, x='Churn', y='Support Calls', palette='viridis')
    plt.title('Average Number of Support Calls by Churn Status')
    plt.xlabel('Churn (0 = Not Churned, 1 = Churned)')
    plt.ylabel('Average Number of Support Calls')
    plt.tight_layout()

    st.pyplot(plt)

elif options == "Total Spend vs. Contract Length (Scatter Plot)":
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(data=combained_df, x='Contract Length', y='Total Spend', hue='Churn', palette='viridis', ax=ax)
    ax.set_title('Relationship Between Total Spend and Contract Length')
    ax.set_xlabel('Contract Length (months)')
    ax.set_ylabel('Total Spend ($)')
    st.pyplot(fig)

elif options == "Churn Over Tenure (Line Chart)":
    fig, ax = plt.subplots()
    sns.lineplot(x='Tenure', y='Churn', data=combained_df, ax=ax)
    ax.set_title('Churn Over Tenure')
    st.pyplot(fig)

elif options == "Average Last Interaction by Churn Status":
    # Calculating the average of the 'Last Interaction' by 'Churn' status
    avg_last_interaction = combained_df.groupby('Churn')['Last Interaction'].mean()
    avg_last_interaction.plot(kind='bar')
    plt.title('Average Last Interaction Time by Churn Status')
    plt.xlabel('Churn Status')
    plt.ylabel('Average Last Interaction Time')
    plt.xticks(ticks=[0, 1], labels=['Non-Churned', 'Churned'], rotation=0)
    plt.grid(axis='y')
    plt.tight_layout()
    st.pyplot(plt)

elif options == "Correlation Heatmap (Support Calls, Churn, Payment Delay)":
    fig, ax = plt.subplots()
    sns.heatmap(combained_df[['Support Calls', 'Churn', 'Payment Delay']].corr(), annot=True, cmap='coolwarm', ax=ax)
    ax.set_title('Correlation Heatmap')
    st.pyplot(fig)

elif options == "Payment Delay Range (Customer Count)":
    bins = [0, 5, 10, 15, 20, 25, 30]
    labels = ['0-5', '5-10', '10-15', '15-20', '20-25', '25-30']
    combained_df['Payment Delay Range'] = pd.cut(combained_df['Payment Delay'], bins=bins, labels=labels, right=False)
    sns.countplot(x='Payment Delay Range', data=combained_df.reset_index(), palette='viridis')
    plt.title('Customer Count by Payment Delay Range')
    plt.xlabel('Delayed Times Range')
    plt.ylabel('Count of Customers')
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(plt)
    combained_df.drop('Payment Delay Range', axis=1, inplace=True)

# Button to show dataset description
if st.sidebar.button('Show Dataset Description'):
    st.subheader('Dataset Description')
    st.write(combained_df.describe())

# Option to show the dataset
if st.sidebar.checkbox('Show Dataset',value=True):
    st.subheader('Dataset')
    st.write(combained_df)

from sklearn.model_selection import train_test_split
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.metrics import classification_report, confusion_matrix

# Load dataset
file_path = 'combained_data.csv'
combained_df = pd.read_csv(file_path)
combained_df = combained_df.dropna()

# Preprocessing for prediction
subscription_type_mapping = {'Basic': 0, 'Standard': 1, 'Premium': 2}
contract_length_mapping = {'Annually': 12, 'Quarterly': 3, 'Monthly': 1}
gender_mapping = {'Male': 0, 'Female': 1}

# Features and target
X = combained_df[['Usage Frequency', 'Support Calls', 'Payment Delay', 
                  'Subscription Type', 'Contract Length', 'Total Spend', 
                  'Last Interaction', 'Gender', 'Age', 'Tenure']]

# Encode categorical features for model training
X['Subscription Type'] = X['Subscription Type'].map(subscription_type_mapping)
X['Contract Length'] = X['Contract Length'].map(contract_length_mapping)
X['Gender'] = X['Gender'].map(gender_mapping)

y = combained_df['Churn']

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the Gradient Boosting Classifier model
model = HistGradientBoostingClassifier()

# Fit the model
model.fit(X_train, y_train)

# Sidebar - Prediction input fields
st.sidebar.title("Customer Churn Prediction")

st.sidebar.subheader("Input Customer Data:")

# Add the new input fields
gender = st.sidebar.selectbox("Gender", ['Male', 'Female'])
age = st.sidebar.number_input('Age', min_value=18, max_value=100, value=30)
tenure = st.sidebar.number_input('Tenure (months)', min_value=0, max_value=120, value=12)

# Existing input fields
usage_frequency = st.sidebar.number_input('Usage Frequency', min_value=0, max_value=100, value=10)
support_calls = st.sidebar.number_input('Support Calls', min_value=0, max_value=100, value=5)
payment_delay = st.sidebar.number_input('Payment Delay (days)', min_value=0, max_value=365, value=0)

# Dropdown for Subscription Type
subscription_type = st.sidebar.selectbox("Subscription Type", ['Basic', 'Standard', 'Premium'])

# Dropdown for Contract Length
contract_length = st.sidebar.selectbox("Contract Length", ['Annually', 'Quarterly', 'Monthly'])

total_spend = st.sidebar.number_input('Total Spend ($)', min_value=0.0, value=1000.0)
last_interaction = st.sidebar.number_input('Last Interaction (days ago)', min_value=0, max_value=365, value=30)

# When the "Predict" button is clicked
if st.sidebar.button('Predict Churn'):
    # Map the user input for Subscription Type, Contract Length, and Gender
    subscription_type_encoded = subscription_type_mapping[subscription_type]
    contract_length_encoded = contract_length_mapping[contract_length]
    gender_encoded = gender_mapping[gender]

    # Collect input data into an array
    input_data = np.array([[usage_frequency, support_calls, payment_delay, 
                            subscription_type_encoded, contract_length_encoded, 
                            total_spend, last_interaction, gender_encoded, age, tenure]])

    # Make prediction
    prediction = model.predict(input_data)
    
    # Display prediction result
    if prediction[0] == 1:
        st.sidebar.success('The customer is likely to *churn*.')
    else:
        st.sidebar.success('The customer is likely to *stay*.')
