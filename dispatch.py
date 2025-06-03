import random
import time
import base64

with open("data/targets.csv") as f:
    targets = f.readlines()

template = open("templates/phishing_email.html").read()

for victim in targets:
    email = victim.strip()
    print(f"[+] Simulating phishing email to: {email}")
    time.sleep(0.2)
    fake_link = f"https://wallet-verify.{random.randint(1000,9999)}.io/connect.html"
    message = template.replace("{{wallet_url}}", fake_link)
    b64msg = base64.b64encode(message.encode()).decode()
    print(f"[debug] Encoded payload: {b64msg[:60]}...")
