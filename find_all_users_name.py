from read_data import read_data

def find_all_users_name(data: dict)->list:
    """
    This function will find all the users in the json file and return the list of users name.
 
    Parameters:
        data (dict): Dictionary containing the data of the json file.
    Returns:
        list: List containing all the users name.
    """
    user_name=[]
    for n in range(len(data['messages'])):
        user_name.append(data['messages'][n]["actor"])
    return user_name
