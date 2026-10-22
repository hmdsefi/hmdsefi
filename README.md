# Hamed Yousefi

Platform engineer at
<img src="https://github.com/Polymarket.png?size=32" width="16" height="16" alt="">
[Polymarket](https://polymarket.com), based in Dubai. I write Go, mostly distributed
systems, blockchain infrastructure and LLM inference infrastructure.

Most of my day-to-day work is in private repositories, so my contribution graph shows
more than the public activity below.

## Now

- **[faultline](https://github.com/hmdsefi/faultline)**: deterministic simulation testing for
  Go. It runs a distributed system on a simulated network, disk and clock inside `go test`,
  injects faults like partitions, crashes and failed fsyncs, and replays any failing run
  exactly from its seed. <!-- faultline:start -->[v0.1.2](https://github.com/hmdsefi/faultline/releases/tag/v0.1.2) shipped on October 19. Next is [Phase 2: Existing-code shims](https://github.com/hmdsefi/faultline/milestone/2).<!-- faultline:end -->
- **[gograph](https://github.com/hmdsefi/gograph)**: <!-- gograph:start -->[v0.9.0](https://github.com/hmdsefi/gograph/releases/tag/v0.9.0) shipped on October 16. Next is [v0.10.0](https://github.com/hmdsefi/gograph/milestone/2), due November 17: Foundations and performance.<!-- gograph:end -->
  Contributions are welcome, and
  [CONTRIBUTING.md](https://github.com/hmdsefi/gograph/blob/master/CONTRIBUTING.md) explains
  where to start.
- **Upstream fixes** in Go infrastructure projects, mostly race conditions, error handling
  and tests that had been switched off. The latest are listed below.

## Recent upstream contributions

<!-- recent-prs:start -->
- <img src="https://github.com/vllm-project.png?size=32" width="16" height="16" alt=""> **vllm-project/aibrix**
  - \[Bug\] Republish a KV cache pod's address when it changes under the same name ([#3242](https://github.com/vllm-project/aibrix/pull/3242))
- <img src="https://github.com/filecoin-project.png?size=32" width="16" height="16" alt=""> **filecoin-project/lotus**
  - fix(sealing): don't let a cancelled task block scheduling of other tasks ([#13869](https://github.com/filecoin-project/lotus/pull/13869))
  - fix(paths): skip unknown files when scanning storage paths ([#13950](https://github.com/filecoin-project/lotus/pull/13950))
- <img src="https://github.com/mark3labs.png?size=32" width="16" height="16" alt=""> **mark3labs/mcp-go**
  - fix(server): unlock when Start fails with a conflicting address ([#1083](https://github.com/mark3labs/mcp-go/pull/1083))
- <img src="https://github.com/k8sgpt-ai.png?size=32" width="16" height="16" alt=""> **k8sgpt-ai/k8sgpt**
  - fix: keep the known parent when the top owner has an unsupported kind ([#1833](https://github.com/k8sgpt-ai/k8sgpt/pull/1833))
  - fix: do not report an unsupported KEDA scaleTargetRef as missing ([#1831](https://github.com/k8sgpt-ai/k8sgpt/pull/1831))
  - fix: honor the namespace filter in the Gateway API analyzers ([#1826](https://github.com/k8sgpt-ai/k8sgpt/pull/1826))
  - fix: report failed results in Kyverno ClusterPolicyReports ([#1832](https://github.com/k8sgpt-ai/k8sgpt/pull/1832))
  - fix: accept an empty storageClassName in StatefulSet claim templates ([#1830](https://github.com/k8sgpt-ai/k8sgpt/pull/1830))
  - fix: keep webhook findings when configurations share a webhook name ([#1827](https://github.com/k8sgpt-ai/k8sgpt/pull/1827))

Plus [27 more in review](https://github.com/search?q=is%3Apr+is%3Aopen+is%3Apublic+author%3Ahmdsefi+-user%3Ahmdsefi+-repo%3AGreedyC%2Fgograph+-repo%3Aabhijeetnardele24-hash%2Fgograph&type=pullrequests).

[All my merged pull requests to other projects](https://github.com/search?q=is%3Apr+is%3Amerged+is%3Apublic+author%3Ahmdsefi+-user%3Ahmdsefi+-repo%3AGreedyC%2Fgograph+-repo%3Aabhijeetnardele24-hash%2Fgograph&type=pullrequests)
<!-- recent-prs:end -->

## Projects

- [faultline](https://github.com/hmdsefi/faultline): deterministic simulation testing for Go,
  with a simulated network, disk and clock and failures you can replay from a seed. Built for
  AI coding agents and people.
- [gograph](https://github.com/hmdsefi/gograph): generic graph library for Go. Dependency
  graphs with cycle checks and topological order, traversal, shortest paths, connectivity
  and partitioning, with no dependencies.
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
