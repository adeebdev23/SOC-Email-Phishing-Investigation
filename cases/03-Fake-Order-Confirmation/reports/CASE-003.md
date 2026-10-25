# CASE-003: Fake Order Confirmation Email Investigation

## 1. Case Information

| Field | Details |
|---|---|
| Case ID | CASE-003 |
| Investigation Type | Suspicious Email / Brand Impersonation |
| Email Subject | ORDER CONFIRMATION - DEWALT POWER STATION |
| Email Date | 9 September 2022 |
| Investigation Date | 25 October 2026 |
| Analyst | Adeeb Awez Ahmed |
| Tools | VS Code, VirusTotal, AbuseIPDB |
| Sample Source | Public Phishing Pot Research Repository |
| Verdict | Suspicious / Deceptive Spam |
| Confidence | High for deceptive content; low for confirmed phishing |

## 2. Investigation Objective

Investigate a suspicious email claiming to be an order confirmation from Lowe's Department for a DeWalt power station.

The investigation focused on identifying sender impersonation, analysing email headers, examining authentication results, extracting suspicious links, conducting threat intelligence checks, and determining whether sufficient evidence existed to classify the message as phishing.

## 3. Email Header Analysis

### Identified Headers

- **From:** Lowe's Department, `noreply@line.me`
- **To:** phishing@pot.org
- **Subject:** ORDER CONFIRMATION - DEWALT POWER STATION
- **Date:** 9 September 2022
- **External Sending IP:** 93.188.155.251
- **Reported Sending Hostname:** palmnbtred.co.uk

### Email Authentication

| Authentication | Result |
|---|---|
| SPF | None |
| DKIM | None |
| DMARC | Fail |
| Header From Domain | line.me |

### Analysis

The email claimed to represent Lowe's Department but displayed an unrelated sender domain.

The subject contained unusual stylised Unicode characters.

SPF returned `none`, indicating no positive SPF authorisation result. DKIM returned `none`, indicating that no signature was available for verification. DMARC failed.

These findings raised concerns about the sender's authenticity but did not independently prove malicious intent.

### Email Routing

The `Received` headers showed that Microsoft's email infrastructure accepted the message from:

**93.188.155.251**

Additional `Received` entries described its movement through Microsoft's mail servers.

The external IP was investigated separately from the internal delivery infrastructure.

## 4. Email Content Analysis

The subject suggested that the recipient had placed an order for a DeWalt power station.

However, examination of the HTML email body revealed:

- No meaningful order confirmation details.
- No clear purchase amount or order reference.
- Images referencing Houston sports content.
- Two shortened `t.co` links.
- External image and tracking-related resources.

### Suspicious Characteristics

1. **Brand Impersonation:** The email claimed to represent Lowe's Department.
2. **Sender Mismatch:** The sender address used `line.me`, which was unrelated to the claimed retailer.
3. **Misleading Subject:** The order-confirmation subject did not match the actual email content.
4. **Unusual Typography:** The subject and sender name used stylised Unicode characters.
5. **Shortened URLs:** The message contained links that obscured their destinations.

**Assessment:** The combination of inconsistent sender information, misleading subject matter and unrelated content strongly suggested a deceptive or spam message.

## 5. Sending IP Investigation

### IP Address: 93.188.155.251

**AbuseIPDB Findings**

| Field | Result |
|---|---|
| Abuse Confidence Score | 0% |
| Abuse Reports | Not found in database |
| ISP | Virterion LLC |
| ASN | AS59729 |
| Usage Type | Data Centre / Web Hosting / Transit |
| Country | Bulgaria |
| City | Sofia |

### Analysis

The IP was associated with hosting infrastructure in Bulgaria.

AbuseIPDB did not provide evidence of reported abusive activity.

However, the absence of abuse reports did not establish that the email was legitimate.

The IP's geographical location and hosting classification were not treated as proof of malicious activity.

## 6. URL Investigation

Two shortened URLs were extracted from the email body.

### URL 1: hxxps://t[.]co/RKXqUZPn2f

**VirusTotal Findings**

- Detection Ratio: 0/92
- HTTP Status: 200
- Response Type: HTML
- First Submission: 9 September 2022
- Last Analysis: 18 June 2026
- Serving IP: 172.66.0.227

**HTML Analysis**

The report contained information associated with a domain-sale page for KalmTrees.com through HugeDomains.

The VirusTotal final URL field still displayed the original `t.co` link.

**Assessment:** No malicious vendor detections were reported. The observed domain-sale content did not confirm the URL's original destination in September 2022.

### URL 2: hxxps://t[.]co/QOkUu1qP4O

**VirusTotal Findings**

