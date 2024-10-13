import collections as clt

def average_rating(user_output: dict):
    total = 0.0
    for user in user_output:
        total += user['rating']
    return total / len(user_output)

def action_breakdown(user_output: dict):
    actions = [user['action'] for user in user_output]
    counts = clt.Counter(actions)
    return {
        'purchase': counts['purchase'],
        'like': counts['like'],
        'view': counts['view'],
        'total': len(user_output)
    }