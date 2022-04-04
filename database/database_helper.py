def goal_helper(goal) -> dict:
    return {
        "id": str(goal['_id']),
        "name": goal['name'],
        "description": goal['description'],
        "deadline": goal['deadline'],
        "category": goal['category']
    }

def admin_helper(admin) -> dict:
    return {
        "id": str(admin['_id']),
        "fullname": admin['fullname'],
        "email": admin['email'],
    }

def progress_helper(progress) -> dict:
    return {
        "id": str(progress['_id']),
        "name": progress['name'],
        "value": progress['value'],
        "entry": progress['deadline'],
        "goal_name": progress['goal_name']
    }