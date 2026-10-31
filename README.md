# Hamed Yousefi

Platform engineer at
<img src="https://github.com/Polymarket.png?size=32" width="16" height="16" alt="">
[Polymarket](https://polymarket.com), based in Dubai. I write Go, mostly distributed
systems, blockchain infrastructure and LLM inference infrastructure.

Most of my day-to-day work is in private repositories, so my contribution graph shows
more than the public activity below.

## Now

- **[gograph](https://github.com/hmdsefi/gograph)**: <!-- gograph:start -->[v0.9.1](https://github.com/hmdsefi/gograph/releases/tag/v0.9.1) shipped on October 26. Next is [v0.10.0](https://github.com/hmdsefi/gograph/milestone/2), due November 17: Foundations and performance.<!-- gograph:end -->
  Contributions are welcome, and
  [CONTRIBUTING.md](https://github.com/hmdsefi/gograph/blob/master/CONTRIBUTING.md) explains
  where to start.
- **[lockstep](https://github.com/hmdsefi/lockstep)**: actor framework for Go with
  deterministic simulation testing built in. You write typed actors with mailboxes,
  supervision and timers, and the same code runs in `go test` on a seeded simulation that
  partitions the network, drops messages and crashes nodes, then replays any failure exactly
  from its seed. <!-- lockstep:start -->[v0.1.0](https://github.com/hmdsefi/lockstep/releases/tag/v0.1.0) shipped on October 25. Next is [v0.2.0 (Phase 2)](https://github.com/hmdsefi/lockstep/milestone/3): Production runtime.<!-- lockstep:end -->
- **[faultline](https://github.com/hmdsefi/faultline)**: deterministic simulation testing for
  Go. It runs a distributed system on a simulated network, disk and clock inside `go test`,
  injects faults like partitions, crashes and failed fsyncs, and replays any failing run
  exactly from its seed. <!-- faultline:start -->[v0.1.2](https://github.com/hmdsefi/faultline/releases/tag/v0.1.2) shipped on October 19. Next is [Phase 2: Existing-code shims](https://github.com/hmdsefi/faultline/milestone/2).<!-- faultline:end -->
- **Upstream fixes** in Go infrastructure projects, mostly race conditions, error handling
  and tests that had been switched off. The latest are listed below.

## Recent upstream contributions

<!-- recent-prs:start -->
- <img src="https://github.com/temporalio.png?size=32" width="16" height="16" alt=""> **temporalio/temporal**
  - Honor per-namespace businessIDReuseRate overrides ([#12761](https://github.com/temporalio/temporal/pull/12761))
- <img src="https://github.com/llm-d.png?size=32" width="16" height="16" alt=""> **llm-d/llm-d-router**
  - fix(sidecar): send a failed decode chunk as an SSE error event ([#3555](https://github.com/llm-d/llm-d-router/pull/3555))
  - fix(sidecar): send finish\_reason only on the last streamed decode chunk ([#3553](https://github.com/llm-d/llm-d-router/pull/3553))
  - fix(epp): rank no-hit-lru candidates relative to each other ([#3384](https://github.com/llm-d/llm-d-router/pull/3384))
- <img src="https://github.com/filecoin-project.png?size=32" width="16" height="16" alt=""> **filecoin-project/lotus**
  - fix(miner): redo precommit when a CommitFailed sector has no CommR or CommD ([#13843](https://github.com/filecoin-project/lotus/pull/13843))
  - fix(sealing): don't require free space to move files already in storage ([#13949](https://github.com/filecoin-project/lotus/pull/13949))
- <img src="https://github.com/k8sgpt-ai.png?size=32" width="16" height="16" alt=""> **k8sgpt-ai/k8sgpt**
  - fix: keep the core analyzers when adding or removing filters over MCP ([#1857](https://github.com/k8sgpt-ai/k8sgpt/pull/1857))
  - fix: honor namespace, label and resource filters in the OLM analyzers ([#1859](https://github.com/k8sgpt-ai/k8sgpt/pull/1859))
  - fix: report the current failure reason for OLM CSVs and Subscriptions ([#1855](https://github.com/k8sgpt-ai/k8sgpt/pull/1855))
- <img src="https://github.com/vllm-project.png?size=32" width="16" height="16" alt=""> **vllm-project/aibrix**
  - \[Bug\] Keep all of a KV cache pod's slot ranges when it owns the first and last slot ([#3240](https://github.com/vllm-project/aibrix/pull/3240))

Plus [21 more in review](https://github.com/search?q=is%3Apr+is%3Aopen+is%3Apublic+author%3Ahmdsefi+-user%3Ahmdsefi+-repo%3AGreedyC%2Fgograph+-repo%3Aabhijeetnardele24-hash%2Fgograph&type=pullrequests).

[All my merged pull requests to other projects](https://github.com/search?q=is%3Apr+is%3Amerged+is%3Apublic+author%3Ahmdsefi+-user%3Ahmdsefi+-repo%3AGreedyC%2Fgograph+-repo%3Aabhijeetnardele24-hash%2Fgograph&type=pullrequests)
<!-- recent-prs:end -->

## Projects

- [gograph](https://github.com/hmdsefi/gograph): generic graph library for Go. Dependency
  graphs with cycle checks and topological order, traversal, shortest paths, connectivity
  and partitioning, with no dependencies.
- [lockstep](https://github.com/hmdsefi/lockstep): actor framework for Go with typed actors,
  supervision and mailboxes, and a seeded simulation in `go test` that replays any failure
  exactly from its seed.
- [faultline](https://github.com/hmdsefi/faultline): deterministic simulation testing for Go,
  with a simulated network, disk and clock and failures you can replay from a seed. Built for
  AI coding agents and people.
- [gowl](https://github.com/hmdsefi/gowl): worker pool for Go that also monitors the
  status of each process.
- [channelize](https://github.com/hmdsefi/channelize): WebSocket framework for outbound
  streams, with several public and private channels on one connection.
- [staking](https://github.com/hmdsefi/staking): Ethereum staking backend on Lido, with
  Temporal workflows for staking, unstaking, rewards accounting and reconciliation.
- [athenz-agent](https://github.com/hmdsefi/athenz-agent): sidecar that wraps Athenz ZPE
  and ZPU, so services can use Athenz without extra code.
- [vault-eth-signer](https://github.com/Brahma-fi/vault-eth-signer) (contributor):
  HashiCorp Vault plugin that signs with secp256k1 keys, so Vault works as a software  HSM
  for Ethereum.

## Sponsoring

If gograph or my other projects save you time, you can support my open source work
through GitHub Sponsors.

[![Sponsor my work](https://img.shields.io/badge/Sponsor_my_work-ea4aaa?style=for-the-badge&logo=githubsponsors&logoColor=white)](https://github.com/sponsors/hmdsefi)

## Contact

[LinkedIn](https://www.linkedin.com/in/hamed-yousefi-411251b5/)
