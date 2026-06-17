# Source Index / 资料来源索引

This file maps short source keys used in `data/cases.csv` to public references. The list favors official, institutional, and primary sources, then adds reputable reporting where it contributes case detail, imagery, dates, or product context.

## Two Axes: Source Type and Quality Tier

Every source has two independent attributes:

- **Source type / provenance** (genre): journal, conference paper, book, think-tank report, government/military document, professional military journal, trade defense media, news media, vendor/industry, analysis blog, OSINT/social, dataset, institutional reference, standard/patent. Definitions and Chinese glosses are in [`docs/taxonomy.md`](../docs/taxonomy.md) section 6.
- **Quality tier** (A/B/C/D): evidentiary weight, which is claim-dependent (see rules below).

The structured, queryable classification of every key below — by `source_type` and `quality_tier` — lives in [`data/sources.csv`](../data/sources.csv), documented in [`docs/source-schema.md`](../docs/source-schema.md). The groupings in *this* file are by topic, for reading; use the CSV to slice by source type.

## Source Quality Rules

- **A - Primary official / institutional**: doctrine, official military articles, government reports, RAND or equivalent research reports, vendor pages for their own products.
- **B - Reputable reporting / specialist media**: AP, RFE/RL, Forbes, The War Zone, professional defense media, named expert articles.
- **C - Secondary aggregation**: blogs, market reports, republications, unsourced summaries, or articles derived mainly from other reporting.
- **D - Unverified / social**: social media posts, videos, image-only claims, or claims that need independent confirmation.

## Doctrine and Concepts

