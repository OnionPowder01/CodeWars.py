#Write a simple regex to validate a username. Allowed characters are:
#lowercase letters,
#numbers,
#underscore
#Length should be between 4 and 16 characters (both included

def validate_usr(username):
    if len(username) < 4 or len(username) > 16:
        return False 
    allowed = 'abcdefghijklmnopqrstuvwxyz0123456789_'
    for i in username:
        if i not in allowed:
            return False
    return True 
