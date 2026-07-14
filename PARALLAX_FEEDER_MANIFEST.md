# PARALLAX Feeder Manifest

This repository feeds the PARALLAX authority repo:

```text
ItsNotAILABS/PARALLAX-Exchange-Clearinghouse
```

## Lane

```text
phantom_simulation_and_sdk
```

## What this repo may feed

- Monte Carlo simulation primitives,
- Phantom Agent SDK contracts,
- paper backtest receipt schemas,
- compute-worker requirements,
- simulation benchmark summaries,
- research mint artifact requirements.

## What this repo must not feed

- unsupported performance claims,
- live trading automation,
- unvalidated optimization claims,
- custody or broker credential material,
- live execution instructions,
- mainnet financial claims.

## PARALLAX target surfaces

- Compute-Bound Strategy Runner,
- Research Mint,
- Proof Room,
- AI Execution,
- Native Interface.

## Promotion rule

A simulation, SDK, benchmark, or compute-worker artifact from this repo becomes PARALLAX authority only after:

1. source commit or artifact hash is recorded,
2. benchmark conditions are declared,
3. claim/evidence boundary is assigned,
4. proof or receipt expectation is mapped,
5. explicit integration PR is opened in `PARALLAX-Exchange-Clearinghouse`.

## Current boundary

This feeder may support paper backtests and compute-bound strategy demos, but it must not claim validated live trading advantage without external evidence and receipts.