- No malicious detections shown in the reviewed results
- HTTP Status: 200
- Response Type: HTML
- First Submission: 18 January 2024
- Last Analysis: 18 June 2026
- Serving IP: 162.159.140.229

**HTML Analysis**

The website title displayed in VirusTotal was:

`HugeDomains.com`

The report also identified Google Analytics and Google Tag Manager.

**Assessment:** The available results did not confirm malicious URL behaviour or the original destination at the time the email was sent.

### URL Analysis Conclusion

Neither shortened URL was confirmed malicious through the reviewed VirusTotal results.

The available analyses were conducted years after the email was sent. Consequently, the historical destinations and original purpose of these links could not be reliably established.

## 7. Additional External Resource Analysis

The email contained an image resource associated with:

`link.click2houston[.]com`

During the investigation, AbuseIPDB resolved this domain to:

**3.222.82.214**

### AbuseIPDB Findings

- Abuse Confidence Score: 0%
- Total Reports: 18
- ISP: Amazon Data Services Northern Virginia
- ASN: AS14618
- Country: United States

### Assessment

The resolved IP belonged to Amazon hosting infrastructure.

The reputation results did not establish that the image-hosting service or associated IP was malicious.

The domain's current IP association was not considered proof of historical attacker infrastructure.

## 8. Indicators and Investigation Artefacts

| Indicator | Type | Assessment |
|---|---|---|
| noreply@line.me | Sender Address | Inconsistent with claimed retailer |
| 93.188.155.251 | Sending IP | No abuse reports identified |
| palmnbtred[.]co.uk | Reported Hostname | Association requires verification |
| t[.]co/RKXqUZPn2f | Shortened URL | Historical destination unconfirmed |
| t[.]co/QOkUu1qP4O | Shortened URL | Historical destination unconfirmed |
| link.click2houston[.]com | External Resource | Image-hosting reference |
| 3.222.82.214 | Infrastructure IP | No confirmed malicious association |

**Note:** These are investigation artefacts. They should not all be treated as confirmed malicious IOCs.

## 9. Investigation Limitations

- No malicious destination was conclusively established for either shortened URL.
- The available VirusTotal analyses were performed several years after the original email.
- The sender's actual intent could not be confirmed.
- No confirmed malware attachment or credential-harvesting page was identified.
- The reputation of hosting infrastructure alone did not establish malicious behaviour.
- No recipient interaction, credential theft or system compromise was observed.

## 10. Final SOC Verdict

**Classification:** Suspicious Email - Brand Impersonation / Deceptive Spam

**Confidence:** High that the message was deceptive; low that it constituted confirmed credential-harvesting phishing.

### Conclusion

The investigated email impersonated Lowe's Department and claimed to provide a DeWalt order confirmation.

However, the sender domain was unrelated to the claimed organisation, the message failed DMARC authentication, and the email body contained unrelated sports-themed content rather than meaningful purchase details.

The message also contained two shortened URLs whose original destinations could not be established from the available evidence.

Threat intelligence checks did not confirm malicious infrastructure or credential-harvesting activity.

Based on these findings, the email was classified as suspicious and deceptive, with insufficient evidence to confirm credential phishing or malware delivery.

## 11. Recommended SOC Actions

1. Flag the message for further security review.
2. Recommend quarantine or spam classification according to organisational policy.
3. Search for similar messages using the subject, sender details and shortened URLs.
4. Investigate whether other recipients received or interacted with the same message.
5. Advise recipients not to use links in unexpected order-confirmation emails.
6. Document the findings and limitations in the incident ticket.
7. Escalate if additional evidence of malicious redirects, credential theft or compromise is identified.

**Note:** These are recommended actions. No production security response actions were performed.

## 12. Key Learning Outcomes

- Analysed multiple `Received` headers to identify the external sending IP.
- Interpreted SPF, DKIM and DMARC authentication results.
- Identified misleading subjects and inconsistent email content.
- Examined HTML email structure and shortened URLs.
- Investigated sender infrastructure using AbuseIPDB.
- Reviewed URL reputation and historical analysis using VirusTotal.
- Distinguished suspicious indicators from confirmed malicious activity.
- Reached a supported SOC conclusion without overstating the available evidence.

## 13. References

- [Original Email Sample](https://github.com/rf-peixoto/phishing_pot/blob/main/email/sample-24.eml)
- [VirusTotal](https://www.virustotal.com/)
- [AbuseIPDB](https://www.abuseipdb.com/)

---

**Investigation Status:** Closed - Suspicious / Deceptive Spam

**Disclaimer:** This investigation was conducted for educational purposes using a publicly available email sample. Threat intelligence results reflect the analysis dates and do not necessarily represent the infrastructure or URL behaviour when the email was originally sent.