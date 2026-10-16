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
  exactly from its seed. <!-- faultline:start -->[v0.1.0](https://github.com/hmdsefi/faultline/releases/tag/v0.1.0) shipped on October 11. Next is [v0.1.1 (hardening and agent plugin)](https://github.com/hmdsefi/faultline/milestone/3), due October 19.<!-- faultline:end -->
- **[gograph](https://github.com/hmdsefi/gograph)**: <!-- gograph:start -->[v0.8.2](https://github.com/hmdsefi/gograph/releases/tag/v0.8.2) shipped on October 2. Next is [v0.9.0](https://github.com/hmdsefi/gograph/milestone/1), due October 19: Dependency graph toolkit.<!-- gograph:end -->
  Contributions are welcome, and
  [CONTRIBUTING.md](https://github.com/hmdsefi/gograph/blob/master/CONTRIBUTING.md) explains
  where to start.
- **Upstream fixes** in Go infrastructure projects, mostly race conditions, error handling
  and tests that had been switched off. The latest are listed below.

## Recent upstream contributions

<!-- recent-prs:start -->
- <img src="https://github.com/k8sgpt-ai.png?size=32" width="16" height="16" alt=""> **k8sgpt-ai/k8sgpt**
  - fix: honor the namespace filter in the Gateway API analyzers ([#1826](https://github.com/k8sgpt-ai/k8sgpt/pull/1826))
  - fix: report failed results in Kyverno ClusterPolicyReports ([#1832](https://github.com/k8sgpt-ai/k8sgpt/pull/1832))
  - fix: accept an empty storageClassName in StatefulSet claim templates ([#1830](https://github.com/k8sgpt-ai/k8sgpt/pull/1830))
  - fix: keep webhook findings when configurations share a webhook name ([#1827](https://github.com/k8sgpt-ai/k8sgpt/pull/1827))
- <img src="https://github.com/ethereum.png?size=32" width="16" height="16" alt=""> **ethereum/hive**
  - hivesim: return API errors from StopClient, PauseClient and UnpauseClient ([#1616](https://github.com/ethereum/hive/pull/1616))
- <img src="https://github.com/mark3labs.png?size=32" width="16" height="16" alt=""> **mark3labs/mcp-go**
  - feat(server): limit the size of a tool result ([#1048](https://github.com/mark3labs/mcp-go/pull/1048))
  - fix(transport): don't take SSE server requests as responses ([#1085](https://github.com/mark3labs/mcp-go/pull/1085))
  - fix(server): serialize stdio session requests with other writes ([#1084](https://github.com/mark3labs/mcp-go/pull/1084))
  - fix(mcp): let WithRawInputSchema replace the default input schema ([#1082](https://github.com/mark3labs/mcp-go/pull/1082))
- <img src="https://github.com/hyperledger.png?size=32" width="16" height="16" alt=""> **hyperledger/fabric**
  - Wrap the Domain template error in the ccaas builder ([#5621](https://github.com/hyperledger/fabric/pull/5621))

Plus [12 more in review](https://github.com/search?q=is%3Apr+is%3Aopen+is%3Apublic+author%3Ahmdsefi+-user%3Ahmdsefi+-repo%3AGreedyC%2Fgograph+-repo%3Aabhijeetnardele24-hash%2Fgograph&type=pullrequests).

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
