import re

def validate_addr_spec(addr):
    if '@' not in addr:
        return 'ng'

    email = addr.rsplit("@", 1)
    local, domain = email[0], email[1]

    # domain part
    if not check_dot_atom(domain):
        return 'ng'

    # local part
    if local.find('"') == -1:
        if not check_dot_atom(local):
            return 'ng'
    elif not check_quoted_string(local):
        return 'ng'

    return 'ok'

def check_dot_atom(text):
    if text.strip('.') is not text:
        return False

    if len(text) == 0:
        return False
    
    if text.find('..') != -1:
        return False

    ng_chars = re.escape(r"!#$%&'*+-/=?^_`{|}~.")
    pattern = "[^0-9a-zA-Z%s]" % ng_chars

    if re.compile(pattern).search(text):
        return False

    return True

def check_quoted_string(text):
    if not text.startswith('"'):
        return False

    if not text.endswith('"'):
        return False

    if len(text) < 2:
        return False

    text = text.strip('"')

    ng_chars = re.escape(r"!#$%&'*+-/=?^_`{|}~(),.:;<>@[]\"\\")
    pattern = "[^0-9a-zA-Z%s]" % ng_chars

    if re.compile(pattern).search(text):
        return False
    
    return True

if __name__ == '__main__':
    validate_addr_spec('abc@example.com')
