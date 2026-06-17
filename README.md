# Awesome Decoys / 假目标与诱饵大全

> A curated knowledge base on dummy targets, decoys, deception systems, physical and signal decoys, cyber deception, multi-spectral signatures, active decoys, and autonomous attritable systems.
>
> 本项目面向“假目标/诱饵”建立公开资料层面的大全：覆盖古往今来的案例、实体/信号/网络形态、经典式/机械化/信息化/智能化演进，以及设计、制造、部署、测试和评估等技术环节。

## Contents

- [Core Ideas](#core-ideas)
- [Scope and Taxonomy](#scope-and-taxonomy)
- [Reading Map](#reading-map)
- [Case Database](#case-database)
- [Source Quality Tiers](#source-quality-tiers)
- [Doctrine and Concepts](#doctrine-and-concepts)
- [Modern Battlefield Lessons](#modern-battlefield-lessons)
- [Recent Conflicts (2020-2026)](#recent-conflicts-2020-2026)
- [Signal and Expendable Decoy Hardware](#signal-and-expendable-decoy-hardware)
- [Inflatable and Physical Decoys](#inflatable-and-physical-decoys)
- [Active and Autonomous Decoys](#active-and-autonomous-decoys)
- [Electromagnetic and Multi-Spectral Deception](#electromagnetic-and-multi-spectral-deception)
- [Cyber Decoys (Honeypots, Honeytokens, Deception)](#cyber-decoys-honeypots-honeytokens-deception)
- [Counter-Decoy and Discrimination](#counter-decoy-and-discrimination)
- [Aircraft and Airbase Decoys](#aircraft-and-airbase-decoys)
- [Armored Vehicle and Artillery Decoys](#armored-vehicle-and-artillery-decoys)
- [Industry and Vendors](#industry-and-vendors)
- [Autonomous Decoy Aircraft System](#autonomous-decoy-aircraft-system)
- [Technology Keywords](#technology-keywords)
- [Research Questions](#research-questions)
- [Additional Source Index](#additional-source-index)
- [Local Seed Documents](#local-seed-documents)
- [To-Do](#to-do)

## Core Ideas

- **Decoy as a universal method** - A decoy can be an object, signal, behavior, identity, account, system, or story that causes an observer or weapon system to allocate attention or action incorrectly.
- **Transparent battlefield** - Persistent ISR, drones, SAR, infrared sensing, SIGINT, and AI-assisted recognition are compressing the time from detection to strike.
- **Decoys as protection** - Decoys shift protection from passive hiding toward active manipulation of the adversary's targeting cycle.
- **Cost imposition** - A low-cost false target can force expenditure of expensive precision weapons and scarce ISR attention.
- **Multi-spectral credibility** - Effective decoys increasingly need optical, thermal, radar, electromagnetic, and behavioral consistency.
- **From static to active** - The development path is moving from visual mockups to remotely controlled, autonomous, sensor-aware, and swarm-capable decoy systems.
- **Deception as a system** - The most valuable decoy is not an isolated object, but part of a larger false battlefield narrative.

## Scope and Taxonomy

The full taxonomy is maintained in [`docs/taxonomy.md`](docs/taxonomy.md). The case-data schema is maintained in [`docs/case-schema.md`](docs/case-schema.md).

![Generational evolution of decoy and deception, from classic manual ruses to intelligent autonomous systems, with representative cases colour-coded by feature dimension](assets/taxonomy-evolution.svg)

This project organizes dummy/decoy systems along several dimensions:

### Time Dimension

- **Ancient and pre-industrial** - Dummy camps, false fires, decoy formations, feigned retreats, ruses, and visual deception before mechanized sensing.
- **Industrial age** - Dummy guns, ships, airfields, factories, camouflage schools, and deception at operational scale.
- **Cold War and precision-strike age** - Radar decoys, missile decoys, mobile launcher ambiguity, air-defense deception, electronic warfare, and hardened-site deception.
- **Contemporary transparent battlefield** - Drone-observed decoys, inflatable weapon systems, false command posts, multi-spectral signatures, AI-assisted target recognition, and cost-imposition.
- **Emerging intelligent deception** - Autonomous decoy vehicles, adaptive signature control, decoy swarms, cyber-physical deception, synthetic data, and closed-loop deception effects assessment.

### Feature Dimension

- **Physical/entity decoys** - Dummy tanks, aircraft, ships, missiles, artillery, radars, C2 nodes, bridges, buildings, supply depots, and personnel-like objects.
- **Signal decoys** - Radio traffic, radar reflectors, RF beacons, false electromagnetic emissions, acoustic signatures, thermal signatures, and synthetic radar returns.
- **Behavioral decoys** - Movement patterns, maintenance routines, convoy timing, patrol tracks, launch preparation, airbase operating rhythm, and pattern-of-life fabrication.
- **Cyber decoys** - Honeypots, honeytokens, fake credentials, decoy services, deception networks, bogus data, false identities, and adversary-engagement environments.
- **Narrative and intelligence decoys** - False orders of battle, double-agent channels, controlled leaks, misleading logistics traces, and cross-source false confirmation.

### Physical Evolution Dimension

- **Classic / manual** - Wood, canvas, fabric, fires, painted surfaces, dummy camps, and hand-built mockups.
- **Mechanical / deployable** - Inflatable forms, foldable frames, trailers, mobile mockups, emitters, heaters, corner reflectors, and towable/relocatable decoys.
- **Informationized / networked** - Electromagnetic signature generators, programmable emissions, sensor-triggered decoying, remote control, distributed false nodes, and multi-source coordination.
- **Intelligent / autonomous** - Unmanned decoy vehicles, autonomous repositioning, adaptive thermal/RF control, swarm behavior, AI-generated signatures, and closed-loop assessment.

### Technology Lifecycle Dimension

- **Design and generation** - Target-signature modeling, threat-sensor modeling, CAD/digital twins, synthetic image generation, RCS/thermal/acoustic design, cyber lure design, and scenario generation.
- **Production and manufacturing** - Inflatable production, additive manufacturing, modular frames, coatings, heaters, RF payloads, low-cost electronics, cyber range templates, and field-repair kits.
- **Deployment and operation** - Placement, concealment, activation timing, mobility, emission control, logistics, operator workload, deception story coherence, and integration with real forces.
- **Testing and evaluation** - Sensor-facing tests, red-team classification, BDA ambiguity, cost-exchange analysis, survivability modeling, cyber engagement metrics, and closed-loop deception effectiveness.

### Additional Dimensions

- **Domain** - Land, air, sea, undersea, space, electromagnetic spectrum, cyber, information, and cross-domain decoys.
- **Target class** - Personnel, vehicles, aircraft, ships, missiles, radars, air-defense systems, C2 nodes, logistics, infrastructure, satellites, identities, services, and datasets.
- **Observer or victim** - Human observer, aircraft pilot, UAV operator, satellite analyst, radar processor, missile seeker, AI classifier, cyber intruder, or decision-maker.
- **Effect mechanism** - Attract fire, absorb munitions, delay decisions, overload ISR, mask real movement, corrupt BDA, create false confidence, expose enemy sensors, or shape enemy maneuver.
- **Fidelity level** - Visual-only, single-signature, multi-spectral, behavioral, networked, or story-level deception.
- **Maturity level** - Concept, historical case, prototype, training aid, commercial product, fielded system, combat-observed system, or validated operational effect.
- **Cost and scalability** - One-off artisanal, unit-built, commercial batch, mass-producible, attritable, reusable, or software-replicable.
- **Counter-decoy angle** - SAR/IR/radar/EO anomaly detection, pattern-of-life validation, AI classifier robustness, multi-source fusion, cyber fingerprinting, and forensic attribution.
- **Source type / provenance** - The genre of the knowledge itself: peer-reviewed journals, conference papers, books, think-tank reports, government/military documents, professional military journals, trade defense media, news media, vendor/industry materials, analysis blogs, OSINT/social media, datasets, and institutional references. This axis is orthogonal to the A/B/C/D quality tier and is recorded per source in [`data/sources.csv`](data/sources.csv).

## Reading Map

### Start Here

- [Like Moths to a False Flame: Lethality and Protection through Deception Operations](https://www.army.mil/article/286861/like_moths_to_a_false_flame_lethality_and_protection_through_deception_operations) - U.S. Army article framing deception as a way to force adversaries to react to false information and waste resources.
- [A Tool for Deception: The Urgent Need for EM Decoys](https://warroom.armywarcollege.edu/articles/tactical-decoys/) - U.S. Army War College article focused on electromagnetic decoys and low-cost spectrum deception.
- [Implementing DoD Replicator Initiative at Speed and Scale](https://www.diu.mil/latest/implementing-the-department-of-defense-replicator-initiative-to-accelerate) - DIU article on scaling all-domain attritable autonomous systems.
- [Russia And Ukraine Are Deploying Increasingly Advanced Decoy Tanks](https://www.forbes.com/sites/vikrammittal/2025/03/03/russia-and-ukraine-are-deploying-increasingly-advanced-decoy-tanks/) - Forbes overview of decoy armored vehicles in the Russia-Ukraine war.
- [Sea Wolf Global F-35 Jet Fighter Decoy System](https://www.seawolfglobal.com/dni/product_f35.html) - Public product page for an inflatable F-35 decoy system.

### For a Technical Overview

- [INFLATECH - Inflatable Military Decoys](https://www.inflatechdecoy.com/) - Vendor overview of inflatable decoy categories and use cases.
- [INFLATECH News](https://www.inflatechdecoy.com/news/) - Vendor news mentioning realistic thermal and radar signatures in current decoy offerings.
- [Sea Wolf Global](https://seawolf502.cafe24.com/shop3/) - Company overview linking inflatable decoys with unmanned/robotic control concepts.
- [Temerland Leopard Tank Decoy](https://temerland.com/en/temerland-is-making-an-unmanned-model-of-a-leopard-tank-based-on-a-regular-car-to-fool-russians/) - Example of a mobile/remote-controlled "active dummy" concept based on a regular vehicle.

### For Historical and Doctrinal Context

- [Hiding in Plain Sight](https://www.armyupress.army.mil/Journals/Military-Review/English-Edition-Archives/March-April-2023/Hiding/) - Army University Press article on deception planning and decoy positions.
- [Deception in the Desert](https://www.armyupress.army.mil/Books/Browse-Books/iBooks-and-EPUBs/Deception-in-the-Desert/) - Historical case on deception in Operation Desert Storm.
- [Assault on Fortress Europe](https://www.armyupress.army.mil/Journals/Military-Review/Online-Exclusive/2020-OLE/Carminati-Assault-Fortress-Europe/) - Discussion of Operation Fortitude South and physical/signals deception before D-Day.

## Case Database

The initial case database is available at [`data/cases.csv`](data/cases.csv). It is structured for later import into Excel, SQLite, Notion, or a small static site.

An interactive, offline, self-contained browser for all cases — filter by category, source tier, and era, with full-text search — is at [`assets/cases-explorer.html`](assets/cases-explorer.html) (open it in any browser).

Core fields:

- `case_id` - Stable case identifier.
- `period` / `time_dimension` - Year, era, conflict period, or historical phase.
- `actor` - Country, force, organization, vendor, or initiative.
- `domain` - Land, air, sea, undersea, space, electromagnetic spectrum, cyber, information, or cross-domain.
- `target_or_platform` - What the decoy imitates or protects.
- `decoy_form` - Physical/entity, signal, behavioral, cyber, narrative, inflatable, electromagnetic, active/mobile, autonomous, or mixed.
- `mobility` - Static, relocatable, mobile, remotely controlled, or autonomous.
- `spectral_features` - Optical, thermal, radar, electromagnetic, behavioral, or multi-spectral features.
- `lifecycle_stage` - Design/generation, production/manufacturing, deployment/operation, testing/evaluation, or combat use.
- `deception_effect` - Intended effect on enemy ISR, targeting, fires, BDA, or resource allocation.
- `source_quality` - A/B/C/D source tier as defined below.
- `source_refs` - Short source keys mapped in [`references/sources.md`](references/sources.md).

Every row also carries `feature_dimension` (physical/signal/behavioral/cyber/narrative/mixed), `domain` (land/air/sea/space/ems/cyber/information/cross_domain), and `physical_evolution` (classic/mechanical/informationized/intelligent) — the axes the case explorer filters on.

Initial cases:

| Case | Period | Focus | Why It Matters |
|---|---:|---|---|
| Ancient and classical ruses | antiquity | Dummy camps, feigned retreats, the Trojan Horse archetype | Shows the decoy logic — manufacturing a false belief — long before sensors and precision fires. |
| Q-ships | 1915-1918 | Disguised armed merchantmen baiting U-boats | Naval decoy ancestor; deception plus staged behavior ("panic party"). |
| WWII Starfish sites and dummy airfields | 1940-1944 | Decoy fires/lights and dummy airfields in the Blitz | Early state-organized decoy program drawing bomb tonnage onto empty ground. |
| The Ghost Army (23rd HQ Special Troops) | 1944-1945 | Inflatable tanks, sonic deception, fake radio, impersonation | Multi-cue consistency exemplar; the model for modern multi-spectral decoys. |
| Operation Fortitude South | 1944 | False army, dummy landing craft, radio traffic, double agents | Classic example of physical, signals, and human-source deception reinforcing one false operational story. |
| Desert Storm deception | 1990-1991 | Amphibious feint, force posture deception, false attack expectation | Shows deception integrated with maneuver and operational design rather than isolated decoy objects. |
| Desert Storm Scud hunt | 1991 | Mobile missile TEL ambiguity and decoy/similar-vehicle problem | Demonstrates how mobile false targets and uncertainty can consume disproportionate ISR and strike effort. |
| Kosovo / Operation Allied Force | 1999 | Serbian camouflage, decoys, emission discipline, shoot-and-scoot IADS | Shows how a weaker force can preserve assets by exploiting target-identification uncertainty. |
| Nagorno-Karabakh An-2 bait drones | 2020 | Expendable manned-aircraft-turned-drones used as SEAD bait | Flagship case of an attritable decoy used to expose and suppress enemy air defenses. |
| Russia-Ukraine inflatable decoys | 2022-present | Tanks, artillery, aircraft, HIMARS-like systems | Current cost-imposition case under drones, precision fires, thermal sensors, and public BDA. |
| Iran-Israel direct strikes | 2024-2025 | Saturation salvos, mixed threats, maneuvering/cluster warheads | Decoy-as-signal: overwhelms tracking and prioritization and depletes expensive interceptors. |
| Houthi Red Sea campaign | 2023-present | Cheap drones/missiles vs multimillion-dollar interceptors | Pure cost-exchange/asymmetry case; mobile launchers and ground decoys frustrate counter-strikes. |
| Sea Wolf F-35 decoy | 2020s | Inflatable aircraft decoy with thermal/radar categories | Useful industry example for airbase survivability and autonomous decoy aircraft requirements. |
| Temerland active Leopard decoy | 2020s | Vehicle-based mobile/remote decoy concept | Bridges passive mockup and active behavioral deception. |
| EM decoy / false C2 node concepts | 2020s | Spectrum deception, fake emissions, command-post decoys | Extends decoy thinking from visible objects to detectable signatures. |
| Agile Combat Employment context | 2020s | Airbase dispersion, survivability, threat timelines | Provides the operational setting where aircraft decoys, false parking patterns, and distributed base deception matter. |

## Source Quality Tiers

- **A - Primary official / institutional**: doctrine, official military articles, government reports, RAND or equivalent research reports, vendor pages for their own products.
- **B - Reputable reporting / specialist media**: AP, RFE/RL, Forbes, The War Zone, professional defense media, named expert articles.
- **C - Secondary aggregation**: blogs, market reports, republications, unsourced summaries, or articles derived mainly from other reporting.
- **D - Unverified / social**: social media posts, videos, image-only claims, or claims that need independent confirmation.

Use source tiering conservatively: a vendor page can be Tier A for product claims but not for independent effectiveness claims; media can be Tier B for reported observations but should not be treated as validated combat assessment without corroboration.

## Doctrine and Concepts

- [Deception Operations - Army University Press PDF](https://www.armyupress.army.mil/Portals/7/combat-studies-institute/csi-books/bjorge2.pdf) - Older but useful study of deception doctrine, fundamentals, and historical examples.
- [Hiding in Plain Sight](https://www.armyupress.army.mil/Journals/Military-Review/English-Edition-Archives/March-April-2023/Hiding/) - Useful for framing deception as integrated with reconnaissance, fires, and intelligence.
- [Sustainment Survivability: Incorporating Deception at the Tactical Level](https://www.army.mil/article/267685/sustainment_survivability_incorporating_deception_at_the_tactical_level_in_the_brigade_support_area) - Tactical deception in support areas and logistics survivability.
- [Dispersion as Uncertainty](https://www.armyupress.army.mil/Journals/Military-Review/Online-Exclusive/2025-OLE/Dispersion-as-Uncertainty/) - Links dispersion, uncertainty, targeting triage, and deception.
- [A Layered Approach to Active Protection](https://www.lineofdeparture.army.mil/Journals/Protection/Protection-Archive/2026-Edition/A-Layered-Approach-to-Active-Protection/) - Discusses deception as part of active protection.

## Modern Battlefield Lessons

- [Like Moths to a False Flame](https://www.army.mil/article/286861/like_moths_to_a_false_flame_lethality_and_protection_through_deception_operations) - Emphasizes rapid sensor-to-shooter cycles and the role of deception in degrading targeting.
- [Beyond the Count: BDA for Modern Warfare](https://www.lineofdeparture.army.mil/Journals/Military-Intelligence/Military-Intelligence-Archive/2025-July-December/Beyond-the-Count/) - Notes that decoys and deception complicate battle damage assessment.
- [Russia And Ukraine Are Deploying Increasingly Advanced Decoy Tanks](https://www.forbes.com/sites/vikrammittal/2025/03/03/russia-and-ukraine-are-deploying-increasingly-advanced-decoy-tanks/) - Useful case material on decoy evolution under drone observation.
- [Inflatable Tanks And Missiles: Czech Firm Makes Decoy Armaments](https://apnews.com/article/a9c478adb9d7ecaa615cb19b25f4833f) - AP report on increased demand for inflatable decoys during the Russia-Ukraine war.
- [Inflatable Tanks And Missiles: Czech Firm Makes Decoy Armaments](https://www.rferl.org/a/czech-inflatable-weapon-decoys-ukraine/32305583.html) - RFE/RL version with visuals and production context.

## Recent Conflicts (2020-2026)

These are the recent, well-observed cases that show the two dominant modern decoy logics: **decoy-as-object** (cheap physical false targets that absorb precision fires) and **decoy-as-signal** (saturation, mixed salvos, and penetration aids that overwhelm a defender's tracking, prioritization, and interceptor magazine). A recurring theme is the **cost-exchange**: a low-cost decoy or munition forcing the expenditure of a far more expensive interceptor or strike weapon.

### Nagorno-Karabakh 2020 - SEAD by decoy

- Azerbaijan flew Soviet-era An-2 biplanes, converted into expendable one-way drones, as bait to make Armenian air defenses activate and fire, exposing their positions for Bayraktar TB2 and Harop strikes. This is the flagship modern example of an attritable decoy used for suppression of enemy air defenses.
- [Lessons from the Nagorno-Karabakh 2020 Conflict](https://api.army.mil/e2/c/downloads/2023/01/31/693ac148/21-655-nagorno-karabakh-2020-conflict-catalog-aug-21-public.pdf) - U.S. Army lessons catalog.
- [The 2020 Nagorno Karabakh War: Unmanned Combat](https://www.raf.mod.uk/what-we-do/centre-for-air-and-space-power-studies/aspr/aspr-vol25-iss2-3-pdf/) - RAF Air and Space Power Review.
- [The next frontier in drone warfare? A Soviet-era crop duster](https://thebulletin.org/2021/02/the-next-frontier-in-drone-warfare-a-soviet-era-crop-duster/) - Bulletin of the Atomic Scientists.

### Russia-Ukraine - decoy HIMARS and aerial/airbase decoys

- Ukraine baited Russian Kalibr and Iskander strikes onto wooden and higher-fidelity HIMARS/M777/radar mock-ups; one firm reportedly built 250+ replicas. Russia in turn used inert cruise missiles and Iranian-type drones as decoys, inflatable command posts, decoy balloons, and painted bomber silhouettes (e.g., at Engels).
- [Ukraine lures Russian missiles with decoys of U.S. rocket system](https://www.washingtonpost.com/world/2022/08/30/ukraine-russia-himars-decoy-artillery/) - The Washington Post.
- [Real Kalibr missiles vs HIMARS decoys](https://www.pravda.com.ua/eng/articles/2024/03/11/7445807/) - Ukrainska Pravda.
- [Decoy Warfare: Lessons and Implication from the War in Ukraine](https://www.usni.org/magazines/proceedings/2024/april/decoy-warfare-lessons-and-implication-war-ukraine) - U.S. Naval Institute Proceedings (also covers Russian aerial decoys).

### Iran-Israel and US-Israel-Iran - saturation and penetration aids

- Across True Promise I and II (2024) and the twelve-day June 2025 war (Rising Lion / True Promise III, with US strikes on Iranian nuclear sites), Iran's method was less about physical dummies and more about decoying the *defense*: large mixed salvos, then ballistic-heavy saturation with maneuvering and cluster/submunition warheads to dilute tracking fidelity and drain scarce, expensive interceptors (Arrow, David's Sling, THAAD, SM-3, Patriot). The April 2024 intercept night reportedly cost the defender on the order of US$1B.
- [Shallow Ramparts: Air and Missile Defenses in the June 2025 Israel-Iran War](https://www.fpri.org/article/2025/10/shallow-ramparts-air-and-missile-defenses-in-the-june-2025-israel-iran-war/) - Foreign Policy Research Institute.
- [Iran Is Piercing Israel's Ballistic Missile Defenses With High-Altitude Cluster Warhead Releases](https://www.twz.com/land/iran-is-piercing-israels-ballistic-missile-defenses-with-high-altitude-cluster-warhead-releases) - The War Zone.

### Houthi / Red Sea - the cost-exchange problem

- Since late 2023, cheap (~US$2k-40k) one-way drones and missiles forced US/coalition warships to expend multimillion-dollar interceptors; shore-based mobile launchers and decoy systems complicated counter-targeting. The asymmetry is the lesson, not any single intercept.
- [Cheap Houthi Drones Are Draining the Pentagon's Coffers](https://newlinesmag.com/argument/cheap-houthi-drones-are-draining-the-pentagons-coffers/) - New Lines Magazine.
- [How Yemen's Houthi rebels have leveraged cheap drones into military success](https://www.nbcnews.com/tech/security/yemens-houthi-rebels-used-cheap-drones-attacks-years-rcna135117) - NBC News.

### Reversing the equation - offensive decoys (provisional)

- Reporting in 2026 describes US Central Command using massed low-cost decoy drones (LUCAS) offensively against Iranian air defenses to open windows for follow-on strikes, inverting the Red Sea cost logic and echoing the Nagorno-Karabakh decoy-SEAD pattern at scale. Single-outlet and recent; treat as provisional.
- [From Red Sea Defense to Epic Fury: How the U.S. Flipped the Drone Cost Equation](https://defense.info/featured-story/2026/03/from-red-sea-defense-to-epic-fury-how-the-u-s-flipped-the-drone-cost-equation/) - Defense.info.

> Source keys and tiers for all of the above are in [`references/sources.md`](references/sources.md) under "Recent Conflict Decoy and Saturation Cases (2020-2026)". Strike counts, intercept percentages, and cost figures are reported estimates that vary by source; keep them separate from validated effects.

## Signal and Expendable Decoy Hardware

This is the backbone of the **signal feature dimension** and the **informationized generation**: fielded systems that imitate a platform's *signature* (radar, infrared, acoustic) rather than its shape. They are recorded in [`data/cases.csv`](data/cases.csv) with the `SIG-` and `HIST-1982-BEKAA` keys.

The throughline is an arms race against the seeker: each decoy works until the sensor learns to discriminate it (Doppler processing vs chaff, imaging-IR vs flares, midcourse discrimination vs penaids), which links this section directly to the counter-decoy branch.

### Expendable RF/IR countermeasures (chaff and flares)

- The oldest signal decoys still in daily use. Chaff (RF) dates to WWII "Window"; flares (IR) are magnesium or multispectral/kinematic payloads that present a hotter, aircraft-like target to a heat-seeker. Dispensed by systems such as the AN/ALE-47.
- [Flares - Infrared Countermeasures](https://www.globalsecurity.org/military/systems/aircraft/systems/flares.htm) - GlobalSecurity.org (chaff, flares, ALE-47).
- [Chaff (countermeasure)](https://en.wikipedia.org/wiki/Chaff_(countermeasure)) - origin and Doppler discrimination.

### Air-launched decoys: TALD and MALD

- The lineage runs ADM-20 Quail (1950s-60s, B-52-carried) -> Samson/ADM-141 TALD/ITALD (Bekaa 1982, Desert Storm 1991) -> DARPA MALD -> ADM-160 MALD/MALD-J (SEAD; combat use reported in Ukraine). These mimic an aircraft's radar cross-section, and the jammer variant (MALD-J) adds stand-in jamming.
- [ADM-141 TALD/ITALD](https://man.fas.org/dod-101/sys/ac/equip/tald.htm) - FAS (DoD-101).
- [ADM-160 MALD](https://www.airandspaceforces.com/weapons/adm-160-mald/) - Air & Space Forces Magazine.

### Towed decoys (air)

- Off-board RF decoys streamed behind the aircraft to pull a radar-guided missile's lock onto the towed body. The ALE-50 ("Little Buddy") is combat-proven; the ALE-55 fiber-optic towed decoy is part of the IDECM suite with the AN/ALQ-214.
- [AN/ALE-50 towed decoy system](https://en.wikipedia.org/wiki/AN/ALE-50_towed_decoy_system) and [AN/ALE-55 fiber-optic towed decoy](https://en.wikipedia.org/wiki/AN/ALE-55_fiber-optic_towed_decoy).

### Naval and undersea decoys: Nulka and Nixie

- Nulka (MK 53) is a rocket-propelled hovering active RF decoy that radiates a large false ship return to seduce anti-ship missiles off the ship. AN/SLQ-25 Nixie is the acoustic analogue: a towed electro-acoustic decoy that lures acoustic/wake-homing torpedoes away from the hull.
- [MK 53 Decoy Launching System (Nulka)](https://www.navy.mil/Resources/Fact-Files/Display-FactFiles/Article/2167877/mk-53-decoy-launching-system-nulka/) - U.S. Navy.
- [AN/SLQ-25 Nixie](https://man.fas.org/dod-101/sys/ship/weaps/an-slq-25.htm) - FAS (DoD-101).

### Strategic penetration aids

- At the strategic scale, ICBM reentry vehicles travel with balloon decoys, chaff, replica RVs, IR-signature masking, and anti-simulation (making the warhead look like a decoy). This is the unsolved midcourse **discrimination problem** that drives missile-defense radar and interceptor design.
- [Countermeasures, Penetration Aids, and Missile Defense](https://missilethreat.csis.org/countermeasures-penetration-aids-and-missile-defense/) - CSIS Missile Threat.

> Full source keys and tiers are in [`references/sources.md`](references/sources.md) under "Signal and Expendable Decoy Hardware".

## Inflatable and Physical Decoys

- [INFLATECH - Inflatable Military Decoys](https://www.inflatechdecoy.com/) - Czech producer of inflatable military decoys.
- [INFLATECH News](https://www.inflatechdecoy.com/news/) - Mentions participation in defense exhibitions and thermal/radar signature replication.
- [AP: Czech Firm Makes Decoy Armaments](https://apnews.com/article/a9c478adb9d7ecaa615cb19b25f4833f) - Public reporting on decoy production scale, setup time, and cost-imposition logic.
- [RFE/RL: Czech Firm Makes Decoy Armaments](https://www.rferl.org/a/czech-inflatable-weapon-decoys-ukraine/32305583.html) - Complementary report on Inflatech and Ukraine-related demand.
- [NorseStorm - Inflatable Decoys](https://www.norsestorm.com/product-categories/inflatable-decoys) - Distributor page summarizing product categories such as tanks, radars, launchers, trucks, aircraft, and naval targets.
- [i2k Defense - Inflatable Decoys and Targets](https://i2kdefense.com/inflatable-decoys-and-targets/) - U.S. provider of inflatable replicas for training and decoy roles.

## Active and Autonomous Decoys

- [DIU Replicator Initiative](https://www.diu.mil/latest/implementing-the-department-of-defense-replicator-initiative-to-accelerate) - Strategic context for scalable attritable autonomous systems.
- [DIU Software Vendors to Support Replicator](https://www.diu.mil/latest/defense-innovation-unit-announces-software-vendors-to-support-replicator) - Highlights process acceleration and autonomy software support.
- [Temerland Active Dummy Leopard Concept](https://temerland.com/en/temerland-is-making-an-unmanned-model-of-a-leopard-tank-based-on-a-regular-car-to-fool-russians/) - Mobile decoy concept using a regular vehicle as the base.
- [Sea Wolf Global](https://seawolf502.cafe24.com/shop3/) - Mentions combining inflatable decoys with robot control systems and unmanned control.
- [War Room: Army of 2040](https://warroom.armywarcollege.edu/articles/army-of-2040/) - Future-oriented discussion that includes autonomous decoys and dynamic electronic signatures.

## Electromagnetic and Multi-Spectral Deception

- [A Tool for Deception: The Urgent Need for EM Decoys](https://warroom.armywarcollege.edu/articles/tactical-decoys/) - Best starting point for electromagnetic decoy concepts.
- [Sea Wolf Global F-35 Jet Fighter Decoy System](https://www.seawolfglobal.com/dni/product_f35.html) - Public decoy product page mentioning infrared, thermal, radar reflector, and wireless-control categories.
- [Interesting Engineering: Inflatable F-35 Decoy](https://interestingengineering.com/military/inflatable-f35-military-decoy) - Media report on F-35 decoy thermal/radar signaling and rapid deployment.
- [Seawolf Marine F-35 Decoy - Chosun Biz](https://biz.chosun.com/en/en-industry/2025/10/03/KHVUVUJHANEXHGELA7EZOPDXT4/) - Korean business media coverage of the F-35 inflatable decoy.
- [Synthetic Aperture Radar: Detecting Russian Inflatable Decoys with SAR](https://syntheticapertureradar.com/detecting-russian-inflatable-decoys-with-sar/) - Useful for understanding the counter-detection side of decoys and SAR interpretation.

## Cyber Decoys (Honeypots, Honeytokens, Deception)

The cyber-domain branch of decoys. The full chapter is in [`docs/cyber-decoys.md`](docs/cyber-decoys.md); cases use the `CYBER-` keys in [`data/cases.csv`](data/cases.csv).

A cyber decoy is a host, service, account, file, credential, or token whose only purpose is to be touched by the wrong person, so that any interaction is a high-confidence intrusion signal. The same logic as a physical decoy — cheap to deploy, expensive to evade, and an arms race against an adversary who learns to fingerprint it.

The decoy ladder runs by interaction depth: **honeytokens** (single bait data items) -> **low-interaction honeypots** (emulated services) -> **high-interaction honeypots** (real OS/services) -> **honeynets** (networks of the above) -> **distributed deception platforms** (enterprise-wide decoys plus breadcrumbs).

- [MITRE Engage](https://engage.mitre.org/) - adversary-engagement framework (replaced MITRE Shield in 2022); maps to ATT&CK.
- [MITRE D3FEND](https://d3fend.mitre.org/) - defensive techniques including explicit decoy techniques.
- [The Honeynet Project](https://www.honeynet.org/) - the long-running nonprofit honeypot research community.
- [Canarytokens](https://canarytokens.org/) - free honeytoken generator (Thinkst); the data-level tripwire.
- [T-Pot](https://github.com/telekom-security/tpotce) - all-in-one platform bundling 20+ open-source honeypots; with [Cowrie](https://github.com/cowrie/cowrie) (SSH/Telnet), [Dionaea](https://github.com/DinoTools/dionaea) (malware collection), and [Conpot](https://github.com/mushorg/conpot) (ICS/SCADA).
- [awesome-honeypots](https://github.com/paralax/awesome-honeypots) - community catalog of the wider tool ecosystem.

Historical anchors: Clifford Stoll's *The Cuckoo's Egg* (1986-87, fake "SDInet" decoy documents), Cheswick's "An Evening with Berferd" (1991), and Fred Cohen's Deception Toolkit (1998). Commercial deception technology has consolidated into platforms such as SentinelOne Singularity Identity (ex-Attivo), Proofpoint Shadow (ex-Illusive), and Zscaler Deception (ex-Smokescreen) — treat vendor effectiveness claims with the same caution as physical-decoy vendors.

## Counter-Decoy and Discrimination

The capstone branch: how decoys are detected and defeated, framed as one arms race between decoy realism and sensor/algorithm discrimination. Full chapter in [`docs/counter-decoy.md`](docs/counter-decoy.md); cases use the `CD-` keys in [`data/cases.csv`](data/cases.csv).

The master principle is **consistency**: a real target is self-consistent across shape, temperature, radar scattering, motion, emissions, supporting activity, and logistics. A decoy is cheap because it fakes some cues and not others, so discrimination is the search for the cue it got wrong or the contradiction between cues.

The throughline across every branch of this project:

| Decoy / penaid | Discriminator that beats it | Decoy response |
|---|---|---|
| Chaff | Pulse-Doppler (velocity collapse) | Larger clouds, timing, combine with jamming |
| Early IR flare | Imaging IR + kinematics | Multi-spectral, kinematic, aircraft-shaped flares |
| Inflatable vehicle | SAR scattering / polarimetry | Corner reflectors, tuned skins, thermal zones |
| Static ground decoy | Pattern-of-life over time | Mobility, servicing, emission rhythm (active decoys) |
| Midcourse balloon decoy | Multi-phenomenology, space sensors, LRDR | Anti-simulation, replica RVs, IR masking |
| EO-credible decoy | Multi-INT fusion | Add EM/behavioral/narrative layers (story-level) |
| Honeypot | Fingerprinting / environment checks | Decoy hardening, realistic activity |
| Any target vs ATR | AI classifier | Adversarial-example decoys (and robust ATR back) |

A note on the AI layer: automated target recognition discriminates decoys at machine speed, but ATR is itself attackable — scatterer-based and physical adversarial perturbations can flip a SAR/EO classifier, and defenses (adversarial training, Bayesian/uncertainty-aware models) trade accuracy, latency, and cost. The decoy can now *be* an adversarial example, so discrimination robustness is its own research front.

- [On the adversarial robustness of aerial detection](https://www.frontiersin.org/journals/computer-science/articles/10.3389/fcomp.2024.1349206/full) - survey of attacks and defenses against aerial/SAR ATR.
- [Detecting Russian Inflatable Decoys with SAR](https://syntheticapertureradar.com/detecting-russian-inflatable-decoys-with-sar/) - the SAR-scattering discriminator in practice.

## Aircraft and Airbase Decoys

- [Sea Wolf Global F-35 Jet Fighter Decoy System](https://www.seawolfglobal.com/dni/product_f35.html) - Aircraft-shaped decoy with public performance categories.
- [Interesting Engineering: Inflatable F-35 Decoy Deploys in 10 Minutes](https://interestingengineering.com/military/inflatable-f35-military-decoy) - Media summary of a rapidly deployable F-35 decoy.
- [Defense Redefined: Seawolf Marine F-35 Decoy](https://defenceredefined.com.cy/seawolf-marine-inflatable-dummy-decoy-of-the-f-35-stealth-fighter/) - Defense media coverage of the F-35 inflatable dummy.
- [Sandboxx: Korean Company's Inflatable F-35 Decoy](https://www.sandboxx.us/news/viral-video-shows-korean-companys-lifelike-inflatable-f-35-decoy/) - Media report with cost and feature context.
- [Sea Wolf Global Catalog PDF](https://seawolf.co.kr/catalog/ADEXca_en.pdf) - Product catalog for broader inflatable weapon-system decoy concepts.

## Armored Vehicle and Artillery Decoys

- [Forbes: Advanced Decoy Tanks](https://www.forbes.com/sites/vikrammittal/2025/03/03/russia-and-ukraine-are-deploying-increasingly-advanced-decoy-tanks/) - Core modern case study for decoy tanks in Ukraine.
- [Temerland Leopard Tank Decoy](https://temerland.com/en/temerland-is-making-an-unmanned-model-of-a-leopard-tank-based-on-a-regular-car-to-fool-russians/) - Active/mobile tank decoy concept.
- [Euromaidan Press: Ukraine's Decoy Tanks](https://euromaidanpress.com/2025/03/04/forbes-ukraines-decoy-tanks-trick-russian-forces-next-active-dummies-will-spy-on-them/) - Secondary coverage of Forbes reporting, with Ukrainian context.
- [INFLATECH Product Overview](https://www.inflatechdecoy.com/) - Includes broad categories such as tanks, launchers, radars, trucks, aircraft, and other equipment.
- [AP: Inflatable Tanks and Missiles](https://apnews.com/article/a9c478adb9d7ecaa615cb19b25f4833f) - Reporting on inflatable tanks, aircraft, howitzers, and HIMARS-type decoys.

## Industry and Vendors

> Inclusion here is not endorsement. These are useful public references for market mapping and capability taxonomy.

A cross-domain, structured vendor map is in [`data/vendors.csv`](data/vendors.csv), with notes and caveats in [`docs/vendors.md`](docs/vendors.md) — spanning inflatable/physical makers, active/autonomous, signal/EW primes (Raytheon, BAE, L3Harris), camouflage/signature (Saab Barracuda, HDT), and cyber-deception vendors. Note: published inflatable-decoy market-size figures are contradictory and one syndicated report conflates military with hunting decoys, so no single figure is treated as authoritative.

- [Sea Wolf Global](https://seawolf502.cafe24.com/shop3/) - South Korean inflatable decoy systems, including aircraft and rocket-artillery concepts.
- [Sea Wolf F-35 Decoy](https://www.seawolfglobal.com/dni/product_f35.html) - Public F-35 decoy page.
- [INFLATECH](https://www.inflatechdecoy.com/) - Czech high-end inflatable military decoy producer.
- [i2k Defense](https://i2kdefense.com/inflatable-decoys-and-targets/) - U.S. inflatable decoys and training targets.
- [i2k Co Defense](https://i2kco.com/defense/) - U.S.-made inflatable military decoy targets.
- [NorseStorm Inflatable Decoys](https://www.norsestorm.com/product-categories/inflatable-decoys) - Distributor/reference page for INFLATECH products.
- [JISR Institute Inflatable Military Decoys](https://jisr-institute.org/solutions/inflatable-military-decoys) - High-level service page on inflatable military decoys.
- [Strategic Market Research: Inflatable Decoy Market](https://www.strategicmarketresearch.com/market-report/inflatable-decoy-market) - Market-sizing source; verify figures before citing in formal work.

## Autonomous Decoy Aircraft System

This project treats an Autonomous Decoy Aircraft System (ADAS) as a specialized branch of active decoys for airbase survivability and distributed aviation operations. The full deep-dive — operational problem, multi-spectral credibility stack, autonomy levels, cost-exchange model, counter-decoy resilience, evaluation plan, and risks — is in [`docs/adas.md`](docs/adas.md).

### Operational Role

- Create plausible false aircraft presence at main bases, dispersal sites, highway strips, and temporary operating locations.
- Force an adversary to spend ISR time distinguishing real aircraft, decoys, support equipment, and empty revetments.
- Absorb or divert expensive precision weapons away from real aircraft, fuel, munitions, C2, and maintenance assets.
- Support Agile Combat Employment by increasing ambiguity across many small operating locations.

### Minimum Credibility Stack

| Layer | Minimum Useful Feature | Higher-End Feature |
|---|---|---|
| Optical | Aircraft outline, scale, paint pattern, shadows, support clutter | Configurable type variants, maintenance posture, realistic surface detail |
| Thermal | Engine-area heat, sun/ambient thermal contrast | Multi-zone heating, cooling schedule, thermal behavior over time |
| Radar | Radar reflector or RCS augmentation | Tunable reflectors or dynamic RCS shaping |
| Electromagnetic | Optional beacon or simple RF signature | Simulated ground support, data-link, radar, or maintenance emissions |
| Behavior | Static parking and periodic repositioning | Remote/autonomous taxi-like movement, light discipline, patrol and servicing routines |
| System | Manual placement | Fleet-level scheduling, deception planning, sensor feedback, BDA collection |

### Research Questions for ADAS

- What minimum optical/thermal/radar signature is enough to trigger adversary classification as a valid aircraft target?
- How should false aircraft, real aircraft, shelters, revetments, fuel points, and maintenance vehicles be arranged to create a coherent false airbase story?
- What is the right cost ceiling relative to the aircraft, weapons likely to be drawn, and expected number of deployments?
- How much autonomy is actually useful: autonomous navigation, autonomous signature control, autonomous decoy scheduling, or only remote operation?
- What indicators would expose the deception: lack of ground crew pattern, inconsistent shadows, repeated thermal templates, no tire marks, or implausible EM emissions?

## Technology Keywords

### Optical and Physical

- Inflatable decoy
- Physical mockup
- Collapsible structure
- Foldable frame
- Camouflage net
- Signature management
- Visual deception
- False target array

### Infrared and Thermal

- Thermal signature
- Infrared decoy
- Distributed heating
- Thermal contrast
- Heat pattern simulation
- Engine plume simulation
- Multi-zone thermal control

### Radar and Electromagnetic

- Radar cross section
- RCS augmentation
- Corner reflector
- Luneberg lens
- Electromagnetic decoy
- RF signature
- DRFM
- Spectrum deception

### Autonomy and Behavior

- Active decoy
- Autonomous decoy
- Attritable autonomous system
- Remote-controlled decoy
- Swarm deception
- Behavior simulation
- Deception effects assessment
- Closed-loop deception

### Operational Concepts

- Military deception
- Deception operations
- Decoy positions
- Sensor-to-shooter disruption
- Kill chain disruption
- Cost imposition
- Targeting-cycle disruption
- Battle damage assessment uncertainty
- Agile combat employment
- Airbase survivability

## Research Questions

### Concept and Doctrine

- How should modern forces distinguish camouflage, concealment, decoying, spoofing, and deception operations?
- When does a decoy become an active deception system rather than a passive false target?
- How should decoy success be measured: enemy fires absorbed, ISR time consumed, delayed decisions, or misallocated forces?
- How should physical decoys, signal decoys, cyber decoys, and narrative deception be described under one shared vocabulary?
- Which cases are best treated as "dummy targets" and which are better treated as broader deception operations?

### Technology

- What level of multi-spectral fidelity is sufficient against current ISR systems?
- Which signatures are most important by target class: aircraft, armor, artillery, radar, C2 node, logistics site?
- How can optical, infrared, radar, and electromagnetic signatures remain mutually consistent?
- What are the tradeoffs between low-cost mass and high-fidelity active simulation?
- Which parts of the lifecycle matter most for each decoy class: design, production, deployment, operation, or evaluation?
- How can cyber deception concepts such as honeypots, honeytokens, and deception networks inform physical decoy design?

### Operations

- How should decoys be synchronized with real force movement, emissions control, fires, and logistics?
- What deployment ratio between real targets and decoys creates useful ambiguity?
- How can decoys support distributed air operations and airbase survivability?
- How can commanders avoid creating an implausible false story?

### Counter-Decoy

- How do SAR, thermal imaging, AI vision, and pattern-of-life analysis expose false targets?
- What mistakes make decoys easy to classify?
- How will AI-assisted ISR change the minimum credibility threshold for decoys?
- What countermeasures expose cyber decoys: fingerprinting, timing artifacts, interaction depth, or inconsistent telemetry?
- How should a decoy database record source uncertainty, combat-effect uncertainty, and claim provenance?

## Additional Source Index

The expanded source index is maintained in [`references/sources.md`](references/sources.md). It groups sources by:

- Doctrine and concepts.
- Historical deception cases.
- Modern conflict cases.
- Airbase survivability and ACE.
- Electromagnetic deception.
- Industry and vendor references.
- Counter-decoy and detection.

When adding a new source, prefer a direct official or primary page first, then add media reporting only when it contributes observations, imagery, dates, or named claims not present in primary material.

A structured, queryable version of the source index — every key classified by `source_type` (journal, conference, book, think-tank, government/military, professional journal, trade media, news, vendor, analysis blog, OSINT/social, dataset, institutional reference) and by `quality_tier` — is maintained in [`data/sources.csv`](data/sources.csv) and documented in [`docs/source-schema.md`](docs/source-schema.md). Source type is orthogonal to quality tier: a vendor page is Tier A for product existence but Tier D for combat effect.

## Local Seed Documents

These local files are the initial knowledge base for the project:

- `自主式假飞机系统立项论证.docx` - Main argument for an autonomous decoy aircraft system.
- `自主式假飞机系统演示文稿.docx` - Presentation version of the project argument.
- `diu.mil-复制器计划 --- The Replicator Initiative.pdf` - Replicator Initiative background.
- `energy-reporters.com-Sea Wolfs Inflatable F-35 Decoy.pdf` - Media article on Sea Wolf F-35 decoy.
- `interestingengineering.com-充气式 F-35 诱饵在 10 分钟内部署以迷惑导弹.pdf` - Media article on rapidly deployable F-35 decoy.
- `forbes.com-俄罗斯和乌克兰正在部署越来越先进的诱饵坦克.pdf` - Russia-Ukraine decoy tank case.
- `temerland.com-Temerland正基于普通汽车制造无人版豹式坦克以欺骗俄罗斯人.pdf` - Temerland active tank decoy case.

Extracted text is available in:

- `C:\Users\chf_c\Documents\Codex\2026-06-17\new-chat\work\extracted_docs`

## To-Do

- [x] Build a structured case database: country, organization, platform, target type, mobility, spectral features, source quality.
- [x] Define the top-level taxonomy across time, feature, physical evolution, lifecycle, and additional dimensions.
- [x] Add historical cases: Operation Fortitude, Desert Storm deception, Kosovo air defense decoys, Gulf War Scud decoys.
- [x] Add recent-conflict cases the project emphasizes: Nagorno-Karabakh 2020 (SEAD by decoy), Russia-Ukraine HIMARS/aerial decoys, Iran-Israel saturation and penaids (2024-2025), Houthi Red Sea cost-exchange, and offensive decoy reporting.
- [x] Add the signal/expendable decoy hardware backbone: chaff & flares, ADM-141 TALD/ITALD, ADM-160 MALD/MALD-J, AN/ALE-50 & ALE-55 towed decoys, Nulka, AN/SLQ-25 Nixie, ICBM penaids, and the Bekaa Valley (Mole Cricket 19) SEAD anchor.
- [x] Add the source-type / provenance dimension and a structured source index (`data/sources.csv`, `docs/source-schema.md`).
- [x] Add airbase survivability resources: Agile Combat Employment, dispersed operations, hardening vs. deception.
- [x] Add source-quality tiers and a dedicated source index.
- [x] Add pre-modern and World-War deception cases: ancient ruses, WWI Q-ships, WWII Starfish/dummy airfields, the Ghost Army, Operation Mincemeat (with dazzle as adjacency).
- [x] Add cyber deception branch (`docs/cyber-decoys.md`): honeypots, honeytokens/canarytokens, deception platforms, AD/identity decoys, ICS honeypots, MITRE Engage/D3FEND, and honeypot fingerprinting.
- [x] Add the counter-decoy / discrimination branch (`docs/counter-decoy.md`): multi-spectral consistency, SAR/polarimetry, IR & Doppler discrimination, midcourse discrimination, pattern-of-life, AI/ATR adversarial robustness, multi-INT fusion.
- [x] Add a cross-domain vendor/market map (`data/vendors.csv`, `docs/vendors.md`): inflatable, active, signal/EW, naval, camouflage, and cyber-deception vendors, with market-figure caveats.
- [x] Build an interactive, offline case explorer (`assets/cases-explorer.html`) faceted by feature, domain, generation, era, and source tier, with a live clickable counts overview.
- [x] Create a static taxonomy evolution figure (`assets/taxonomy-evolution.svg`): classic -> mechanical -> informationized -> intelligent, with representative cases colour-coded by feature.
- [x] Create a dedicated Autonomous Decoy Aircraft System (ADAS) deep-dive chapter (`docs/adas.md`).
- [ ] Convert the list into a GitHub-style repository structure with `README.md`, `data/`, `papers/`, `vendors/`, and `cases/`.

## Suggested Repository Structure

```text
awesome-decoys/
  README.md
  data/
    cases.csv
    sources.csv
    vendors.csv
    glossary.csv
  docs/
    taxonomy.md
    case-schema.md
    source-schema.md
    adas.md
    vendors.md
    airbase-survivability.md
    cyber-decoys.md
    counter-decoy.md
  references/
    doctrine.md
    modern-conflicts.md
    industry.md
  assets/
    cases-explorer.html
    taxonomy-evolution.svg
    taxonomy.drawio
    roadmap.png
```

## License

Suggested license for a public curated list: CC BY 4.0 or CC0 for the list metadata. Verify source licenses before redistributing copied content or images.
