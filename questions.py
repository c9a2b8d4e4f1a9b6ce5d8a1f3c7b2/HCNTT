import json
import os

from decouple import config

MAX_REPO = 50
SOURCE_REPO = "hashgraph/hiero-consensus-node"
REPO_NAME = "hiero-consensus-node"
run_number = os.environ.get('GITHUB_RUN_NUMBER', '0')

target_scopes = [
    ""
]



def get_cyclic_index(run_number, max_index=100):
    """Convert run number to a cyclic index between 1 and max_index"""
    return (int(run_number) - 1) % max_index + 1


if run_number == "0":
    BASE_URL = f"https://deepwiki.com/{SOURCE_REPO}"
else:
    # Convert to cyclic index (1-100)
    run_index = get_cyclic_index(run_number, MAX_REPO)
    # Format the URL with leading zeros
    repo_number = f"{run_index:03d}"
    BASE_URL = f"https://deepwiki.com/0xOyakhilome/{REPO_NAME}--{repo_number}"

scope_files = [
    "hapi/hedera-protobuf-java-api/src/main/proto/platform/event/event_consensus_data.proto",
    "hapi/hedera-protobuf-java-api/src/main/proto/platform/event/event_core.proto",
    "hapi/hedera-protobuf-java-api/src/main/proto/platform/event/event_descriptor.proto",
    "hapi/hedera-protobuf-java-api/src/main/proto/platform/event/gossip_event.proto",
    "hapi/hedera-protobuf-java-api/src/main/proto/platform/event/state_signature_transaction.proto",
    "hapi/hedera-protobuf-java-api/src/main/proto/platform/message/gossip_known_tips.proto",
    "hapi/hedera-protobuf-java-api/src/main/proto/platform/message/gossip_ping.proto",
    "hapi/hedera-protobuf-java-api/src/main/proto/platform/message/gossip_sync_data.proto",
    "hapi/hedera-protobuf-java-api/src/main/proto/platform/state/platform_state.proto",
    "hapi/hedera-protobuf-java-api/src/main/proto/platform/state/virtual_map_state.proto",
    "platform-sdk/consensus-gossip-impl/src/main/java/module-info.java",
    "platform-sdk/consensus-gossip-impl/src/main/java/org/hiero/consensus/gossip/impl/DefaultGossipModule.java",
    "platform-sdk/consensus-gossip-impl/src/main/java/org/hiero/consensus/gossip/impl/gossip/Gossip.java",
    "platform-sdk/consensus-gossip-impl/src/main/java/org/hiero/consensus/gossip/impl/gossip/GossipController.java",
    "platform-sdk/consensus-gossip-impl/src/main/java/org/hiero/consensus/gossip/impl/gossip/GossipWiring.java",
    "platform-sdk/consensus-gossip-impl/src/main/java/org/hiero/consensus/gossip/impl/gossip/SyncException.java",
    "platform-sdk/consensus-gossip-impl/src/main/java/org/hiero/consensus/gossip/impl/gossip/SyncGossipModular.java",
    "platform-sdk/consensus-gossip-impl/src/main/java/org/hiero/consensus/gossip/impl/gossip/Utilities.java",
    "platform-sdk/consensus-gossip-impl/src/main/java/org/hiero/consensus/gossip/impl/gossip/permits/LruSyncGuard.java",
    "platform-sdk/consensus-gossip-impl/src/main/java/org/hiero/consensus/gossip/impl/gossip/permits/NoopSyncGuard.java",
    "platform-sdk/consensus-gossip-impl/src/main/java/org/hiero/consensus/gossip/impl/gossip/permits/SyncGuard.java",
    "platform-sdk/consensus-gossip-impl/src/main/java/org/hiero/consensus/gossip/impl/gossip/permits/SyncGuardFactory.java",
    "platform-sdk/consensus-gossip-impl/src/main/java/org/hiero/consensus/gossip/impl/gossip/permits/SyncPermitMetrics.java",
    "platform-sdk/consensus-gossip-impl/src/main/java/org/hiero/consensus/gossip/impl/gossip/permits/SyncPermitProvider.java",
    "platform-sdk/consensus-gossip-impl/src/main/java/org/hiero/consensus/gossip/impl/gossip/rpc/GossipRpcReceiver.java",
    "platform-sdk/consensus-gossip-impl/src/main/java/org/hiero/consensus/gossip/impl/gossip/rpc/GossipRpcReceiverHandler.java",
    "platform-sdk/consensus-gossip-impl/src/main/java/org/hiero/consensus/gossip/impl/gossip/rpc/GossipRpcSender.java",
    "platform-sdk/consensus-gossip-impl/src/main/java/org/hiero/consensus/gossip/impl/gossip/rpc/SyncData.java",
    "platform-sdk/consensus-gossip-impl/src/main/java/org/hiero/consensus/gossip/impl/gossip/shadowgraph/InsertableStatus.java",
    "platform-sdk/consensus-gossip-impl/src/main/java/org/hiero/consensus/gossip/impl/gossip/shadowgraph/ReservedEventWindow.java",
    "platform-sdk/consensus-gossip-impl/src/main/java/org/hiero/consensus/gossip/impl/gossip/shadowgraph/RpcPeerHandler.java",
    "platform-sdk/consensus-gossip-impl/src/main/java/org/hiero/consensus/gossip/impl/gossip/shadowgraph/RpcPeerState.java",
    "platform-sdk/consensus-gossip-impl/src/main/java/org/hiero/consensus/gossip/impl/gossip/shadowgraph/ShadowEvent.java",
    "platform-sdk/consensus-gossip-impl/src/main/java/org/hiero/consensus/gossip/impl/gossip/shadowgraph/Shadowgraph.java",
    "platform-sdk/consensus-gossip-impl/src/main/java/org/hiero/consensus/gossip/impl/gossip/shadowgraph/ShadowgraphInsertionException.java",
    "platform-sdk/consensus-gossip-impl/src/main/java/org/hiero/consensus/gossip/impl/gossip/shadowgraph/ShadowgraphMetrics.java",
    "platform-sdk/consensus-gossip-impl/src/main/java/org/hiero/consensus/gossip/impl/gossip/shadowgraph/ShadowgraphReservation.java",
    "platform-sdk/consensus-gossip-impl/src/main/java/org/hiero/consensus/gossip/impl/gossip/shadowgraph/ShadowgraphSynchronizer.java",
    "platform-sdk/consensus-gossip-impl/src/main/java/org/hiero/consensus/gossip/impl/gossip/shadowgraph/SyncPhase.java",
    "platform-sdk/consensus-gossip-impl/src/main/java/org/hiero/consensus/gossip/impl/gossip/shadowgraph/SyncResult.java",
    "platform-sdk/consensus-gossip-impl/src/main/java/org/hiero/consensus/gossip/impl/gossip/shadowgraph/SyncTimeoutException.java",
    "platform-sdk/consensus-gossip-impl/src/main/java/org/hiero/consensus/gossip/impl/gossip/shadowgraph/SyncTiming.java",
    "platform-sdk/consensus-gossip-impl/src/main/java/org/hiero/consensus/gossip/impl/gossip/shadowgraph/SyncUtils.java",
    "platform-sdk/consensus-gossip-impl/src/main/java/org/hiero/consensus/gossip/impl/gossip/sync/SyncInputStream.java",
    "platform-sdk/consensus-gossip-impl/src/main/java/org/hiero/consensus/gossip/impl/gossip/sync/SyncMetrics.java",
    "platform-sdk/consensus-gossip-impl/src/main/java/org/hiero/consensus/gossip/impl/gossip/sync/SyncOutputStream.java",
    "platform-sdk/consensus-gossip-impl/src/main/java/org/hiero/consensus/gossip/impl/gossip/sync/protocol/SyncStatusChecker.java",
    "platform-sdk/consensus-gossip-impl/src/main/java/org/hiero/consensus/gossip/impl/network/ByteConstants.java",
    "platform-sdk/consensus-gossip-impl/src/main/java/org/hiero/consensus/gossip/impl/network/Connection.java",
    "platform-sdk/consensus-gossip-impl/src/main/java/org/hiero/consensus/gossip/impl/network/ConnectionManager.java",
    "platform-sdk/consensus-gossip-impl/src/main/java/org/hiero/consensus/gossip/impl/network/ConnectionTracker.java",
    "platform-sdk/consensus-gossip-impl/src/main/java/org/hiero/consensus/gossip/impl/network/ExternalIpAddress.java",
    "platform-sdk/consensus-gossip-impl/src/main/java/org/hiero/consensus/gossip/impl/network/InboundConnectionManager.java",
    "platform-sdk/consensus-gossip-impl/src/main/java/org/hiero/consensus/gossip/impl/network/IpAddressStatus.java",
    "platform-sdk/consensus-gossip-impl/src/main/java/org/hiero/consensus/gossip/impl/network/Network.java",
    "platform-sdk/consensus-gossip-impl/src/main/java/org/hiero/consensus/gossip/impl/network/NetworkMetrics.java",
    "platform-sdk/consensus-gossip-impl/src/main/java/org/hiero/consensus/gossip/impl/network/NetworkPeerIdentifier.java",
    "platform-sdk/consensus-gossip-impl/src/main/java/org/hiero/consensus/gossip/impl/network/NetworkProtocolException.java",
    "platform-sdk/consensus-gossip-impl/src/main/java/org/hiero/consensus/gossip/impl/network/NetworkUtils.java",
    "platform-sdk/consensus-gossip-impl/src/main/java/org/hiero/consensus/gossip/impl/network/OutboundConnectionManager.java",
    "platform-sdk/consensus-gossip-impl/src/main/java/org/hiero/consensus/gossip/impl/network/PeerCommunication.java",
    "platform-sdk/consensus-gossip-impl/src/main/java/org/hiero/consensus/gossip/impl/network/PeerConnectionServer.java",
    "platform-sdk/consensus-gossip-impl/src/main/java/org/hiero/consensus/gossip/impl/network/PeerInfo.java",
    "platform-sdk/consensus-gossip-impl/src/main/java/org/hiero/consensus/gossip/impl/network/SocketConnection.java",
    "platform-sdk/consensus-gossip-impl/src/main/java/org/hiero/consensus/gossip/impl/network/communication/NegotiationException.java",
    "platform-sdk/consensus-gossip-impl/src/main/java/org/hiero/consensus/gossip/impl/network/communication/NegotiationProtocols.java",
    "platform-sdk/consensus-gossip-impl/src/main/java/org/hiero/consensus/gossip/impl/network/communication/Negotiator.java",
    "platform-sdk/consensus-gossip-impl/src/main/java/org/hiero/consensus/gossip/impl/network/communication/NegotiatorBytes.java",
    "platform-sdk/consensus-gossip-impl/src/main/java/org/hiero/consensus/gossip/impl/network/communication/ProtocolNegotiatorThread.java",
    "platform-sdk/consensus-gossip-impl/src/main/java/org/hiero/consensus/gossip/impl/network/communication/handshake/HandshakeException.java",
    "platform-sdk/consensus-gossip-impl/src/main/java/org/hiero/consensus/gossip/impl/network/communication/handshake/HashCompareHandshake.java",
    "platform-sdk/consensus-gossip-impl/src/main/java/org/hiero/consensus/gossip/impl/network/communication/handshake/VersionCompareHandshake.java",
    "platform-sdk/consensus-gossip-impl/src/main/java/org/hiero/consensus/gossip/impl/network/communication/states/InitialState.java",
    "platform-sdk/consensus-gossip-impl/src/main/java/org/hiero/consensus/gossip/impl/network/communication/states/NegotiationState.java",
    "platform-sdk/consensus-gossip-impl/src/main/java/org/hiero/consensus/gossip/impl/network/communication/states/NegotiationStateWithDescription.java",
    "platform-sdk/consensus-gossip-impl/src/main/java/org/hiero/consensus/gossip/impl/network/communication/states/ProtocolNegotiated.java",
    "platform-sdk/consensus-gossip-impl/src/main/java/org/hiero/consensus/gossip/impl/network/communication/states/ReceivedInitiate.java",
    "platform-sdk/consensus-gossip-impl/src/main/java/org/hiero/consensus/gossip/impl/network/communication/states/SentInitiate.java",
    "platform-sdk/consensus-gossip-impl/src/main/java/org/hiero/consensus/gossip/impl/network/communication/states/SentKeepalive.java",
    "platform-sdk/consensus-gossip-impl/src/main/java/org/hiero/consensus/gossip/impl/network/communication/states/Sleep.java",
    "platform-sdk/consensus-gossip-impl/src/main/java/org/hiero/consensus/gossip/impl/network/communication/states/WaitForAcceptReject.java",
    "platform-sdk/consensus-gossip-impl/src/main/java/org/hiero/consensus/gossip/impl/network/connection/NotConnectedConnection.java",
    "platform-sdk/consensus-gossip-impl/src/main/java/org/hiero/consensus/gossip/impl/network/connectivity/ConnectionServer.java",
    "platform-sdk/consensus-gossip-impl/src/main/java/org/hiero/consensus/gossip/impl/network/connectivity/InboundConnectionHandler.java",
    "platform-sdk/consensus-gossip-impl/src/main/java/org/hiero/consensus/gossip/impl/network/connectivity/OutboundConnectionCreator.java",
    "platform-sdk/consensus-gossip-impl/src/main/java/org/hiero/consensus/gossip/impl/network/connectivity/SocketFactory.java",
    "platform-sdk/consensus-gossip-impl/src/main/java/org/hiero/consensus/gossip/impl/network/connectivity/TlsFactory.java",
    "platform-sdk/consensus-gossip-impl/src/main/java/org/hiero/consensus/gossip/impl/network/protocol/HeartbeatPeerProtocol.java",
    "platform-sdk/consensus-gossip-impl/src/main/java/org/hiero/consensus/gossip/impl/network/protocol/HeartbeatProtocol.java",
    "platform-sdk/consensus-gossip-impl/src/main/java/org/hiero/consensus/gossip/impl/network/protocol/PeerProtocol.java",
    "platform-sdk/consensus-gossip-impl/src/main/java/org/hiero/consensus/gossip/impl/network/protocol/Protocol.java",
    "platform-sdk/consensus-gossip-impl/src/main/java/org/hiero/consensus/gossip/impl/network/protocol/ProtocolRunnable.java",
    "platform-sdk/consensus-gossip-impl/src/main/java/org/hiero/consensus/gossip/impl/network/protocol/rpc/RpcInternalExceptionHandler.java",
    "platform-sdk/consensus-gossip-impl/src/main/java/org/hiero/consensus/gossip/impl/network/protocol/rpc/RpcMessageId.java",
    "platform-sdk/consensus-gossip-impl/src/main/java/org/hiero/consensus/gossip/impl/network/protocol/rpc/RpcOverloadMonitor.java",
    "platform-sdk/consensus-gossip-impl/src/main/java/org/hiero/consensus/gossip/impl/network/protocol/rpc/RpcPeerProtocol.java",
    "platform-sdk/consensus-gossip-impl/src/main/java/org/hiero/consensus/gossip/impl/network/protocol/rpc/RpcPingHandler.java",
    "platform-sdk/consensus-gossip-impl/src/main/java/org/hiero/consensus/gossip/impl/network/protocol/rpc/RpcProtocol.java",
    "platform-sdk/consensus-gossip-impl/src/main/java/org/hiero/consensus/gossip/impl/network/topology/ConnectionManagerFactory.java",
    "platform-sdk/consensus-gossip-impl/src/main/java/org/hiero/consensus/gossip/impl/network/topology/DynamicConnectionManagers.java",
    "platform-sdk/consensus-gossip-impl/src/main/java/org/hiero/consensus/gossip/impl/network/topology/NetworkTopology.java",
    "platform-sdk/consensus-gossip-impl/src/main/java/org/hiero/consensus/gossip/impl/network/topology/StaticTopology.java",
    "platform-sdk/consensus-gossip-impl/src/main/java/org/hiero/consensus/gossip/impl/reconnect/ReconnectProtocolFactory.java",
    "platform-sdk/consensus-gossip/src/main/java/module-info.java",
    "platform-sdk/consensus-gossip/src/main/java/org/hiero/consensus/gossip/GossipModule.java",
    "platform-sdk/consensus-gossip/src/main/java/org/hiero/consensus/gossip/ReservedSignedStateResult.java",
    "platform-sdk/consensus-gossip/src/main/java/org/hiero/consensus/gossip/config/BroadcastConfig.java",
    "platform-sdk/consensus-gossip/src/main/java/org/hiero/consensus/gossip/config/GossipConfig.java",
    "platform-sdk/consensus-gossip/src/main/java/org/hiero/consensus/gossip/config/GossipConfigurationExtension.java",
    "platform-sdk/consensus-gossip/src/main/java/org/hiero/consensus/gossip/config/GossipWiringConfig.java",
    "platform-sdk/consensus-gossip/src/main/java/org/hiero/consensus/gossip/config/NetworkEndpoint.java",
    "platform-sdk/consensus-gossip/src/main/java/org/hiero/consensus/gossip/config/NetworkEndpointConverter.java",
    "platform-sdk/consensus-gossip/src/main/java/org/hiero/consensus/gossip/config/ProtocolConfig.java",
    "platform-sdk/consensus-gossip/src/main/java/org/hiero/consensus/gossip/config/SocketConfig.java",
    "platform-sdk/consensus-gossip/src/main/java/org/hiero/consensus/gossip/config/SyncConfig.java",
    "platform-sdk/consensus-reconnect-impl/src/main/java/module-info.java",
    "platform-sdk/consensus-reconnect-impl/src/main/java/org/hiero/consensus/reconnect/impl/DefaultReconnectModule.java",
    "platform-sdk/consensus-reconnect-impl/src/main/java/org/hiero/consensus/reconnect/impl/DefaultSignedStateValidator.java",
    "platform-sdk/consensus-reconnect-impl/src/main/java/org/hiero/consensus/reconnect/impl/ReconnectController.java",
    "platform-sdk/consensus-reconnect-impl/src/main/java/org/hiero/consensus/reconnect/impl/ReconnectCoordinator.java",
    "platform-sdk/consensus-reconnect-impl/src/main/java/org/hiero/consensus/reconnect/impl/ReconnectProtocolFactoryImpl.java",
    "platform-sdk/consensus-reconnect-impl/src/main/java/org/hiero/consensus/reconnect/impl/ReconnectStateException.java",
    "platform-sdk/consensus-reconnect-impl/src/main/java/org/hiero/consensus/reconnect/impl/ReconnectStateLearner.java",
    "platform-sdk/consensus-reconnect-impl/src/main/java/org/hiero/consensus/reconnect/impl/ReconnectStatePeerProtocol.java",
    "platform-sdk/consensus-reconnect-impl/src/main/java/org/hiero/consensus/reconnect/impl/ReconnectStateSyncProtocol.java",
    "platform-sdk/consensus-reconnect-impl/src/main/java/org/hiero/consensus/reconnect/impl/ReconnectStateTeacher.java",
    "platform-sdk/consensus-reconnect-impl/src/main/java/org/hiero/consensus/reconnect/impl/ReconnectStateTeacherThrottle.java",
]



