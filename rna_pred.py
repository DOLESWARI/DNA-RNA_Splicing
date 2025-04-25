import streamlit as st
import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder

def run():
    # Load the pre-trained model (static)
    model_file_path = "multi_output_model.pkl"
    with open(model_file_path, 'rb') as file:
        loaded_model = pickle.load(file)

    # Initialize encoders
    label_encoders = {}

    # Streamlit App
    st.title("Multi-Output Predictor")
    st.write("Upload the dataset CSV file and provide input to predict **Condition**, **RNA Sequence**, and **Varied RNA Sequence**.")

    # Step 1: Upload CSV File
    uploaded_csv = st.file_uploader("Upload Dataset CSV File", type=["csv"])
    data = None
    if uploaded_csv:
        data = pd.read_csv(uploaded_csv)
        st.success("CSV File Uploaded Successfully!")
        st.write("Dataset Preview:")
        st.dataframe(data.head())

        # Extract unique options for dropdowns from the CSV
        input_features = [
            'Stage', 'Age', 'Male_or_Female', 'Hair_Color', 'Skin_Tone',
            'Height', 'Color_Blindness', 'Weight', 'Eye_Colour', 'Eye_Sight',
            'Vericose_Vein', 'Blood Pressure', 'Thyroid', 'Blood_Group',
            'Allergy', 'Migrane', 'Nerve_Problem'
        ]

        output_features = ['Sample _ID','Condition', 'RNA_Sequence', 'Varied_RNA_Sequence']

        dropdown_options = {feature: data[feature].dropna().unique().tolist()
                            for feature in input_features if data[feature].dtype == 'object'}

        # Step 2: Collect User Input
        st.subheader("Provide Input Data (Leave Blank to Predict Entire Dataset)")
        user_input = {}
        for feature in input_features:
            if feature in dropdown_options:
                user_input[feature] = st.selectbox(f"Select {feature}:", options=[""] + dropdown_options[feature])
            elif feature in ['Age', 'Height', 'Weight']:
                user_input[feature] = st.number_input(f"Enter {feature} (Leave Blank for Dataset Prediction):", min_value=0, value=0, step=1)
            else:
                user_input[feature] = st.text_input(f"Enter {feature} (Leave Blank for Dataset Prediction):")

        # Remove empty inputs to distinguish between known and unknown prediction
        is_known_data = all(value == "" for value in user_input.values() if isinstance(value, str)) and all(value == 0 for value in user_input.values() if isinstance(value, (int, float)))

        # Step 3: Predict Button
        if st.button("Predict"):
            if is_known_data and data is not None:  # Known Data Prediction
                st.subheader("Predicting for Entire Dataset")
                encoded_data = data[input_features].copy()

                # Encode categorical features in the dataset
                for col in encoded_data.select_dtypes(include=['object']).columns:
                    if col not in label_encoders:
                        le = LabelEncoder()
                        label_encoders[col] = le.fit(data[col].astype(str))
                    encoded_data[col] = label_encoders[col].transform(encoded_data[col].astype(str))

                # Predict for entire dataset
                try:
                    known_predictions = loaded_model.predict(encoded_data)
                    known_predictions_df = pd.DataFrame(
                        known_predictions[:, :len(output_features)], columns=output_features
                    )
                    st.write(known_predictions_df)
                except Exception as e:
                    st.error(f"Error in dataset prediction: {e}")

            elif not is_known_data:  # User Input Prediction
                st.subheader("Predicting for Provided Input")
                user_input_df = pd.DataFrame([user_input])

                # Encode categorical features in user input
                for col in user_input_df.select_dtypes(include=['object']).columns:
                    if col in label_encoders:
                        user_input_df[col] = label_encoders[col].transform(user_input_df[col].astype(str))
                    else:
                        le = LabelEncoder()
                        label_encoders[col] = le.fit(data[col].astype(str))
                        user_input_df[col] = le.transform(user_input_df[col].astype(str))

                # Predict for user input
                try:
                    predicted_output = loaded_model.predict(user_input_df)
                    predicted_df = pd.DataFrame(
                        predicted_output[:, :len(output_features)], columns=output_features
                    )
                    st.write(predicted_df)
                except Exception as e:
                    st.error(f"Error in prediction: {e}")
            else:
                st.warning("Please upload a CSV file or provide input data for prediction.")

# Ensure compatibility with main script
if __name__ == "__main__":
    run()
