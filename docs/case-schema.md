# Case Database Schema

`data/cases.csv` is the seed case database. This schema defines the intended fields as the project grows from a small resource list into a full dummy/decoy encyclopedia.

## Current Core Fields

| Field | Meaning | Example |
|---|---|---|
| `case_id` | Stable identifier | `HIST-1944-FORTITUDE` |
| `name_zh` | Chinese case name | `坚忍行动南方` |
| `name_en` | English case name | `Operation Fortitude South` |
| `period` | Year, era, or conflict period | `1944` |
| `actor` | Country, force, organization, vendor, or initiative | `Allied forces / FUSAG` |
| `conflict_context` | War, campaign, exercise, market, or concept context | `Second World War / Normandy landings` |
| `target_or_platform` | What the decoy imitates or protects | `Tanks, aircraft, landing craft` |
| `decoy_form` | Physical, signal, behavioral, cyber, narrative, autonomous, or mixed | `Physical decoys plus radio deception` |
| `mobility` | Static, relocatable, mobile, remote-controlled, autonomous | `Static / relocatable` |
| `spectral_features` | EO, IR, SAR/radar, RF, acoustic, cyber, behavioral, multi-spectral | `Optical, radio traffic` |
| `deception_effect` | Intended or observed effect | `Misled adversary about invasion location` |
| `source_quality` | A/B/C/D source tier | `A` |
| `source_refs` | Source keys from `references/sources.md` | `IWM-FORTITUDE; AUP-FORTRESS-EUROPE` |
| `notes` | Short caveats and research notes | `Canonical example of story-level deception` |

## Recommended Future Fields

Add these fields when the database becomes large enough to need filtering and analysis:

| Field | Meaning | Example Values |
|---|---|---|
| `time_dimension` | Historical phase | `ancient`, `industrial`, `world_wars`, `cold_war`, `contemporary`, `emerging` |
| `domain` | Operational domain | `land`, `air`, `sea`, `space`, `ems`, `cyber`, `information`, `cross_domain` |
| `feature_dimension` | Main feature class | `physical`, `signal`, `behavioral`, `cyber`, `narrative`, `mixed` |
| `physical_evolution` | Technology generation | `classic`, `mechanical`, `informationized`, `intelligent` |
| `lifecycle_stage` | Lifecycle focus | `design`, `manufacturing`, `deployment`, `operation`, `testing`, `combat_use` |
| `target_class` | Target class | `armor`, `aircraft`, `ship`, `missile`, `radar`, `c2`, `logistics`, `identity`, `service`, `dataset` |
| `observer_victim` | Who or what is deceived | `human`, `uav_operator`, `satellite_analyst`, `radar`, `missile_seeker`, `ai_classifier`, `cyber_intruder`, `commander` |
| `effect_mechanism` | Main effect | `attract_fire`, `consume_isr`, `delay_decision`, `mask_movement`, `corrupt_bda`, `collect_tradecraft` |
| `fidelity_level` | Signature/story depth | `visual_only`, `single_signature`, `multi_spectral`, `behavioral`, `networked`, `story_level` |
| `maturity_level` | Evidence and deployment maturity | `concept`, `prototype`, `training_aid`, `commercial_product`, `fielded`, `combat_observed`, `validated_effect` |
| `cost_scalability` | Cost and production character | `one_off`, `unit_built`, `commercial_batch`, `mass_producible`, `attritable`, `software_replicable` |
| `counter_decoy_methods` | How it may be detected | `thermal_anomaly`, `sar_scattering`, `rf_fingerprint`, `pattern_of_life`, `cyber_fingerprint` |
| `evidence_strength` | Strength of effectiveness claim | `claimed`, `reported`, `corroborated`, `measured`, `classified_unknown` |
| `source_dates` | Publication or access dates | `2025-03-03` |

## Source Quality Guidance

Use source-quality labels cautiously:

- A vendor page can be Tier A for product existence and claimed specifications, but not for combat effectiveness.
- A media report can be Tier B for named observations, imagery, and dates, but not for validated kill-chain effects.
- A historical official study can be Tier A for doctrine and campaign narrative, while still requiring caveats for disputed battle damage numbers.
- Social media and image-only claims should be Tier D until geolocation, date, platform, and context are independently checked.

## Normalization Rules

- Keep `case_id` stable once published.
- Prefer one case per operationally meaningful event, system, or concept.
- Use semicolons inside multi-value cells so CSV import remains simple.
- Distinguish product claims from operational effectiveness.
- Record uncertainty explicitly in `notes`.
- Keep links in `references/sources.md`; use source keys in the CSV.
