
# CASE-002: Chase Bank Phishing Email Investigation

## 1. Case Information

| Field | Details |
|---|---|
| Case ID | CASE-002 |
| Investigation Type | Email Phishing / Banking Impersonation |
| Email Subject | Your Bank Account has been blocked due to unusual activities |
| Sample Date | 19 September 2023 |
| Investigation Date | 25 October 2026 |
| Analyst | Adeeb Awez Ahmed |
| Tools | VS Code, VirusTotal, AbuseIPDB |
| Sample Source | Public Phishing Pot research repository |
| Verdict | Likely Phishing |
| Confidence | Medium |

## 2. Investigation Objective

Analyse a suspicious email impersonating Chase Bank to identify potential phishing indicators, investigate email authentication, examine embedded URLs, perform threat intelligence checks, and determine an evidence-based SOC verdict.

## 3. Email Header Analysis

The available sample was a forwarded email.

The original suspicious message was represented within the forwarded content, while the outer email headers belonged to the forwarding and delivery chain.

### Original Message Information

- Claimed Sender: Chase Online Service
- Displayed Sender: Chase
- Address appearing in forwarded sender information: info-yagcfgyuze@boonsupply.com
- Subject: Your Bank Account has been blocked due to unusual activities
- Requested Action: Reactivate the suspended bank account

The original sender address and authentication results could not be independently verified from the forwarded content.

### Forwarded Message Authentication

- SPF: Pass
- DKIM: Pass
- DMARC: Pass
- Authenticated domain: hotmail.com
- Observed sending IPv4: 209.85.221.179
- Additional delivery infrastructure: 2a01:111:f400:7e8b::811

**Finding:** The successful authentication results relate to the forwarded message and do not establish the legitimacy of the original Chase email.

## 4. Email Content Analysis

The message claimed that unusual account activity had resulted in a temporary suspension of the recipient's bank account.

It instructed the recipient to click a "Reactivate Your Account" link to restore access.

### Suspicious Indicators

1. **Bank Impersonation:** The message claimed to represent Chase Bank.
2. **Urgency:** The message stated that the account had been suspended.
3. **Account Verification Lure:** The recipient was instructed to reactivate the account.
4. **Sender Inconsistency:** The forwarded content included an email address using the unrelated boonsupply.com domain.
5. **External Link:** The account-reactivation URL used dsgo.to rather than an identifiable Chase-owned domain.

These characteristics are consistent with social engineering techniques commonly used in banking phishing.

## 5. URL Investigation

### Suspicious URL

- Domain: dsgo[.]to
- Link Text: Reactivate Your Account
- Investigation Tool: VirusTotal

### VirusTotal Findings

- Security Vendor Detections: 0/92
- Observed Analysis Tags:
  - multiple-redirects
  - iframes
  - external-resources
  - password-input

The analysed URL returned an HTML response and VirusTotal displayed a final destination under dsgo.to.

### Analysis

The URL was unrelated to the claimed banking organisation.

Although no security vendors flagged the URL as malicious, the observed redirect and password-input characteristics warranted further investigation.

The available evidence did not confirm a malicious final destination, successful credential collection, or actual account compromise.

**Assessment:** Suspicious account-reactivation URL. Credential harvesting remains unconfirmed.

## 6. Threat Intelligence Investigation

### 6.1 Forwarding IP: 209.85.221.179

**VirusTotal**

- Detection Ratio: 0/92
- Organisation: Google LLC
- ASN: AS15169

**AbuseIPDB**

- Abuse Confidence Score: 0%
- Total Reports: 87
- Classification: Whitelisted subnet
- ISP: Google LLC

**Assessment:** Legitimate Google mail infrastructure observed in the forwarding path. Not established as attacker infrastructure.

### 6.2 Microsoft Delivery IP

IP Address: 2a01:111:f400:7e8b::811

**VirusTotal**

- Detection Ratio: 0/92
- Organisation: Microsoft Corporation
- ASN: AS8075

**AbuseIPDB**

- Abuse Confidence Score: 0%
- Reports: None displayed
- ISP: Microsoft Limited

