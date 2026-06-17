# Industry and Vendor Map / 厂商与市场图谱

A cross-domain map of organizations that design and build decoys and deception systems, from
inflatable physical decoys to RF/IR expendables, naval and airborne EW decoys, signature
management, and cyber deception. The structured list is [`data/vendors.csv`](../data/vendors.csv).

> **Inclusion is not endorsement.** These are public references for market mapping and capability
> taxonomy. Treat any vendor's effectiveness claims as Tier A for *product existence and stated
> specifications* and far lower for *validated battlefield or breach-detection outcomes* — the same
> rule the project applies everywhere (see [`docs/source-schema.md`](source-schema.md)).

## Categories

| Category | What they make | Examples |
|---|---|---|
| `inflatable_physical` | Inflatable/foldable replicas of vehicles, aircraft, radars, launchers | Inflatech, Sea Wolf Global, i2k, Rusbalt, ATL, Airborne Industries |
| `active_autonomous` | Mobile/remote/autonomous "active dummies" | Temerland |
| `signal_ew` | Air-launched and towed RF/EW decoys | Raytheon (MALD), BAE (ALE-55), Brunswick/IMI (TALD) |
| `naval_decoy` | Shipboard active/expendable decoys | BAE / L3Harris (Nulka) |
| `camouflage_signature` | Multispectral camouflage and signature management (adjacency) | Saab Barracuda, HDT Global |
| `cyber_deception` | Honeypots, honeytokens, deception platforms | Thinkst, SentinelOne (ex-Attivo), Proofpoint (ex-Illusive), Zscaler (ex-Smokescreen), Acalvio, Fortinet |

## Notes on the Physical-Decoy Market

The inflatable-decoy market grew sharply with the Russia-Ukraine war, but published market-size
figures are **contradictory and low-confidence**: estimates range from roughly US$150M (2024) to
US$300-500M (2025) with single-digit CAGRs, and at least one widely syndicated report conflates
military decoys with *hunting/wildlife* inflatable decoys. Do not cite a single market figure as
authoritative; if a number is needed, attribute it to a specific report and flag the divergence.

The same Ukraine demand signal recurs across reporting (Metinvest's 250+ mock-ups, Czech Inflatech
scaling production) — see the Russia-Ukraine cases in [`data/cases.csv`](../data/cases.csv).

## Notes on the Signal/EW and Cyber Markets

The signal/EW decoy field is dominated by a few primes (Raytheon, BAE Systems, L3Harris) tied to
specific fielded systems (MALD, Nulka, ALE-55) rather than a broad vendor market. The cyber
deception market has **consolidated through acquisitions** — Attivo into SentinelOne, Illusive into
Proofpoint, Smokescreen into Zscaler — so several "vendors" are now product lines inside larger
security platforms. See [`docs/cyber-decoys.md`](cyber-decoys.md).

## Caveats

- Several smaller inflatable makers (Rusbalt, ATL, Airborne Industries, Magam, Shape Inflatable,
  Hangzhou Gauss) appear mainly in syndicated market reports; their entries in `vendors.csv` have
  no verified URL and are marked accordingly.
- Camouflage/signature-management vendors (Saab Barracuda, HDT Global) are an **adjacency**: their
  core business is reducing observability, with decoy/deception product lines alongside.
- Brunswick/IMI is listed as `legacy` (TALD/Samson origin); the lineage now sits within other primes.
