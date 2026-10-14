# Hamed Yousefi

Platform engineer at
<img src="https://github.com/Polymarket.png?size=32" width="16" height="16" alt="">
[Polymarket](https://polymarket.com), based in Dubai. I write Go, mostly distributed
systems, blockchain infrastructure and LLM inference infrastructure.

Most of my day-to-day work is in private repositories, so my contribution graph shows
more than the public activity below.

## Now

- **[gograph](https://github.com/hmdsefi/gograph)**: <!-- gograph:start -->[v0.8.2](https://github.com/hmdsefi/gograph/releases/tag/v0.8.2) shipped on October 2. Next is [v0.9.0](https://github.com/hmdsefi/gograph/milestone/1), due October 19: Dependency graph toolkit.<!-- gograph:end -->
  Contributions are welcome, and
  [CONTRIBUTING.md](https://github.com/hmdsefi/gograph/blob/master/CONTRIBUTING.md) explains
  where to start.
- **Upstream fixes** in Go infrastructure projects, mostly race conditions, error handling
  and tests that had been switched off. The latest are listed below.

## Recent upstream contributions

<!-- recent-prs:start -->
- <img src="https://github.com/vllm-project.png?size=32" width="16" height="16" alt=""> **vllm-project/aibrix**
  - \[Bug\] Round request trace bucket indexes instead of truncating ([#3046](https://github.com/vllm-project/aibrix/pull/3046))
  - \[Bug\] Stop the VTC token tracker from keeping stale user totals ([#3048](https://github.com/vllm-project/aibrix/pull/3048))
  - \[Bug\] Keep a prefix's pods when one of its branches is evicted ([#3044](https://github.com/vllm-project/aibrix/pull/3044))
  - \[Bug\] Remove the Preble histogram map that kept every tree node ([#3050](https://github.com/vllm-project/aibrix/pull/3050))
- <img src="https://github.com/abhijeetnardele24-hash.png?size=32" width="16" height="16" alt=""> **abhijeetnardele24-hash/gograph**
  - Check for nil results in the Sources and Sinks tests ([#1](https://github.com/abhijeetnardele24-hash/gograph/pull/1))
- <img src="https://github.com/llm-d.png?size=32" width="16" height="16" alt=""> **llm-d/llm-d-router**
  - fix(epp): reject file-discovery entries without a unique name ([#3390](https://github.com/llm-d/llm-d-router/pull/3390))
  - fix(epp): use the pod's node name as the topology hostname fallback ([#3386](https://github.com/llm-d/llm-d-router/pull/3386))
  - fix(sidecar): forward requests with n \> 1 without chunked decode ([#3388](https://github.com/llm-d/llm-d-router/pull/3388))
  - feat(sidecar): treat an Anthropic cache\_threshold stop reason as a prefill fallback ([#3268](https://github.com/llm-d/llm-d-router/pull/3268))
- <img src="https://github.com/hyperledger.png?size=32" width="16" height="16" alt=""> **hyperledger/fabric**
  - Honor the chaincode connection.json domain field ([#5617](https://github.com/hyperledger/fabric/pull/5617))

Plus [22 more in review](https://github.com/search?q=is%3Apr+is%3Aopen+is%3Apublic+author%3Ahmdsefi+-user%3Ahmdsefi&type=pullrequests).
<!-- recent-prs:end -->

[All my merged pull requests to other projects](https://github.com/search?q=is%3Apr+is%3Amerged+author%3Ahmdsefi+-user%3Ahmdsefi&type=pullrequests)

## Projects

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