**Assessment:** Legitimate Microsoft delivery infrastructure. Not evidence of malicious origination.

### 6.3 Sender Domain: boonsupply.com

**VirusTotal**

- No malicious vendor detections
- URLQuery classified the domain as suspicious
- Domain age at investigation: Approximately 9 years
- Registrar shown: Cloudflare, Inc.

**AbuseIPDB**

The domain resolved to 75.2.60.5 during the investigation.

- Abuse Confidence Score: 72%
- Total Reports: 213
- ISP: Amazon.com, Inc.
- ASN: AS16509

**Important Limitation**

The IP 75.2.60.5 is associated with shared Amazon infrastructure.

Its abuse reports cannot be directly attributed to boonsupply.com or to the historical phishing email.

The current domain resolution also does not establish where the domain was hosted when the 2023 email was sent.

**Assessment:** Domain involvement in the original message remains suspicious but is not independently proven malicious through the reputation results.

## 7. Indicators and Investigation Artefacts

| Indicator | Type | Assessment |
|---|---|---|
| info-yagcfgyuze@boonsupply.com | Email address | Suspicious address in forwarded content |
| boonsupply[.]com | Domain | Requires verification |
| dsgo[.]to | URL domain | Suspicious account-reactivation destination |
| 209.85.221.179 | IPv4 | Google forwarding infrastructure |
| 2a01:111:f400:7e8b::811 | IPv6 | Microsoft delivery infrastructure |
| 75.2.60.5 | IPv4 | Current shared hosting association, not verified attacker infrastructure |

Not all listed artefacts are malicious IOCs.

## 8. Investigation Limitations

- The sample was forwarded, so the original message's full headers and authentication results were unavailable.
- The original sender's infrastructure could not be conclusively identified.
- VirusTotal did not flag the reactivation URL as malicious.
- The original redirect behaviour at the time of the email could not be verified.
- The current reputation of related infrastructure does not establish its historical reputation.
- No evidence of credential submission, financial loss or account compromise was available.

## 9. Final SOC Verdict

**Classification:** Likely Phishing - Banking Impersonation

**Confidence:** Medium

### Conclusion

The email is assessed as likely phishing because it impersonated Chase Bank, used urgency-based social engineering, and instructed the recipient to reactivate an account through an unrelated domain.

The sender information displayed in the forwarded content further raised suspicion.

Threat intelligence checks were inconclusive. The analysed reactivation URL had no malicious vendor detections, and the original sender's authentication could not be independently verified.

The findings support a suspected banking phishing attempt but do not establish successful credential theft or account compromise.

## 10. Recommended SOC Actions

1. Escalate the suspicious email for security review.
2. Recommend quarantine if the message is confirmed malicious.
3. Search mail logs for similar subjects, sender addresses and embedded URLs.
4. Investigate whether any recipients clicked the reactivation link.
5. Verify suspicious account-activity claims directly through the bank's official channels.
6. Consider blocking confirmed malicious indicators after validating their ownership and possible operational impact.
7. Record the findings and investigation limitations in the incident ticket.

**Note:** These are recommended response actions. No production systems were modified during this educational investigation.

## 11. Key Learning Outcomes

- Distinguished original phishing content from forwarded email headers.
- Interpreted SPF, DKIM and DMARC results in the correct authentication context.
- Conducted IP, domain and URL reputation checks using VirusTotal and AbuseIPDB.
- Identified limitations of reputation-based threat detection.
- Avoided attributing shared or legitimate mail infrastructure to an attacker without sufficient evidence.
- Produced an evidence-based SOC verdict despite inconclusive threat intelligence results.

## 12. References

- VirusTotal: https://www.virustotal.com/
- AbuseIPDB: https://www.abuseipdb.com/
- Original Email Dataset: https://github.com/rf-peixoto/phishing_pot
- Source Sample: https://github.com/rf-peixoto/phishing_pot/blob/main/email/sample-5.eml

---

**Investigation Status:** Closed - Likely Phishing (Medium Confidence)

**Disclaimer:** This investigation was conducted for educational and portfolio purposes using a publicly available phishing sample. Findings reflect the evidence available during analysis.
