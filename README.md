# TikTok `tt-device-guard-client-data` Encoder/Decoder

This repository contains a Python script that demonstrates how to **encode** and **decode** the TikTok header `tt-device-guard-client-data`.

TikTok uses this header to transmit **device fingerprint information** and **signed payloads** during API requests.  
The payload is typically a JSON object containing identifiers such as `aid`, `av`, `did`, `iid`, `ts`, and cryptographic signatures.  
To make it safe for transport over HTTP, the JSON is encoded into **Base64** and placed in the `tt-device-guard-client-data` header.

---

## Features

- Encode JSON payloads into Base64 strings suitable for `tt-device-guard-client-data`.
- Decode Base64 strings back into JSON objects for inspection or modification.
- Print the original JSON, encoded Base64, and decoded JSON.
- Allow modifications to JSON fields and re-encode them.

---

## Requirements

- Python 3.6+
- No external dependencies (uses only `base64` and `json` from the standard library).

---

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/SizaDev/tt-device-guard-client-data
   cd tt-device-guard-client-data


- Run the script:
python3 encoder.py
- The script will:
- Print the original JSON payload (representing TikTok device data).
- Encode it into Base64 and display the result (this is the value of tt-device-guard-client-data).
- Decode the Base64 back into JSON for inspection.
- Modify a field (e.g., timestamp) and re-encode it.
Example Output== Original JSON ==
{
  "device_token": "1|{\"aid\":1233,\"av\":\"42.4.4\",\"did\":\"7569671398152095249\",\"iid\":\"7569672269414090497\",\"fit\":\"1762451702\",\"s\":0.8,\"idc\":\"my\",\"ts\":\"1762506132\"}",
  "timestamp": 1762506266,
  "req_content": "device_token,path,timestamp",
  "dtoken_sign": "ts.1.MEYCIQCKyC9uDtN176zaYC1EwfpqEG1m+FNYldFHqDKI86DC+dwIhALZCINK78LekPMWKuBQJCWbTrfcKavM+KLB5oariSHl",
  "dreq_sign": "MEYCIQF0KxsdvL52NRZjFoardj5EsFI7A/H9DeXSCho30gIhAJT6kqHe38xJbu39RhaXJR0+KZM18hD9g6S6EQvQCNAx"
}

== Encoded Base64 (tt-device-guard-client-data) ==
eyJkZXZpY2VfdG9rZW4iOiIxfHtcImFpZFwiOjEyMzMsXCJhdlwiOlwiNDIuNC40XCIsXCJkaWRcIjpcIjc1Njk2NzEzOTgxNTIwOTUyNDlcIixcImlpZFwiOlwiNzU2OTY3MjI2OTQxNDA5MDQ5N1wiLFwiZml0XCI6XCIxNzYyNDUxNzAyXCIsXCJzXCI6MC44LFwiaWRjXCI6XCJteVwiLFwidHNcIjpcIjE3NjI1MDYxMzJcIn0iLCJ0aW1lc3RhbXAiOjE3NjI1MDYyNjYsInJlcV9jb250ZW50IjoiZGV2aWNlX3Rva2VuLHBhdGgsdGltZXN0YW1wIiwiZHRva2VuX3NpZ24iOiJ0cy4xLk1FWUNJUUNLeUM5dUR0TjE3NnphWUMxRXdmcUVHMW0rRk5ZbGRGSHFES0k4NkRDK2R3SWhBTFpDSU5LNzhMZWtQTVdLdUJRSkNXYlRyZmNLYXZNTCtrTEJ5MGFyaVNIbCIsImRyZXFfc2lnbiI6Ik1FWUNJUUNGMEt4c2R5Y3R2bDUyTlJaakZvYXJkajVFc0ZJN0FcL0g5RGVYU0NobzMwZ0loQUpUNmtxSGUzOHgzSmJ1MzlSaGFYSlIwK0taMThoRDlnNlM2RVF2UUNOQXgifQ==

== Decoded JSON ==
{ ... same as original ... }

== Modified Base64 ==
<new encoded string after modification>
Notes- This script is for educational and research purposes only.
- The tt-device-guard-client-data header is part of TikTok’s internal API security and device verification system.
- Modifying or replaying these values against TikTok servers may violate their Terms of Service.
LicenseThis project is licensed under the MIT License. You are free to use, modify, and distribute it.