target_scopes += [
    "Critical: Network not being able to confirm new transactions (total network shutdown)",
    "Critical: Network partition caused outside of design parameters",
    "Critical: Direct loss of funds",
    "Critical: Unintended permanent freezing of funds",
    "Critical: Any impact caused by Tampering/Manipulating Hashgraph history",

    "High: Temporary freezing of network transactions by delaying one block by 500% or more of the average block time of the preceding 24 hours beyond standard difficulty adjustments",
    "High: Preventing gossip of a transaction or multiple transactions",
    "High: Reorganizing transaction history without direct theft of funds",
    "High: Any impacts caused by Tampering with submitted transactions",
    "High: Authorizing transactions without approval from signers/owners",
    "High: Non-network-based DoS affecting projects with greater than or equal to 25% of the market capitalization on top of the respective layer",

    "Medium: Increasing network processing node resource consumption by at least 30% without brute force actions, compared to the preceding 24 hours",
    "Medium: Shutdown of greater than or equal to 30% of network processing nodes without brute force actions, but does not shut down the network",
    "Medium: A bug in the respective layer 0/1/2 network code that results in unintended smart contract behavior with no concrete funds at direct risk",
    "Medium: Incorrect or missing records exported to mirror nodes",
    "Medium: Impacts caused by griefing with no economic damage to any user on the network",
    "Medium: Theft of unpaid staking rewards",
    "Medium: Modification of transaction fees outside of design parameters"
]


