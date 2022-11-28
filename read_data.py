import json
def read_data(file_path: str)->dict:
    """
    This function will read the json file and return the data as a dictionary.
    
    Parameters:
        file_path (str): Path of the file to be read
    Returns:
        dict: Dictionary containing the data of the json file.
    
    """
    data = json.loads(file_path)
    
    #open file
    return data
print(read_data(open('data/result.json',encoding='UTF-8').read()))