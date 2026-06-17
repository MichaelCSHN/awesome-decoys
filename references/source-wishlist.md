# Source Wishlist

[English](source-wishlist.md) | [中文](source-wishlist.zh-CN.md)

This file tracks source-acquisition gaps. It is intentionally separate from
[`sources.md`](sources.md): the source index records what the project already has, while this
wishlist records what should be strengthened next.

## Coverage Target

For a case to be considered well-supported:

- It should have at least two independent `source_refs`.
- At least one source should be Tier A or A/B.
- Current-conflict battlefield effects should be corroborated by more than one outlet, or explicitly marked as reported/provisional.
- Vendor pages should be used for product existence and claimed specifications, not for validated combat effectiveness.
- Technical methods should prefer peer-reviewed papers, patents/specifications, official test reports, or military research reports over blog explainers.

## Priority Backlog

| Priority | Area | Current weakness | Source target |
|---|---|---|---|
| P0 | Recent LUCAS / Epic Fury claims | Official and specialist anchors are now present, but the exact decoy/saturation role is still under-corroborated | Add more official after-action detail, procurement traces, imagery analysis, or independent defense-media confirmation of LUCAS employment as decoy/saturation rather than only one-way attack |
| P0 | Russia-Ukraine decoy combat effects | Strike counts, destroyed-decoy claims, and BDA remain media-reported | Add geolocated OSINT threads only when archived and independently checked; prefer official Ukrainian/Russian statements plus independent imagery analysis |
| P1 | WWII Starfish sites | `HIST-WWII-STARFISH` still leans on secondary visual articles | Add UK National Archives, Historic England, IWM, or official civil-defense histories |
| P1 | Houthi Red Sea decoys | Threat inventory and cost-exchange are now better anchored; ground-decoy and launcher-survivability claims remain indirect | Add UKMTO, US Navy, CRS/GAO, IISS, RUSI, imagery analysis, or official after-action sources on launchers, decoys, and strike effectiveness |
| P1 | Counter-decoy IR and multispectral discrimination | Some method cases still use broad explainers | Add SPIE/IEEE/DTIC/NATO STO papers on imaging-IR seeker discrimination, multispectral target recognition, and SAR/EO fusion |
| P1 | Space decoys and counter-decoy discrimination | Existing space coverage is mostly ballistic-missile midcourse penaids | Add missile-defense discrimination, satellite decoy/proximity-operation, space-domain-awareness, and inflatable/reflector target sources from MDA, GAO, CRS, CSIS, RAND, IAC/AIAA, and peer-reviewed astrodynamics literature |
| P1 | Underwater decoys and unmanned undersea systems | Nixie is present, but underwater soft-kill, acoustic countermeasure, and UUV decoy coverage is thin | Add naval torpedo-defense manuals, NATO STO/ONR papers, vendor specs, and research on mobile acoustic decoys, expendable bathythermograph-like devices, and UUV false targets |
| P1 | AI / ATR / autonomous counter-decoy | ATR/adversarial robustness exists, but AI-generated decoys and autonomous deception planning are under-covered | Add papers on SAR/EO ATR, physical adversarial examples, generative camouflage, simulation-to-real target synthesis, and autonomous multi-agent deception |
| P1 | Unmanned decoy systems | Modern An-2 and LUCAS-style entries need broader context | Add loitering decoys, MALD-X/MALD-N, UAV-borne RF emitters, attritable loyal-wingman decoy roles, autonomous swarm decoys, and exercise/test sources |
| P2 | Cyber anti-honeypot | `CYBER-ANTI-HONEYPOT` is still mostly tool-list / explainer driven | Add academic work on honeypot fingerprinting, adversary interaction, and deception-system evaluation |
| P2 | Vendor catalogs | Product lists exist, but many are not archived or normalized by generation and spectrum | Add PDFs, archived pages, patent families, and procurement notices for each major vendor family |

## Source-Hunting Queries

Use targeted searches first:

- `site:dtic.mil decoy deception infrared flare imaging seeker discrimination`
- `site:apps.dtic.mil multispectral target recognition decoy discrimination`
- `site:spiedigitallibrary.org infrared countermeasure flare discrimination`
- `site:ieeexplore.ieee.org SAR decoy discrimination polarimetric`
- `site:gao.gov decoy deception missile defense discrimination`
- `site:crsreports.congress.gov deception decoy missile defense`
- `site:mda.mil discrimination decoys countermeasures missile defense`
- `site:csis.org missile defense decoys discrimination space`
- `site:rand.org space deception decoy counterspace`
- `site:navalpostgraduate.edu torpedo decoy acoustic countermeasure`
- `site:onr.navy.mil acoustic decoy unmanned undersea`
- `site:sto.nato.int decoy acoustic torpedo countermeasure`
- `site:darpa.mil MALD-X decoy autonomous electronic warfare`
- `site:afresearchlab.com autonomous decoy aircraft electronic warfare`
- `site:ieeexplore.ieee.org adversarial examples SAR ATR physical`
- `site:arxiv.org generative camouflage decoy target recognition`
- `site:discovery.nationalarchives.gov.uk Operation Mincemeat decoy`
- `site:nationalarchives.gov.uk Starfish decoy sites`
- `site:centcom.mil Houthi decoy launcher`

## When To Promote A Source

Promote a case from weak to strong only when the source changes the evidence posture:

- C to B: a named reporter, specialist outlet, or expert account adds independent detail.
- B to A/B: a professional military journal, named practitioner article, or technical paper supports the mechanism.
- A/B to A: official/institutional documents, archival records, RAND-class reports, peer-reviewed work, or vendor documents for product-existence claims.

Do not promote a case merely because more articles repeat the same upstream claim.
