from read_data import read_data


def find_all_users_name(data: dict) -> list:
    """
    This function will find all the users in the json file and return the list of users name.

    Parameters:
        data (dict): Dictionary containing the data of the json file.
    Returns:
        list: List containing all the users name.
    """
    messages = data['messages']
    users = []
    for m in messages:
        if m['type'] == 'message':
            if users.count(m['from']) == 0:
                users.append(m['from'])
        elif m['type'] == 'service':
            if users.count(m['actor']) == 0:
                users.append(m['from'])

    return users


data = read_data('data/result.json')
print(find_all_users_name(data))
