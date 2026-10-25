
from email import policy
from email.parser import BytesParser
from pathlib import Path
import base64
import re

email_file = Path("sample-18.eml")
message = BytesParser(policy=policy.default).parsebytes(
    email_file.read_bytes()
)

count = 0

for part in message.walk():
    if part.get_content_type() != "text/html":
        continue

    html = part.get_content()

    pattern = r"data:image/(png|jpeg|jpg|gif);base64,([A-Za-z0-9+/=\s]+)"

    for match in re.finditer(pattern, html, re.IGNORECASE):
        encoded = re.sub(r"\s+", "", match.group(2))

        try:
            image_data = base64.b64decode(encoded, validate=True)
        except Exception:
            continue

        count += 1
        extension = match.group(1).lower()
        filename = f"embedded-image-{count}.{extension}"

        Path(filename).write_bytes(image_data)
        print(f"Extracted: {filename}")

print(f"Total images extracted: {count}")
