from data_loader import load_data
from model_train import pre_process_data

if __name__ == "__main__":

    #---------------------------------------------------------------------------------------------------------------------------
    # load data from the CSV data file & preprocess
    file_path = 'data//heart2.csv'
    data_load_response = load_data(file_path)

    if data_load_response["body"]["data"] is not None:
        data_df = data_load_response["body"]["data"].copy()

        rows, cols = data_df.shape
        print(f"ECG> Data loaded successfully:  rows={rows}, cols={cols}")

        preprocessed_data = pre_process_data(data_df)
        X = preprocessed_data["body"]["data"].copy()
        preprocessed_data_msg = preprocessed_data["body"]["message"]
        print(f"{preprocessed_data_msg}")

        rows, cols = X.shape
        print(f"     - rows={rows}, cols={cols}")
        print(f"     - columns are ={X.columns.tolist()}")

    else:
        print("Data loader failed.")