# Hamed Yousefi

Platform engineer at [Polymarket](https://polymarket.com), based in Dubai. I write Go,
mostly distributed systems, blockchain infrastructure and LLM inference infrastructure.

Most of my day-to-day work is in private repositories, so my contribution graph shows
more than the public activity below.

## Now

- **[gograph](https://github.com/hmdsefi/gograph)**:
  [v0.8.2](https://github.com/hmdsefi/gograph/releases/tag/v0.8.2) shipped on October 2
  with four bug fixes. Next is [v0.9.0](https://github.com/hmdsefi/gograph/milestone/1),
  due October 27, which adds a dependency graph toolkit: condensation into a DAG, Graphviz
  DOT export, topological levels, critical paths and induced subgraphs. Contributions are
  welcome, and [CONTRIBUTING.md](https://github.com/hmdsefi/gograph/blob/master/CONTRIBUTING.md)
  explains where to start.
- **Upstream fixes** in Go infrastructure projects, mostly race conditions, error handling
  and tests that had been switched off. In review now:
  [llm-d router](https://github.com/llm-d/llm-d-router),
  [mcp-go](https://github.com/mark3labs/mcp-go),
  [Bifrost](https://github.com/maximhq/bifrost),
  [k8sgpt](https://github.com/k8sgpt-ai/k8sgpt) and
  [Ethereum Hive](https://github.com/ethereum/hive).

## Recent upstream contributions

- **[vLLM AIBrix](https://github.com/vllm-project/aibrix)** (LLM inference on Kubernetes):
  kept prefix cache blocks dirty when they change during a delta push
  ([#2877](https://github.com/vllm-project/aibrix/pull/2877)), stopped JSON patches from
  starting with empty operations ([#2878](https://github.com/vllm-project/aibrix/pull/2878)),
  and re-enabled the controller test suites in CI
  ([#2861](https://github.com/vllm-project/aibrix/pull/2861),
  [#2864](https://github.com/vllm-project/aibrix/pull/2864),
  [#2896](https://github.com/vllm-project/aibrix/pull/2896)).
- **[Hyperledger Fabric](https://github.com/hyperledger/fabric)**: fixed a race between
  starting and stopping the delivery service
  ([#5591](https://github.com/hyperledger/fabric/pull/5591)), applied the peer's gRPC
  message size limits to the delivery client
  ([#5590](https://github.com/hyperledger/fabric/pull/5590)), released the registrar lock
  when a channel update is rejected ([#5586](https://github.com/hyperledger/fabric/pull/5586)),
  and removed consensus data when a channel is removed
  ([#5588](https://github.com/hyperledger/fabric/pull/5588)).
- **[Filecoin Lotus](https://github.com/filecoin-project/lotus)**: stopped the F3 datastore
  from being closed twice on shutdown
  ([#13850](https://github.com/filecoin-project/lotus/pull/13850)) and upgraded the build
  to Go 1.26.8 ([#13841](https://github.com/filecoin-project/lotus/pull/13841)).

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