def question_generator(target_file: str) -> str:
    """
    Generate exploit-focused audit questions for one scope file.
    """
    prompt = f"""
Generate exploit-focused security audit questions for `{target_file}` only.

Important: `{target_file}` is in-scope in this  repository and is accessible context.
Do not say the file is missing/inaccessible and do not ask for file content.

Rules:
- Every question must start with `[File: {target_file}]`.
- Use symbols/function names from `{target_file}` when possible.
- Each question must include attacker action, preconditions, trigger, and concrete impact.
- Every question MUST assume the attacker is a user with NO special permissions (unprivileged external user).
- Do not assume admin keys, owner roles, privileged APIs, internal network access, or operator-only controls.
- Only include privileged-access scenarios if they clearly start from a no-permission user path that leads to escalation.
- Focus questions on user without privilege this is very important 
- Focus on the scope solely and only generate questions base on the scope .
- Never return empty; output the maximum valid high-signal set.
- Hard minimum 80 questions; target up to 150.
- Do not generate questions base on the Security.MD file that would result in out of scope and rejected vulnerability 
- Generate question base on the scope provided this is very very important 
- Focus questions in scope if scope is provided 

Note: Think like an attacker with no permission (very important), check Researcher.MD also to get more info.

Output only valid Python (no markdown, no explanations):
questions = [
    "[File: {target_file}] [Function: functionName()] Can an unprivileged external user do X by exploiting Y under Z preconditions, causing concrete impact?",
    "[File: {target_file}] [Function: anotherFunction()] Can a user without permission craft malformed input/path W to bypass check Q and violate invariant R, leading to impact S?",
]
"""
    return prompt


