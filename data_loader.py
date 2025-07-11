import pandas as pd


def format_response(status_code, message, data=None):
    """
    Format the response for the API.
    
    Parameters:
    status_code (int): HTTP status code.
    message (str): Message to include in the response.
    data (any, optional): Additional data to include in the response.
    
    Returns:
    dict: Formatted response dictionary.
    """
    return {
        'statusCode': status_code,
        'body': {
            'message': message,
            'data': data
        }
    }

def load_data(file_path):
    """
    Load data from a CSV file and return a DataFrame.
    
    Parameters:
    file_path (str): The path to the CSV file.
    
    Returns:
    pd.DataFrame: DataFrame containing the loaded data.
    """
    try:
        data_df = pd.read_csv(file_path)
        rows, cols = data_df.shape
        return format_response(200, f"Successfully read {file_path}  rows={rows}, cols={cols}", data=data_df)

    except FileNotFoundError:
        return format_response(404, f"File not found: {file_path}")

    except UnicodeDecodeError as e:
        return format_response(422, f"Decoding error while reading the file: {e}")

    except Exception as e:
        return format_response(500, f"data loader failed: {e}")
    


if __name__ == "__main__":
    print("Load dataset using data_loader function.")