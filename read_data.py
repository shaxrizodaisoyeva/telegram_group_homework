import json
def read_data(file_path: str)->dict:
    """
    This function will read the json file and return the data as a dictionary.
    
    Parameters:
        file_path (str): Path of the file to be read
    Returns:
        dict: Dictionary containing the data of the json file.
    
    """
    #open file
    encoding="UTF8"
    f=open(file_path).read()
    read_data=json.loads(f)
    return read_data
file_path='data/result.json'
print(read_data(file_path))