- `AUP-DECEPTION-OPERATIONS` - [Deception Operations](https://www.armyupress.army.mil/Portals/7/combat-studies-institute/csi-books/bjorge2.pdf), Army University Press / Combat Studies Institute.
- `AUP-HIDING-PLAIN-SIGHT` - [Hiding in Plain Sight](https://www.armyupress.army.mil/Journals/Military-Review/English-Edition-Archives/March-April-2023/Hiding/), Army University Press.
- `ARMY-MOTHS-FALSE-FLAME` - [Like Moths to a False Flame](https://www.army.mil/article/286861/like_moths_to_a_false_flame_lethality_and_protection_through_deception_operations), U.S. Army.
- `WARROOM-EM-DECOYS` - [A Tool for Deception: The Urgent Need for EM Decoys](https://warroom.armywarcollege.edu/articles/tactical-decoys/), War Room / U.S. Army War College.
- `WOTR-EMS-DECEPTION` - [Thinking Through Deception on the Electromagnetic Spectrum](https://warontherocks.com/thinking-through-deception-on-the-electromagnetic-spectrum/), War on the Rocks.
- `DSIAC-DECOYS-US-MILITARY` - [An Overview of Decoys Used in the U.S. Military](https://dsiac.dtic.mil/wp-content/uploads/2023/09/TI-Response-Report_DSIAC_An-Overview-of-Decoys-Used-in-the-U.S.-Military_1162024.pdf), DSIAC.

## Historical Deception Cases

- `IWM-FORTITUDE` - [D-Day Deception: Parachuting Dummies and Inflatable Tanks](https://www.iwm.org.uk/history/second-world-war/d-day/parachuting-dummies-and-inflatable-tanks), Imperial War Museums.
- `ENGLISH-HERITAGE-FORTITUDE` - [D-Day Deception: Operation Fortitude South](https://www.english-heritage.org.uk/visit/places/dover-castle/history-and-stories/d-day-deception/), English Heritage.
- `AUP-FORTRESS-EUROPE` - [Assault on Fortress Europe](https://www.armyupress.army.mil/Journals/Military-Review/Online-Exclusive/2020-OLE/Carminati-Assault-Fortress-Europe/), Army University Press.
- `AUP-DECEPTION-DESERT` - [Deception in the Desert: Deceiving Iraq in Operation DESERT STORM](https://www.armyupress.army.mil/Books/Browse-Books/iBooks-and-EPUBs/Deception-in-the-Desert/), Army University Press.
- `CGSC-DESERT-STORM-DECEPTION` - [Deception in Operations Desert Shield / Desert Storm](https://cgsc.contentdm.oclc.org/digital/api/collection/p15040coll2/id/3069/download), CGSC digital library.
- `SOFNEWS-SCUD-HUNT` - [Desert Storm - SOF Scud Hunting Mission in Iraq](https://sof.news/history/desert-storm-sof-scud-hunting-mission-in-iraq/), SOF News.
- `NGWRC-SCUD` - [Scud Use in Desert Storm](https://ngwrc.net/2023/05/02/scud-use-in-desert-storm/), National Gulf War Resource Center.
- `JSTOR-SCUD-HUNT` - [Operation Desert Storm Scud Hunt - 1991](https://www.jstor.org/stable/resrep13964.8), JSTOR-hosted report chapter.
- `RAND-KOSOVO` - [NATO's Air War for Kosovo: A Strategic and Operational Assessment](https://www.rand.org/content/dam/rand/pubs/monograph_reports/MR1365/RAND_MR1365.pdf), RAND.
- `NDU-KOSOVO-FIELDED-FORCES` - [Attacking Fielded Forces: An Airman's Perspective from Kosovo](https://ndupress.ndu.edu/Media/News/News-Article-View/Article/2018960/attacking-fielded-forces-an-airmans-perspective-from-kosovo/), NDU Press.
- `AFMC-SERBIAN-IADS` - [Hostile Airspace: Serbian IADS during Allied Force](https://www.afmc.af.mil/News/Article-Display/Article/1843192/hostile-airspace-serbian-iads-during-allied-force/), Air Force Materiel Command.
- `PARAMETERS-KOSOVO-INFO-SUPERIORITY` - [Kosovo and the Current Myth of Information Superiority](https://press.armywarcollege.edu/cgi/viewcontent.cgi?article=1967&context=parameters), Parameters / U.S. Army War College Press.

## Modern Conflict Cases

- `AP-INFLATECH` - [Inflatable Tanks and Missiles: Czech Firm Makes Decoy Armaments](https://apnews.com/article/a9c478adb9d7ecaa615cb19b25f4833f), Associated Press.
- `RFERL-INFLATECH` - [Czech Firm Makes Decoy Armaments](https://www.rferl.org/a/czech-inflatable-weapon-decoys-ukraine/32305583.html), Radio Free Europe / Radio Liberty.
- `FORBES-DECOY-TANKS` - [Russia And Ukraine Are Deploying Increasingly Advanced Decoy Tanks](https://www.forbes.com/sites/vikrammittal/2025/03/03/russia-and-ukraine-are-deploying-increasingly-advanced-decoy-tanks/), Forbes.
- `NV-UA-DECOY-ARMS-RACE` - [Ukraine, Russia in arms race to improve their decoy use](https://english.nv.ua/russian-war/ukraine-russia-in-arms-race-to-improve-their-decoy-use-50494791.html), The New Voice of Ukraine.
- `NEWSWEEK-RUSSIAN-INFLATABLE` - [Ukraine trying to outgun Russia in war of inflatable decoy tanks](https://www.newsweek.com/ukraine-russia-inflatable-decoy-tanks-1829779), Newsweek.
- `1945-RUSSIA-INFLATABLE` - [Russia Deploys World War II Tactic in Ukraine: Inflatable Tanks](https://www.19fortyfive.com/2023/09/russia-deploys-world-war-ii-tactic-in-ukraine-inflatable-tanks/), 19FortyFive.
- `TWZ-US-ARMY-DECOYS` - [Inflatable Decoys Paired With Faked Radio Signals Used To Bait Enemy Artillery](https://www.twz.com/news-features/inflatable-decoys-faked-signals-used-to-bait-enemy-artillery-in-recent-army-exercise), The War Zone.

## Airbase Survivability and ACE

- `USAF-ACE` - [Agile Combat Employment, AFDN 1-21](https://www.doctrine.af.mil/Portals/61/documents/AFDN_1-21/AFDN%201-21%20ACE.pdf), U.S. Air Force doctrine.
- `RAND-AIRBASE-ATTACKS` - [Air Base Attacks and Defensive Counters](https://www.rand.org/pubs/research_reports/RR968.html), RAND.
- `CRS-ACE` - [Defense Primer: Agile Combat Employment Concept](https://www.everycrsreport.com/reports/IF12694.html), Congressional Research Service mirror.
- `AIR-UNIVERSITY-ACE` - [Implementing New Airpower Concepts: Insights from Agile Combat Employment](https://www.airuniversity.af.edu/Portals/10/AUPress/Papers/KP_14_Mulgund_Implementing_New_Airpower_Concepts.1.pdf), Air University Press.
- `USNI-ACE-PROBLEMS` - [Problems for Agile Combat Employment](https://www.usni.org/magazines/proceedings/2024/july/problems-agile-combat-employment), U.S. Naval Institute Proceedings.

## Industry and Vendor References

- `SEAWOLF-F35` - [Sea Wolf Global F-35 Jet Fighter Decoy System](https://www.seawolfglobal.com/dni/product_f35.html), Sea Wolf Global.
- `SEAWOLF-CATALOG` - [Sea Wolf Global Catalog PDF](https://seawolf.co.kr/catalog/ADEXca_en.pdf), Sea Wolf.
- `INTERESTING-ENGINEERING-F35` - [Inflatable F-35 military decoy](https://interestingengineering.com/military/inflatable-f35-military-decoy), Interesting Engineering.
- `DEFENSE-REDEFINED-F35` - [Seawolf Marine inflatable dummy decoy of the F-35 stealth fighter](https://defenceredefined.com.cy/seawolf-marine-inflatable-dummy-decoy-of-the-f-35-stealth-fighter/), Defense Redefined.
- `SANDBOXX-F35` - [Korean company's lifelike inflatable F-35 decoy](https://www.sandboxx.us/news/viral-video-shows-korean-companys-lifelike-inflatable-f-35-decoy/), Sandboxx.
- `INFLATECH-HOME` - [INFLATECH inflatable military decoys](https://www.inflatechdecoy.com/), INFLATECH.
- `INFLATECH-NEWS` - [INFLATECH news](https://www.inflatechdecoy.com/news/), INFLATECH.
- `NORSESTORM-INFLATABLE` - [Inflatable Decoys](https://www.norsestorm.com/product-categories/inflatable-decoys), NorseStorm.
- `I2K-DEFENSE` - [Inflatable Decoys and Targets](https://i2kdefense.com/inflatable-decoys-and-targets/), i2k Defense.
- `TEMERLAND-LEOPARD` - [Temerland is making an unmanned model of a Leopard tank based on a regular car](https://temerland.com/en/temerland-is-making-an-unmanned-model-of-a-leopard-tank-based-on-a-regular-car-to-fool-russians/), Temerland.
- `EUROMAIDAN-TEMERLAND` - [Ukraine's decoy tanks trick Russian forces](https://euromaidanpress.com/2025/03/04/forbes-ukraines-decoy-tanks-trick-russian-forces-next-active-dummies-will-spy-on-them/), Euromaidan Press.

## Autonomy and Attritable Systems

- `DIU-REPLICATOR` - [Implementing the Department of Defense Replicator Initiative](https://www.diu.mil/latest/implementing-the-department-of-defense-replicator-initiative-to-accelerate), Defense Innovation Unit.
- `DIU-REPLICATOR-SOFTWARE` - [DIU announces software vendors to support Replicator](https://www.diu.mil/latest/defense-innovation-unit-announces-software-vendors-to-support-replicator), Defense Innovation Unit.

## Counter-Decoy and Detection

- `SAR-DECOY-DETECTION` - [Detecting Russian Inflatable Decoys with SAR](https://syntheticapertureradar.com/detecting-russian-inflatable-decoys-with-sar/), Synthetic Aperture Radar.
- `RAND-KOSOVO` - [NATO's Air War for Kosovo](https://www.rand.org/content/dam/rand/pubs/monograph_reports/MR1365/RAND_MR1365.pdf), RAND. Useful for BDA and target-validation uncertainty.
- `USNI-ACE-PROBLEMS` - [Problems for Agile Combat Employment](https://www.usni.org/magazines/proceedings/2024/july/problems-agile-combat-employment), U.S. Naval Institute. Useful for AI/space-sensing pressure on dispersion and deception.

## Signal and Expendable Decoy Hardware

These are the canonical signature/expendable decoy systems — the backbone of the "signal" feature dimension and the "informationized" generation. They span air, naval, and strategic domains.

### Expendable RF/IR countermeasures (chaff and flares)

- `GS-FLARES` - [Flares - Infrared Countermeasures](https://www.globalsecurity.org/military/systems/aircraft/systems/flares.htm), GlobalSecurity.org. Tier B. (Also covers chaff and the AN/ALE-47 dispenser.)
- `WIKI-CHAFF` - [Chaff (countermeasure)](https://en.wikipedia.org/wiki/Chaff_(countermeasure)), Wikipedia. Tier C. (WWII "Window" origin; Doppler discrimination.)
- `MM-COUNTERMEASURES` - [How Aircraft Countermeasures Win the Battle Against Incoming Missiles](https://militarymachine.com/missile-countermeasures-chaff-flares-decoys), Military Machine. Tier C. (Multispectral/kinematic flares vs imaging IR; DIRCM.)

### Air-launched decoys (TALD, MALD)

- `FAS-TALD` - [ADM-141 Tactical Air-Launched Decoy (TALD)/ITALD](https://man.fas.org/dod-101/sys/ac/equip/tald.htm), FAS (DoD-101). Tier A.
- `DSN-TALD` - [IMI (Brunswick) ADM-141 TALD](https://www.designation-systems.net/dusrm/m-141.html), Designation-Systems.net. Tier A/B.
- `ASF-MALD` - [ADM-160 MALD](https://www.airandspaceforces.com/weapons/adm-160-mald/), Air & Space Forces Magazine. Tier B.
- `DSN-MALD` - [ADM-160A/B/C MALD](https://www.designation-systems.net/dusrm/m-160.html), Designation-Systems.net. Tier A/B.
- `GS-MALD` - [ADM-160 Miniature Air-Launched Decoy (MALD)](https://www.globalsecurity.org/military/systems/aircraft/systems/mald.htm), GlobalSecurity.org. Tier B/C.

### Towed decoys (air)

- `WIKI-ALE50` - [AN/ALE-50 towed decoy system](https://en.wikipedia.org/wiki/AN/ALE-50_towed_decoy_system), Wikipedia. Tier C. ("Little Buddy"; combat-proven over Kosovo/Iraq.)
- `WIKI-ALE55` - [AN/ALE-55 fiber-optic towed decoy](https://en.wikipedia.org/wiki/AN/ALE-55_fiber-optic_towed_decoy), Wikipedia. Tier C. (IDECM with AN/ALQ-214.)

### Naval and undersea decoys (Nulka, Nixie)

- `NAVY-NULKA-MK53` - [MK 53 Decoy Launching System (Nulka)](https://www.navy.mil/Resources/Fact-Files/Display-FactFiles/Article/2167877/mk-53-decoy-launching-system-nulka/), U.S. Navy Fact File. Tier A.
- `BAE-NULKA` - [Nulka active missile decoy](https://www.baesystems.com/en/product/nulka), BAE Systems. Tier A (product).
- `DST-NULKA` - [Nulka Active Missile Decoy](https://www.dst.defence.gov.au/innovation/nulka-active-missile-decoy), Australian DST Group. Tier A.
- `FAS-NIXIE` - [AN/SLQ-25 Nixie](https://man.fas.org/dod-101/sys/ship/weaps/an-slq-25.htm), FAS (DoD-101). Tier A.
- `WIKI-NIXIE` - [AN/SLQ-25 Nixie](https://en.wikipedia.org/wiki/AN/SLQ-25_Nixie), Wikipedia. Tier C.

### Strategic penetration aids

- `CSIS-PENAIDS` - [Countermeasures, Penetration Aids, and Missile Defense](https://missilethreat.csis.org/countermeasures-penetration-aids-and-missile-defense/), CSIS Missile Threat. Tier A.
- `GS-MIDCOURSE` - [Mid-Course Phase](https://www.globalsecurity.org/space/systems/mid-course.htm), GlobalSecurity.org. Tier B/C. (Discrimination problem; MIT Countermeasures report.)

## Recent Conflict Decoy and Saturation Cases (2020-2026)

### Nagorno-Karabakh 2020 (An-2 bait drones / SEAD by decoy)

- `ARMY-NK2020-LESSONS` - [Lessons from the Nagorno-Karabakh 2020 Conflict](https://api.army.mil/e2/c/downloads/2023/01/31/693ac148/21-655-nagorno-karabakh-2020-conflict-catalog-aug-21-public.pdf), U.S. Army (Combat Studies / lessons catalog). Tier A.
- `RAF-ASPR-NK-DRONES` - [The 2020 Nagorno Karabakh War: Unmanned Combat](https://www.raf.mod.uk/what-we-do/centre-for-air-and-space-power-studies/aspr/aspr-vol25-iss2-3-pdf/), RAF Air and Space Power Review. Tier A.
- `BAS-AN2-CROPDUSTER` - [The next frontier in drone warfare? A Soviet-era crop duster](https://thebulletin.org/2021/02/the-next-frontier-in-drone-warfare-a-soviet-era-crop-duster/), Bulletin of the Atomic Scientists. Tier B.
- `SWJ-NK-LESSONS` - [What the United States Military Can Learn from the Nagorno-Karabakh War](https://smallwarsjournal.com/2021/04/04/what-united-states-military-can-learn-nagorno-karabakh-war/), Small Wars Journal (Arizona State University). Tier B.

### Russia-Ukraine (HIMARS decoys, aerial/airbase decoys)

- `WAPO-UA-HIMARS-DECOY` - [Ukraine lures Russian missiles with decoys of U.S. rocket system](https://www.washingtonpost.com/world/2022/08/30/ukraine-russia-himars-decoy-artillery/), The Washington Post. Tier B.
- `UP-KALIBR-VS-HIMARS` - [Real Kalibr missiles vs HIMARS decoys](https://www.pravda.com.ua/eng/articles/2024/03/11/7445807/), Ukrainska Pravda. Tier B. (Metinvest 250+ mock-ups; Kamyshin on a decoy-deployment "user manual".)
- `EUROMAIDAN-MASTERS-ILLUSION` - [Masters of illusion: Ukraine's decoy makers outwit Russia](https://euromaidanpress.com/2024/03/13/masters-of-illusion-ukraines-decoy-makers-outwit-russia/), Euromaidan Press. Tier C.
- `ARMYRECOG-FORTITUDE` - [Ukraine's mastery of decoy warfare](https://www.armyrecognition.com/focus-analysis-conflicts/army/conflicts-in-the-world/russia-ukraine-war-2022/analysis-ukraine-s-mastery-of-decoy-warfare-named-fortitude), Army Recognition. Tier C.
- `USNI-DECOY-WARFARE-UKRAINE` - [Decoy Warfare: Lessons and Implication from the War in Ukraine](https://www.usni.org/magazines/proceedings/2024/april/decoy-warfare-lessons-and-implication-war-ukraine), U.S. Naval Institute Proceedings. Tier A/B. (Russian inert cruise-missile/drone decoys, inflatable command posts, painted Tu-95 at Engels, decoy balloons.)

### Iran-Israel and US-Israel-Iran (saturation, penetration aids, cost-exchange)

- `FPRI-SHALLOW-RAMPARTS` - [Shallow Ramparts: Air and Missile Defenses in the June 2025 Israel-Iran War](https://www.fpri.org/article/2025/10/shallow-ramparts-air-and-missile-defenses-in-the-june-2025-israel-iran-war/), Foreign Policy Research Institute. Tier A/B. (True Promise I/II composition and impact counts; June 2025 saturation.)
- `TWZ-IRAN-CLUSTER-WARHEAD` - [Iran Is Piercing Israel's Ballistic Missile Defenses With High-Altitude Cluster Warhead Releases](https://www.twz.com/land/iran-is-piercing-israels-ballistic-missile-defenses-with-high-altitude-cluster-warhead-releases), The War Zone. Tier B.
- `DSA-IRAN-SATURATION` - [Israel Admits Missile Shield Limits: Iran's Ballistic Arsenal Could Overwhelm Iron Dome, Arrow and U.S. Gulf Bases](https://defencesecurityasia.com/en/israel-iran-ballistic-missile-threat-5000-missiles-iron-dome-arrow-gulf-bases-2027/), Defence Security Asia. Tier C. (Decoys "to dilute tracking fidelity"; interceptor depletion toward 2027.)
- `SATURATION-LAYERED-BATTLEFIELD` - [Missile Saturation and the Layered Battlefield](https://trevor-barnes.com/p/missile-saturation-and-the-layered), analyst essay. Tier C. (Cost-of-defense framing; April 2024 ~US$1B intercept night.)

### Houthi / Red Sea cost-exchange

- `NEWLINES-HOUTHI-DRONES` - [Cheap Houthi Drones Are Draining the Pentagon's Coffers](https://newlinesmag.com/argument/cheap-houthi-drones-are-draining-the-pentagons-coffers/), New Lines Magazine. Tier B.
- `NATIONAL-CHEAP-DRONES` - [Drones get cheaper and deadlier as armies race for low-cost defences](https://www.thenationalnews.com/news/mena/2025/01/23/drones-get-cheaper-and-deadlier-as-armies-race-for-low-cost-defences/), The National. Tier B.
- `GEOPOL-DRONES-DOLLARS` - [Drones vs. Dollars: The Costly Calculus of U.S.-Houthi Warfare](https://geopoliticsunplugged.substack.com/p/drones-vs-dollars-the-costly-calculus), Geopolitics Unplugged. Tier C. (Operation Rough Rider; mobile launchers and decoy systems complicate targeting.)
- `NBC-HOUTHI-DRONES` - [How Yemen's Houthi rebels have leveraged cheap drones into military success](https://www.nbcnews.com/tech/security/yemens-houthi-rebels-used-cheap-drones-attacks-years-rcna135117), NBC News (quotes CSIS Missile Defense Project). Tier B.

### Reversing the cost equation (US offensive decoys)

- `DEFENSEINFO-EPICFURY-LUCAS` - [From Red Sea Defense to Epic Fury: How the U.S. Flipped the Drone Cost Equation](https://defense.info/featured-story/2026/03/from-red-sea-defense-to-epic-fury-how-the-u-s-flipped-the-drone-cost-equation/), Defense.info. Tier C. Single-outlet, recent; corroborate before formal citation.

## Notes for Future Updates

- Add page numbers for PDF sources after local extraction.
- Add `source_date`, `accessed_date`, and `archive_url` fields if the repository becomes public-facing.
- Avoid copying images or long text from sources unless license terms are clear; link and summarize instead.
