import re

def validate_addr_spec(addr):
    if '@' not in addr:
        return 'ng'

    email = addr.rsplit("@", 1)
    local, domain = email[0], email[1]

    # domain part
    if domain.strip('.') is not domain:
        return 'ng'

    if len(domain) == 0:
        return 'ng'
    
    if domain.find('..') != -1:
        return 'ng'

    ng_chars = re.escape(r"!#$%&'*+-/=?^_`{|}~.")
    pattern = "[^0-9a-zA-Z%s]" % ng_chars

    if re.compile(pattern).search(domain):
        return 'ng'

    return 'ok'

if __name__ == '__main__':
    validate_addr_spec('abc@example.com')
