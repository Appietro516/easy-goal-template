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
