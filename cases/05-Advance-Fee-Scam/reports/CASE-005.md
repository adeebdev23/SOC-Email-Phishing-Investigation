
# CASE-001: Microsoft Account Phishing Investigation

## Case Information
- Type: Email Phishing / Brand Impersonation
- Email Date: 8 September 2023
- Investigation Date: 24 October 2026
- Analyst: Adeeb Awez Ahmed
- Tools: VS Code, VirusTotal, AbuseIPDB
- Source: Public phishing research sample

## 1. Email Header Analysis
- From: no-reply@access-accsecurity.com
- Reply-To: sotrecognizd@gmail.com
- Return-Path: bounce@thcultarfdes.co.uk
- Sending IP: 89.144.44.2
- SPF: None
- DKIM: None
- DMARC: Permanent error

## 2. Email Content Analysis
The email impersonated the Microsoft account team
and claimed unusual account sign-in activity.

The "Report The User" button used a mailto link
addressed to an unrelated Gmail account.

A hidden 1x1 image referenced an external tracking
URL hosted on thebandalisty[.]com.

## 3. VirusTotal Findings

Sending IP: 89.144.44.2
- Detection: 0/92
- ASN: AS201132
- Network: MSCode
- Country: Poland

Sender Domain: access-accsecurity[.]com
- No malicious vendor detections

Tracking Domain: thebandalisty[.]com
- Detection: 9/92 malicious/phishing
- Additional suspicious classification: ESET

## 4. AbuseIPDB Findings
IP: 89.144.44.2
- Abuse Confidence Score: 0%
- Reports: 1
- ISP: MSCode.pl
- Reported activity: Port Scan / DDoS Attack

## 5. Analysis
The email impersonated Microsoft while using an
unrelated sender domain and Gmail reply destination.

The sending IP and sender domain reputation results
were inconclusive.

The hidden tracking domain had multiple malicious
and phishing classifications at investigation time.

## 6. Verdict
Likely phishing - Microsoft account impersonation.

Confidence: Moderate to High

No evidence was established of successful account
compromise or credential theft.

## 7. Recommended SOC Response
- Escalate the suspected phishing message.
- Recommend quarantine following verification.
- Search for related sender addresses and messages.
- Review whether recipients replied or loaded
  remote content.
- Consider blocking confirmed malicious indicators
  after assessing operational impact.

These are recommended actions, not production
actions performed during this investigation.
