# TikTok `tt-device-guard-client-data` Encoder/Decoder & Signer

This repository contains a Python script that demonstrates how to **encode**, **decode**, and **sign** payloads used in TikTok’s internal header `tt-device-guard-client-data`.

TikTok uses this header to transmit **device information** and **signed payloads** during API requests.  
The script shows how to:
- Build a JSON payload with fields like `device_token`, `timestamp`, `path`.
- Encode the payload into Base64 (to be used as the header value).
- Decode Base64 back into JSON for inspection.
- Generate digital signatures (`dtoken_sign` and `dreq_sign`) using ECDSA.

---

## Features

- ✅ Encode JSON payloads into Base64 strings.  
- ✅ Decode Base64 strings back into JSON objects.  
- ✅ Generate `dtoken_sign` (signature of `device_token`).  
- ✅ Generate `dreq_sign` (signature of `device_token + path + timestamp`).  
- ✅ Print original JSON, encoded Base64, and decoded JSON.  
- ✅ Allow modifications to JSON fields and re-encode with updated signatures.  

---

## Requirements

- Python 3.7+
- Install dependency:
  ```bash
  pip install ecdsa



Usage
- Clone the repository:
git clone https://github.com/SizaDev/tt-device-guard-client-data.git
cd tt-device-guard-client-data
- Run the script:
python3 encoder.py
- The script will:
- Print the original JSON payload with generated signatures.
- Encode it into Base64 and display the result (this is the value of tt-device-guard-client-data).
- Decode the Base64 back into JSON for inspection.
- Modify a field (timestamp in the example), regenerate signatures, and re-encode.

Example Output
== Original JSON with signatures ==
{
  "device_token": "1|{\"aid\":1233,\"av\":\"42.4.4\",\"did\":\"7569671398152095249\",\"iid\":\"7569672269414090497\",\"fit\":\"1762451702\",\"s\":0.8,\"idc\":\"my\",\"ts\":\"1762506132\"}",
  "timestamp": 1762506266,
  "req_content": "device_token,path,timestamp",
  "path": "/aweme/v1/aweme/stats/",
  "dtoken_sign": "ts.1.MEYCIQ...",
  "dreq_sign": "MEYCIQ..."
}

== Encoded Base64 ==
eyJkZXZpY2VfdG9rZW4iOiIxfHtcImFpZFwiOjEyMzMsXCJhdlwiOlwiNDIuNC40XCIsXCJkaWRcIjpcIjc1Njk2NzEzOTgxNTIwOTUyNDlcIixcImlpZFwiOlwiNzU2OTY3MjI2OTQxNDA5MDQ5N1wiLFwiZml0XCI6XCIxNzYyNDUxNzAyXCIsXCJzXCI6MC44LFwiaWRjXCI6XCJteVwiLFwidHNcIjpcIjE3NjI1MDYxMzJcIn0iLCJ0aW1lc3RhbXAiOjE3NjI1MDYyNjYsInJlcV9jb250ZW50IjoiZGV2aWNlX3Rva2VuLHBhdGgsdGltZXN0YW1wIiwiZHRva2VuX3NpZ24iOiJ0cy4xLk1FWUNJUUNLeUM5dUR0TjE3NnphWUMxRXdmcUVHMW0rRk5ZbGRGSHFES0k4NkRDK2R3SWhBTFpDSU5LNzhMZWtQTVdLdUJRSkNXYlRyZmNLYXZNTCtrTEJ5MGFyaVNIbCIsImRyZXFfc2lnbiI6Ik1FWUNJUUNGMEt4c2R5Y3R2bDUyTlJaakZvYXJkajVFc0ZJN0FcL0g5RGVYU0NobzMwZ0loQUpUNmtxSGUzOHgzSmJ1MzlSaGFYSlIwK0taMThoRDlnNlM2RVF2UUNOQXgifQ==

== Decoded JSON ==
{ ... same as original ... }

== Modified Base64 ==
<new encoded string after modification>



Notes
- This script is for educational and research purposes only.
- The tt-device-guard-client-data header is part of TikTok’s internal API security and device verification system.
- Modifying or replaying these values against TikTok servers may violate their Terms of Service.

License
This project is licensed under the MIT License. You are free to use, modify, and distribute it.
