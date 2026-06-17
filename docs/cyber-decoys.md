# Cyber Decoys / 网络诱饵

[English](cyber-decoys.md) | [中文](cyber-decoys.zh-CN.md)

Cyber deception is the cyber-domain branch of the same idea that runs through the rest of this
project: build something — a host, a service, an account, a file, a credential, a token — whose
**only purpose is to be touched by the wrong person**, so that any interaction with it is a
high-confidence signal of an intruder. Where a physical decoy absorbs a missile, a cyber decoy
absorbs an attacker's time, attention, and tradecraft, and converts an otherwise silent breach
into an alert.

This chapter maps the cyber branch onto the shared taxonomy in [`docs/taxonomy.md`](taxonomy.md)
and is indexed in the case database ([`data/cases.csv`](../data/cases.csv), `CYBER-` keys) and the
source index ([`references/sources.md`](../references/sources.md), "Cyber Deception").

## 1. Why It Works

The economics are inverted from normal defense. A legitimate user has no reason to ever touch a
decoy asset, so the false-positive rate is near zero: any hit is meaningful. As MITRE puts it, with
traditional defense the adversary only has to be right once, but against deception the adversary
only has to be **wrong** once. Deception also flips the cost curve — it is cheap to deploy and
expensive to evade, and it can be operational in days rather than the months a detection program
takes to tune.

## 2. The Decoy Ladder (by interaction depth)

| Depth | What it is | Examples | Tradeoff |
|---|---|---|---|
| **Honeytoken** | A single piece of bait data, no host | Fake AWS key, canary file/document, decoy DB row, web/URL token, fake credential | Trivial to plant; detects *use*, not full TTPs |
| **Low-interaction honeypot** | Emulated service banners | Dionaea, OpenCanary, Honeyd, Cowrie (shell emulation) | Cheap, scalable; easier to fingerprint |
| **High-interaction honeypot** | Real or near-real OS/service | Full VMs, instrumented jails, "honeyfs" filesystems | Rich TTP capture; risk of being used as a pivot |
| **Honeynet** | A network of honeypots + monitoring | The Honeynet Project, T-Pot (20+ honeypots in one) | Realistic lateral-movement bait; heavier to run |
| **Distributed Deception Platform (DDP)** | Enterprise-wide decoys + breadcrumbs | Commercial deception tech (see §5) | Coverage and orchestration; cost |

## 3. By Decoy Object (what is faked)

- **Hosts / services** — fake servers, RDP/SSH/SMB/HTTP/FTP services, databases (MongoDB, Elasticsearch), printers, IoT/router (TR-069).
- **Identities / credentials** — honey accounts, decoy Active Directory objects, planted credentials (e.g., DCEPT), Kerberos/LSASS bait.
- **Data** — canary files/documents, fake source code, decoy records, watermarked datasets.
- **Tokens** — Canarytokens: a tripwire embedded in a file, folder, URL, DNS name, cloud API key, or QR code that calls home when used.
- **Breadcrumbs / lures** — fake artifacts (saved sessions, mapped drives, history entries) on *real* machines that point an intruder toward the decoys (e.g., Honeybits).
- **OT / ICS** — fake SCADA/PLC infrastructure (Conpot, GasPot, medpot for medical, DICOM).

## 4. Open-Source Ecosystem

A capable lab can be stood up entirely from open source:

- **T-Pot** (Deutsche Telekom Security) — an all-in-one platform bundling 20+ honeypots with an ELK dashboard.
- **Cowrie** — medium/high-interaction SSH/Telnet honeypot (successor to Kippo); records every command, includes a fake filesystem ("honeyfs").
- **Dionaea** — low-interaction, multi-protocol malware-collection honeypot (SMB, HTTP, FTP, etc.).
- **Conpot** — ICS/SCADA honeypot (Modbus, DNP3, BACnet, SNMP) with an emulated HMI.
- **Honeyd** — the classic daemon (Niels Provos) that spins up many virtual hosts with arbitrary services.
- **OpenCanary** (Thinkst) — lightweight, pip-installable multi-service honeypot daemon.
- **Canarytokens** (Thinkst) — self-hostable honeytoken generator; hosted demo at canarytokens.org.
- **Modern Honey Network (MHN)** — orchestration that wraps Snort, Cowrie/Kippo, Dionaea, Conpot for easy fleet deployment.
- **awesome-honeypots** — the community catalog of the above and many more.

