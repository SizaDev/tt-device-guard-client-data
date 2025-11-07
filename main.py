#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import base64
import json

def encode_payload(payload: dict) -> str:
    # Convert dict to JSON string and encode to Base64
    json_str = json.dumps(payload, ensure_ascii=False)
    return base64.b64encode(json_str.encode("utf-8")).decode("ascii")

def decode_payload(b64_str: str) -> dict:
    # Decode Base64 string back to JSON dict
    raw = base64.b64decode(b64_str, validate=True).decode("utf-8")
    return json.loads(raw)

def main():
    # Original JSON payload
    payload = {
        "device_token": "1|{\"aid\":1233,\"av\":\"42.4.4\",\"did\":\"7569671398152095249\",\"iid\":\"7569672269414090497\",\"fit\":\"1762451702\",\"s\":0.8,\"idc\":\"my\",\"ts\":\"1762506132\"}",
        "timestamp": 1762506266,
        "req_content": "device_token,path,timestamp",
        "dtoken_sign": "ts.1.MEYCIQCKyC9uDtN176zaYC1EwfpqEG1m+FNYldFHqDKI86DC+dwIhALZCINK78LekPMWKuBQJCWbTrfcKavM+KLB5oariSHl",
        "dreq_sign": "MEYCIQF0KxsdvL52NRZjFoardj5EsFI7A/H9DeXSCho30gIhAJT6kqHe38xJbu39RhaXJR0+KZM18hD9g6S6EQvQCNAx"
    }

    # Print original JSON
    print("== Original JSON ==")
    print(json.dumps(payload, ensure_ascii=False, indent=2))

    # Encode to Base64
    encoded = encode_payload(payload)
    print("\n== Encoded Base64 ==")
    print(encoded)

    # Decode back to JSON
    decoded = decode_payload(encoded)
    print("\n== Decoded JSON ==")
    print(json.dumps(decoded, ensure_ascii=False, indent=2))

    # Modify a field and re-encode
    decoded["timestamp"] = 9999999999  # Example modification
    new_encoded = encode_payload(decoded)
    print("\n== Modified Base64 ==")
    print(new_encoded)

if __name__ == "__main__":
    main()