def audit_format(security_question: str) -> str:
    """
    Generate a focused security-audit prompt.
    """
    prompt = f"""# SECURITY AUDIT PROMPT

## Security Question
{security_question}

## Access Rules (Strict)
- In-scope paths referenced by this question exist in this repository and are accessible context.
- Do not claim files are missing/inaccessible.
- Do not ask for file content.
- Do not output repo-navigation/help text.
- Vuln is valid mostly when it requires user with no privileged 

## Mission
Investigate only this question for real, exploitable protocol-security issues in contracts.
Ignore style/refactor/docs issues.



Note: Think like a real attacker in a real world and  check Researcher.MD also to get more info and be smart.


## Validation Gate (all required)
1. Exact in-scope code location (file, function, line range).
2. Clear root cause and failed assumption.
3. Practical exploit path (preconditions -> trigger -> result).
4. Existing checks reviewed and shown insufficient.
5. Concrete impact + realistic likelihood.

## Output (Strict)
If and only if all validation checks pass, output this exact structure:

### Title
[Concise vulnerability title]

### Summary
[2-3 sentence summary]

### Finding Description
[Exact code path, root cause, exploit flow, why checks fail]

### Impact Explanation
[Concrete protocol impact and severity rationale]

### Likelihood Explanation
[Realistic attacker capability, feasibility, repeatability]

### Recommendation
[Specific fix guidance]

### Proof of Concept
[Reproducible steps]

Else output exactly:
#NoVulnerability found for this question.

Output only one of the two outcomes above. No extra text.
"""
    return prompt


