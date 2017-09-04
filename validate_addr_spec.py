import re

def validate_addr_spec(addr):
     addr.rsplit("@", 1)

   return 'ok'

if __name__ == '__main__':
    validate_addr_spec('abc@example.com')
