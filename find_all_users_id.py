from read_data import read_data

def find_all_users_id(data: dict)->list:
    """ 
    This function will find all the users in the json file and return the list of users id
    
    Parameters:
        data (dict): Dictionary containing the data of the json file
    Returns:
        list: List containing all the users id
    """
    messages=data['messages']
    user_id=[]
    for msg in messages:
        id=msg.get('from_id', False)
        if id not in user_id and id:
            user_id.append(id)

        id=msg.get('actor_id', False)
        if id not in user_id and id:
            user_id.append(id)
    user_id.remove("channel1640165484")
    user_id.remove("channel1474589327")
    return user_id
data=read_data('data/result.json')
print(find_all_users_id(data))