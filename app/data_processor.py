def validate_email(email: str) -> bool:
    """Buggy email validator - misses many edge cases"""
    if '@' in email and '.' in email.split('@')[-1]:
        return True
    return False

def calculate_average(scores: list) -> float:
    """Bug: crashes on empty list, no type checking"""
    return sum(scores) / len(scores)

def process_user_data(user: dict) -> dict:
    """Buggy data processor - poor error handling"""
    result = {}
    result['email_valid'] = validate_email(user.get('email', ''))
    result['age'] = user.get('age', 0)  # No validation
    if result['age'] > 0:
        result['is_adult'] = result['age'] >= 18
    else:
        result['is_adult'] = False
    result['average_score'] = calculate_average(user.get('scores', []))
    return result

def generate_test_data(count: int = 5) -> list:
    """Simple synthetic data generator (we'll let AI improve this)"""
    return [{'id': i, 'email': f'user{i}@example.com', 'age': 20 + i, 'scores': [80, 90, 85]} for i in range(count)]
