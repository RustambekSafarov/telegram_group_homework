from read_data import read_data
from find_all_users_id import find_all_users_id


def find_user_message_count(data: dict, users_id: list) -> dict:
    """
    This function will find the user's message count.

    Parameters:
        data (dict): Dictionary containing the data of the json file
        user_id (list): User id of the user
    Returns:
        dict: Number of messages of the users
    """
    message_count = {}
    messages = data['messages']
    for i in users_id:
        message_count[i] = 0
        for msg in messages:
            if msg['type'] == 'message' and msg['from_id'] == i:
                message_count[i] += 1
            if msg['type'] == 'service' and msg['actor_id'] == i:
                message_count[i] += 1
    return message_count


data = read_data('data/result.json')
data1 = find_all_users_id(data)
print(find_user_message_count(data, data1))
