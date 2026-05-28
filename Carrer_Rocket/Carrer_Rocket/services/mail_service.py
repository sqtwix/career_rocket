import re

def check_mail(mail : str) -> bool:
    allowed_combinations = {
        'yandex': ['ru'],
        'gmail': ['com'],
        'mail': ['ru', 'com'],
        'yahoo' : ['com']
    }

    mail_pattern = r'^[a-zA-Z0-9x]{2,34}@[a-zA.-]+\.[a-zA-Z]{2,}$'

    if not re.match(mail_pattern, mail): return False

    local_part, domain_full = mail.split('@')
    domain_parts = domain_full.split('.')

    if domain_parts[0] not in allowed_combinations: return False
    if domain_parts[1] not in allowed_combinations[domain_parts[0]]: return False
    return True
