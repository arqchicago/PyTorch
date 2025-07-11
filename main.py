from data_loader import load_data


if __name__ == "__main__":

    #---------------------------------------------------------------------------------------------------------------------------
    # load data from the CSV data file
    file_path = 'data//heart2.csv'
    data_load_response = load_data(file_path)

    if data_load_response["body"]["data"] is not None:
        data_df = data_load_response["body"]["data"].copy()

        rows, cols = data_df.shape
        print(f"Data loaded successfully:  rows={rows}, cols={cols}")

    else:
        print("Data loader failed.")