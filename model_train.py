import pandas as pd
from data_loader import format_response
from sklearn.preprocessing import StandardScaler, OneHotEncoder

def pre_process_data(data_df):

    print("ECG> Preprocessing Data...")

    try:
        # Check if the DataFrame is empty
        if data_df.empty:
            raise ValueError("The input DataFrame is empty.")
        
        # Identify numeric and categorical columns
        numeric_cols = ['age', 'trestbps', 'chol', 'thalach']
        categorical_cols = ['sex']

        X = data_df[numeric_cols+categorical_cols].copy()

        # Standardize numeric features
        scaler = StandardScaler()
        X[numeric_cols] = scaler.fit_transform(X[numeric_cols])

        # One-hot encode categorical features
        oh_encoder = OneHotEncoder(sparse_output=False, drop='first')
        encoded_categorical = oh_encoder.fit_transform(X[categorical_cols])
        encoded_categorical_df = pd.DataFrame(encoded_categorical, columns=oh_encoder.get_feature_names_out(categorical_cols))
        X = pd.concat([X[numeric_cols], encoded_categorical_df], axis=1)

        # Ensure the DataFrame has the expected shape
        if X.shape[1] != len(numeric_cols) + len(oh_encoder.get_feature_names_out(categorical_cols)):
            raise ValueError("The processed DataFrame does not have the expected number of columns.")
        
        return format_response(200, f"ECG> Data preprocessing completed successfully!", X)
    
    except KeyError as e:
        return format_response(422, f"ECG> Missing columns in the input data: {e}")
    
def train_model():
    ## Todo
    pass
    


if __name__ == "__main__":
    print("Train model using train_model function.")