## 5. Commercial Deception Technology (DDP)

Enterprise platforms add fleet management, breadcrumbs across production hosts, automated decoy
generation, and SIEM/SOAR integration. The market has consolidated through acquisitions:

- **SentinelOne Singularity Identity** (formerly **Attivo Networks**).
- **Proofpoint Shadow** (formerly **Illusive Networks**).
- **Zscaler Deception** (formerly **Smokescreen IllusionBLACK**).
- **Acalvio ShadowPlex**, **CounterCraft**, **Fortinet FortiDeceptor**, and others.

Inclusion is not endorsement; treat vendor effectiveness claims as Tier A for product existence
and far lower for validated breach-detection outcomes, exactly as with physical-decoy vendors.

## 6. Doctrine and Frameworks

- **MITRE Engage** (engage.mitre.org) — adversary-engagement framework that replaced **MITRE Shield** in March 2022; organizes denial, deception, and engagement and maps to MITRE ATT&CK. MITRE reports that adversary engagement raised intel collected per operation from a couple of IOCs to roughly 40 pieces.
- **MITRE D3FEND** (d3fend.mitre.org) — a knowledge graph of defensive techniques that includes explicit decoy techniques (decoy file, decoy network resource, decoy credential, decoy user/session).
- **The Honeynet Project** — the long-running nonprofit research community ("Know Your Enemy") that professionalized honeypot research.

## 7. Historical Anchors

- **The Cuckoo's Egg (1986-87)** — Clifford Stoll, tracing an intruder through Lawrence Berkeley Lab, fabricated a fake "SDInet" project full of decoy documents (honeytokens) to keep the attacker online long enough to trace the connection to a KGB-linked operation. The foundational real-world cyber-deception case.
- **"An Evening with Berferd" (1991)** — Bill Cheswick lured and observed an attacker inside a controlled "jail," an early articulation of the high-interaction honeypot.
- **Deception Toolkit (1998)** — Fred Cohen's DTK, one of the first freely available honeypot tools and an early "A Framework for Deception."

## 8. Evaluation Metrics (lifecycle: testing/evaluation)

- **Alert fidelity** — interactions per false positive (should be near-perfect).
- **Interaction depth achieved** — token use vs banner probe vs full session.
- **Tradecraft captured** — new ATT&CK techniques, tools, infrastructure per engagement.
- **Time-to-detection / dwell-time reduction.**
- **Containment** — was the high-interaction host ever used as a real pivot?
- **Coverage / believability** — fraction of attack paths seeded with credible breadcrumbs.

## 9. Counter-Decoy (cyber): How Attackers Beat It

This is the cyber face of the project's counter-decoy dimension and the bridge to branch ③:

- **Fingerprinting** — default configs, characteristic banners/responses, missing real activity, timing artifacts, known honeypot software signatures.
- **Environment checks** — VM/sandbox detection, lack of user history, too-clean or implausible data.
- **Reconnaissance services** — e.g., Shodan's Honeyscore and similar tools that flag likely honeypots.
- **Anti-anti-honeypot** — hardening decoys (realistic noise, aged data, production-like fingerprints) so they survive scrutiny; the same realism/consistency problem as physical multi-spectral decoys.

## 10. Mapping to the Shared Taxonomy

| Taxonomy axis | Cyber instantiation |
|---|---|
| Feature dimension | `cyber` (and `narrative` for fake projects/identities) |
| Domain | `cyber` (with OT/ICS spanning into physical) |
| Physical evolution | classic = static honeypot; informationized = orchestrated honeynet; intelligent = adaptive/auto-generated deception and AI shells |
| Observer / victim | `cyber_intruder` (human or automated) |
| Effect mechanism | `collect_tradecraft`, `delay_decision`, `attract_fire` (attention), high-fidelity detection |
| Counter-decoy | fingerprinting, environment checks, interaction-depth testing |