def validation_format(report: str) -> str:
    """
    Generate a short strict-validation prompt for  security claims.
    """
    prompt = f"""#  VALIDATION PROMPT

## Security Claim
{report}


Note: Check the Security.MD and never generate report that would result in out of scope and rejected vulnerability 


## Required Checks (all must pass)
1. Exact file/function/line references.
2. Clear root cause and failed assumption.
3. Realistic exploit flow and why checks fail.
4. Concrete impact and realistic likelihood.

## Output (Strict)
If valid, output:

Audit Report
## Title
## Summary
## Finding Description
## Impact Explanation
## Likelihood Explanation
## Recommendation
## Proof of Concept

Else output exactly:
#NoVulnerability found for this question.

Output only one of the two outcomes above.
"""
    return prompt


def scan_format(report: str) -> str:
    """
    Generate a short cross-project analog scan prompt for .
    """
    prompt = f"""# ANALOG SCAN PROMPT

## External Report
{report}

## Access Rules (Strict)
- Treat in-scope  files as accessible context.
- Do not claim missing/inaccessible files.
- Do not ask for repository contents.

## Objective
Find whether the same vulnerability class can occur in  in-scope code.
Use the external report as a hint, not as proof.


Note: Check the RESEARCHER.md and think in this actual way 
Note: Check the Security.MD and never generate report that would result in out of scope and rejected vulnerability 

## Method
1. Classify vuln type (auth, accounting, state transition, pricing/rounding, replay, reentrancy, DoS).
2. Map this external report to this protocol and check every scenario in this protocol to find valid vulnerability.
3. Prove root cause with exact file/function/line references.
4. Confirm concrete impact + realistic likelihood.

## Disqualify Immediately
- No reachable attacker-controlled entry path.
- Trusted-role compromise required.
- Theoretical-only issue with no protocol impact.
- Impact or likelihood missing.

## Output (Strict)
If valid analog exists, output:

### Title
### Summary
### Finding Description
### Impact Explanation
### Likelihood Explanation
### Recommendation
### Proof of Concept

If not, output exactly:
#NoVulnerability found for this question.

No extra text.
"""
    return prompt


