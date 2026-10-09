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
- <img src="https://github.com/mark3labs.png?size=32" width="16" height="16" alt=""> **mark3labs/mcp-go**
  - fix(server): treat a non-positive pagination limit as no paging ([#1047](https://github.com/mark3labs/mcp-go/pull/1047))
  - fix(mcp): keep structuredContent on tool\_result content ([#1031](https://github.com/mark3labs/mcp-go/pull/1031))
  - fix(server): reject an unsupported MCP-Protocol-Version header ([#1030](https://github.com/mark3labs/mcp-go/pull/1030))
  - fix: parse sampling content sent as an array ([#1029](https://github.com/mark3labs/mcp-go/pull/1029))
  - fix(mcp): omit empty completion context arguments ([#1024](https://github.com/mark3labs/mcp-go/pull/1024))
- <img src="https://github.com/vllm-project.png?size=32" width="16" height="16" alt=""> **vllm-project/aibrix**
  - \[Feat\] Report how many prefix blocks are cached ([#2945](https://github.com/vllm-project/aibrix/pull/2945))
- <img src="https://github.com/hyperledger.png?size=32" width="16" height="16" alt=""> **hyperledger/fabric**
  - Reject illegal channel IDs in configtxgen ([#5609](https://github.com/hyperledger/fabric/pull/5609))
- <img src="https://github.com/llm-d.png?size=32" width="16" height="16" alt=""> **llm-d/llm-d-router**
  - fix(sidecar): record stage metrics in the P2P connector ([#3093](https://github.com/llm-d/llm-d-router/pull/3093))
  - fix(sidecar): recover a streamed decode-first abort in shared storage ([#3120](https://github.com/llm-d/llm-d-router/pull/3120))
  - fix(sidecar): keep discarded decode-first headers out of the response ([#3121](https://github.com/llm-d/llm-d-router/pull/3121))

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
