# Hamed Yousefi

Platform engineer at
<img src="https://github.com/Polymarket.png?size=32" width="16" height="16" alt="">
[Polymarket](https://polymarket.com), based in Dubai. I write Go, mostly distributed
systems, blockchain infrastructure and LLM inference infrastructure.

Most of my day-to-day work is in private repositories, so my contribution graph shows
more than the public activity below.

## Now

- **[gograph](https://github.com/hmdsefi/gograph)**: <!-- gograph:start -->[v0.8.2](https://github.com/hmdsefi/gograph/releases/tag/v0.8.2) shipped on October 2. Next is [v0.9.0](https://github.com/hmdsefi/gograph/milestone/1), due October 27: Dependency graph toolkit.<!-- gograph:end -->
  Contributions are welcome, and
  [CONTRIBUTING.md](https://github.com/hmdsefi/gograph/blob/master/CONTRIBUTING.md) explains
  where to start.
- **Upstream fixes** in Go infrastructure projects, mostly race conditions, error handling
  and tests that had been switched off. The latest are listed below.

## Recent upstream contributions

<!-- recent-prs:start -->
- <img src="https://github.com/vllm-project.png?size=32" width="16" height="16" alt=""> **vllm-project/aibrix**
  - \[Bug\] Fix TOS V1 download when part\_chunksize is not set ([#2895](https://github.com/vllm-project/aibrix/pull/2895))
  - \[CI\] Run integration-tagged controller tests in CI ([#2896](https://github.com/vllm-project/aibrix/pull/2896))
  - \[Bug\] Keep prefix cache blocks dirty when they change during a delta push ([#2877](https://github.com/vllm-project/aibrix/pull/2877))
  - \[Bug\] Stop NewJSONPatch from prepending empty operations ([#2878](https://github.com/vllm-project/aibrix/pull/2878))
- <img src="https://github.com/maximhq.png?size=32" width="16" height="16" alt=""> **maximhq/bifrost**
  - \[fix\]: use provider-reported cost for transcription pricing ([#7825](https://github.com/maximhq/bifrost/pull/7825))
- <img src="https://github.com/hyperledger.png?size=32" width="16" height="16" alt=""> **hyperledger/fabric**
  - Reject key-level endorsement policies that cannot be parsed ([#5598](https://github.com/hyperledger/fabric/pull/5598))
  - Don't send the invalid block ID error twice in the participation API ([#5597](https://github.com/hyperledger/fabric/pull/5597))
  - Stop the follower chain when the channel membership check fails ([#5595](https://github.com/hyperledger/fabric/pull/5595))
  - Fix a race between starting and stopping the delivery service ([#5591](https://github.com/hyperledger/fabric/pull/5591))
- <img src="https://github.com/filecoin-project.png?size=32" width="16" height="16" alt=""> **filecoin-project/lotus**
  - fix(config): accept LOTUS\_CHAINSTORE\_ENABLESPLITSTORE in splitstore validation ([#13851](https://github.com/filecoin-project/lotus/pull/13851))

Plus [15 more in review](https://github.com/search?q=is%3Apr+is%3Aopen+is%3Apublic+author%3Ahmdsefi+-user%3Ahmdsefi&type=pullrequests).
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

## Contact

[LinkedIn](https://www.linkedin.com/in/hamed-yousefi-411251b5/)
