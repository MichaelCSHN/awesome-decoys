# Autonomous Decoy Aircraft System (ADAS) / 自主式假飞机系统专题

[English](adas.md) | [中文](adas.zh-CN.md)

This chapter develops the project's lead application: an **autonomous decoy aircraft system** for
airbase survivability and distributed aviation operations. It is written to feed a concept/proposal
(立项论证) and pulls together the rest of the library — the signal-decoy hardware lineage
([`docs/counter-decoy.md`](counter-decoy.md) and the `SIG-` cases), the inflatable/active-decoy
market ([`docs/vendors.md`](vendors.md)), and the counter-decoy discrimination methods that set the
credibility bar.

## 1. The Operational Problem

Persistent ISR (low-orbit imaging, SAR, drones, SIGINT, AI-assisted recognition) plus long-range
precision fires compress the find-fix-track-target-engage-assess cycle against fixed, high-value
aviation assets. Aircraft on the ground at main bases, dispersal sites, and highway strips are
exactly the targets that Agile Combat Employment (ACE) tries to protect by spreading out. Decoys
turn dispersion into **ambiguity**: the adversary must now decide which of many parking spots,
revetments, and aircraft-shaped objects across many sites is worth a scarce precision weapon.

This is the airbase instance of the cost-exchange logic seen in Ukraine (decoy HIMARS drawing
Kalibr) and the SEAD-by-decoy logic of Nagorno-Karabakh and Bekaa Valley.

## 2. Role and Effects

- Create plausible false aircraft presence across main bases, dispersal sites, highway strips, and temporary operating locations.
- Force the adversary to spend ISR time discriminating real aircraft, decoys, support equipment, and empty revetments.
- Absorb or divert precision weapons away from real aircraft, fuel, munitions, C2, and maintenance.
- Support ACE by raising ambiguity across many small operating locations simultaneously.
- Optionally, bait and expose the adversary's targeting/ISR (who looked, who shot) — a decoy that also collects.

## 3. The Multi-Spectral Credibility Stack

A decoy is only as good as its **least consistent cue** (see counter-decoy §1). The stack below is
the requirements spine; the right-hand column is what defeats a lazy version of each layer.

| Layer | Minimum useful feature | Higher-end feature | Discriminator that beats a weak version |
|---|---|---|---|
| Optical | Aircraft outline, scale, paint, shadows, support clutter | Type variants, maintenance posture, surface detail | EO anomaly, missing ground clutter |
| Thermal | Engine-area heat, ambient contrast | Multi-zone heating, realistic cool-down cycle | IR uniformity, mistimed/absent heat cycle |
| Radar | Reflector or RCS augmentation | Tunable / dynamic RCS shaping | SAR scattering: no internal structure |
| Electromagnetic | Optional beacon | Simulated ground-support, data-link, radar emissions | SIGINT silence next to a "live" aircraft |
| Behavior | Static parking + periodic repositioning | Taxi-like movement, light discipline, servicing rhythm | Pattern-of-life: no crew, no tracks, repeated templates |
| System | Manual placement | Fleet scheduling, deception planning, sensor feedback, BDA collection | Multi-INT fusion: implausible disposition/logistics |

The design tension is constant: each added layer raises both credibility and **cost/energy/heat/
power**, and the whole point is to stay far below the cost of the real aircraft.

## 4. Autonomy: How Much Is Actually Useful

Autonomy is a means to **behavioral realism and operator economy**, not an end. Useful levels:

- **Remote reposition** — defeat single-look pattern-of-life by moving between revetments.
- **Autonomous signature control** — schedule thermal/EM emissions to mimic a servicing/alert cycle.
- **Autonomous taxi/relocation** — present motion, the cue static decoys cannot fake.
- **Fleet-level deception scheduling** — coordinate many decoys + real aircraft into one coherent false airbase story (the hardest and highest-value layer).

This places ADAS on the "intelligent/autonomous" rung of the physical-evolution axis and connects to
attritable-mass initiatives (e.g., Replicator) for low-cost, software-replicable behavior.

## 5. Cost-Exchange Model

The decoy wins if `(cost of decoy + deploy/sustain) << (cost of the weapon it draws + value of the real asset protected x risk reduction)`.
Key levers: unit cost, number of deployments per unit, weapons likely drawn, and ISR time consumed.
A decoy that survives one look but fails the second is worth little; a decoy that must be re-shot to
confirm is worth a lot. Evaluate against the *adversary's* magazine depth and ISR throughput, not
just against a single engagement.

## 6. Counter-Decoy Resilience (design to be discriminated against)

Design the decoy by red-teaming it with the discriminators in [`docs/counter-decoy.md`](counter-decoy.md):

- Add internal radar structure / tuned reflectors so SAR scattering is plausible.
- Give thermal zones an engine-to-hull gradient and a realistic duty cycle, not a uniform hot blob.
- Pair with at least minimal EM activity so SIGINT does not flag a "silent live aircraft."
- Seed pattern-of-life: occasional movement, support-vehicle clutter, light discipline.
- Make the *array* logistically plausible (spacing, access, dispersal that fits doctrine), because multi-INT fusion attacks the disposition, not just the object.
- Assume AI/ATR discrimination and the adversarial-example arms race: realism must hold against an automated classifier, and the decoy fleet should not all share one detectable template.

## 7. Relationship to the Rest of the Library

- **Lineage**: ADM-20 Quail -> TALD -> MALD shows the air-launched decoy heritage; ADAS is the *ground/airbase* counterpart focused on persistence and array credibility (`SIG-` cases).
- **Market**: inflatable aircraft decoys already exist (Sea Wolf F-35; i2k; Inflatech) — ADAS is the active/autonomous, multi-spectral evolution of that product class (`docs/vendors.md`).
- **Doctrine**: airbase survivability and ACE provide the operational setting (`AIRBASE-ACE` case).
- **Counter-decoy**: §6 above is the discrimination chapter applied as a requirements checklist.

## 8. Evaluation Plan (lifecycle: testing/evaluation)

- Sensor-facing trials: EO, IR, SAR, RF, and (where relevant) acoustic, against the fused picture.
- Red-team classification: can an analyst or an ATR model separate decoys from real aircraft, and at what range/time?
- Time-to-discriminate under persistent ISR (the pattern-of-life clock).
- Cost-exchange and deployment-tempo trials (setup time, operator load, power, weather/wind robustness).
- Closed-loop deception-effect assessment: did it draw fire, consume ISR, or alter adversary maneuver?

## 9. Key Risks

- **Multi-spectral inconsistency** — the single biggest failure mode; one wrong cue unravels the rest.
- **Cost creep** — high fidelity must not approach the cost of the real aircraft.
- **Power, heat, and wind** — active emissions, heating, and autonomy raise power draw; large light structures are fragile in field conditions.
- **Deployment tempo** — must match high-tempo dispersed operations.
- **Adversary learning** — AI/ATR will learn fleet templates; avoid a single detectable signature across the fleet.
