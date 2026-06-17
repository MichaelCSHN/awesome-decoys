# Counter-Decoy and Discrimination / 反诱饵与鉴别

Every branch of this project ends at the same place: a decoy works only until the observer learns
to tell it apart from the real thing. This chapter is the capstone — it collects the discrimination
methods that defeat decoys across domains and frames them as one **arms race** between decoy
realism and sensor/algorithm discrimination.

The unifying idea is **consistency**. A real target emits a self-consistent story across many
cues — shape, temperature, radar scattering, motion, emissions, supporting activity, and logistical
plausibility. A decoy is cheap precisely because it fakes *some* of those cues and not others.
Discrimination is the search for the cue the decoy got wrong, or the contradiction between cues.

Indexed in [`data/cases.csv`](../data/cases.csv) under the `CD-` keys; see also the cyber
counter-decoy case `CYBER-ANTI-HONEYPOT` and chapter [`docs/cyber-decoys.md`](cyber-decoys.md).

## 1. The Discrimination Methods

### 1.1 Multi-spectral / cross-cue consistency (the master principle)

No single signature is decisive; fusion of EO + IR + radar + RF + behavior is. A "tank" with no
engine heat, an "aircraft" with no ground crew or data-link emissions, or an inflatable with a
perfect outline but no internal radar structure all fail cross-cue checks. The defender's job is to
demand more cues than the decoy budget can fake consistently. The decoy maker's job is the
inverse — raise multi-spectral fidelity without approaching the cost of the real asset.

### 1.2 Radar: SAR scattering and polarimetry

Inflatable and skin-only decoys scatter radar very differently from a metal vehicle with internal
structure, tracks, and edges. SAR and polarimetric analysis exposes the missing returns, wrong
scattering centers, and absent multipath. This is a leading reason modern physical decoys add
corner reflectors, Luneburg lenses, and tuned skins — and why those additions are themselves
detectable when done crudely.

### 1.3 Radar: Doppler and ballistic discrimination

Chaff loses velocity almost immediately after release, so pulse-Doppler radar separates it from a
moving aircraft by its collapsing Doppler shift. In the atmosphere, lightweight decoys decelerate
differently from a heavy reentry vehicle (wrong ballistic coefficient), enabling terminal-phase
discrimination — which is exactly why the **midcourse** case (below) is the hard one.

### 1.4 Infrared: spectral, spatial, and kinematic

Early flares were single hot points; imaging-IR seekers reject them by shape and by kinematics
(a flare decelerates and falls away from the flight path). The countermeasure response —
multi-spectral and kinematic flares, pyrophoric and aircraft-shaped payloads — is a direct example
of the realism/discrimination spiral. Thermal decoys on the ground fail when their heat is uniform,
mistimed, or lacks the engine-to-hull gradient and duty cycle of a running vehicle.

### 1.5 Ballistic missile defense: the midcourse discrimination problem

In the vacuum of exo-atmospheric midcourse flight, a light balloon decoy and a heavy warhead
follow the *same* trajectory, so the ballistic-coefficient trick of the atmosphere is gone. The
defender must discriminate by other phenomenology (radar features, IR signature, micro-motion) and
by sensors such as the Long Range Discrimination Radar and proliferated space sensors. This remains
the canonical "unsolved" discrimination problem and the strongest argument that offense-favorable
decoying scales to the strategic level. Anti-simulation — making the warhead look like one of the
decoys — inverts the burden onto the defense.

### 1.6 Pattern-of-life and temporal validation

Persistent ISR changes the game from a single look to a time series. Static decoys betray
themselves over time: no resupply, no crew movement, no tire tracks appearing, repeated identical
thermal templates, lights and emissions on implausible schedules. The "transparent battlefield"
that makes decoys necessary also makes *lazy* decoys easy — the counter is behavioral realism
(movement, servicing, emission rhythm), which is why active and autonomous decoys exist.

### 1.7 AI / ATR discrimination — and its fragility

Automated target recognition (ATR) promises to discriminate decoys at machine speed across huge
sensor volumes. But ATR is itself attackable: scatterer-based and physical adversarial perturbations
can flip a SAR/EO classifier with small, physically realizable changes (extra scatterers, patches,
paint), and defenses (adversarial training, Bayesian/uncertainty-aware models, model-hardware
co-design) trade accuracy, latency, and cost. So the arms race goes meta: the decoy can now be an
adversarial example, and discrimination robustness becomes a research front in its own right.

### 1.8 Multi-INT fusion and logistics plausibility

A decoy that is credible to one collector often fails when collectors are fused: EO says "aircraft,"
but SIGINT hears no emissions, OSINT shows no transport to the site, and the dispersal pattern makes
no logistical sense. Cross-INT correlation and plausibility checks (Could it get there? Is it
supplied? Does the order of battle fit?) are among the cheapest and most robust discriminators.

### 1.9 Cyber: honeypot fingerprinting

The cyber face of the same principle: attackers fingerprint decoys by default configurations,
service banners, timing artifacts, missing user activity, and VM/sandbox tells, and reconnaissance
tools flag likely honeypots. The defender's counter is decoy hardening — realistic noise, aged data,
production-like fingerprints — the exact analogue of physical multi-spectral realism. See
`CYBER-ANTI-HONEYPOT`.

## 2. The Arms-Race Thread (how the branches connect)

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

The throughline: discrimination demands *more independent, consistent cues*; deception answers with
*more layers of consistent fakery*. Cost, energy, and time decide who is ahead in a given matchup.

## 3. Evaluation (lifecycle: testing/evaluation)

- **Discrimination probability** vs each sensor and vs the fused picture.
- **Cue-consistency audit** — which signatures the decoy reproduces and which it contradicts.
- **Time-to-discriminate** under persistent ISR (the pattern-of-life clock).
- **ATR robustness** — accuracy under adversarial perturbation and distribution shift.
- **Cost-exchange of discrimination** — does discriminating cost the defender more than the decoy cost the attacker?
- **Red-team realism** — independent classification trials, not self-assessment.

## 4. Mapping to the Shared Taxonomy

This chapter is the operational expansion of the taxonomy's **Counter-Decoy Angle** sub-dimension
(see [`docs/taxonomy.md`](taxonomy.md) section 6): optical/IR/SAR/RF anomaly detection,
pattern-of-life validation, AI-classifier robustness, multi-source fusion, cyber fingerprinting,
logistics plausibility, and forensic attribution.
