from read_data import read_data


def find_all_users_id(data: dict) -> list:
    """ 
    This function will find all the users in the json file and return the list of users id

    Parameters:
        data (dict): Dictionary containing the data of the json file
    Returns:
        list: List containing all the users id
    """
    users_id = []
    messages = data['messages']
    for i in messages:
        if i['type'] == 'service':
            if users_id.count(i['actor_id']) == 0:
                users_id.append(i['actor_id'])
        elif i['type'] == 'message':
            if users_id.count(i['from_id']) == 0:
                users_id.append(i['from_id'])
    return users_id


data = read_data('data/result.json')
print(find_all_users_id(data))
