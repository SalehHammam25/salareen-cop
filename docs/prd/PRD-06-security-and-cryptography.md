# PRD-06: Security and Cryptography

**Status:** Future stage; requirements extraction not started
**Repository:** `salareen-cop`
**Implementation:** Not started

Stage 6 secures the proven Stage 5 peer protocol without changing Stages 1-5.
The mandatory path uses canonical UTF-8 JSON, SHA-256 commitments, and Ed25519
from Python `cryptography`. It requires signed byte-identical configuration and
Step-0 declarations, fresh secret nonces, commit-acknowledge-reveal, verified
capture claims, hash-chained append-only logs, and final nonce audit. Any byte,
signature, claim, ordering, or audit mismatch fails closed as a technical loss.
Private keys, credentials, endpoints, domains, and pre-audit nonces are excluded
from repository artifacts and logs.

Acceptance requires symmetric cross-repository vectors, one-byte config refusal,
signature/tamper rejection, phase enforcement, and full-suite compatibility.
