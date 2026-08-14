# RooomUI

**Agent-native UI and human-approval interaction layer for enterprise AI applications.**

Version: `0.1.0`

RooomUI is a ROOOMTECH interaction core for connecting AI agents to business applications. It defines shared state and structured UI/tool/approval events so applications can render agent output while keeping human control over consequential actions.

## What it does

- Maintain shared application/agent state
- Emit structured generative-UI events
- Represent tool execution requests as explicit events
- Represent human approval checkpoints before consequential operations
- Keep event history for replay and audit
- Stay independent of a specific LLM or agent framework

## Why RooomUI

RooomAgent handles reasoning and tools; RooomUI handles the user-facing interaction contract. This separation lets web, mobile, Slack/Teams-style and internal enterprise applications reuse the same agent backend while implementing their own presentation layer and approval experience.

## Quick start

Requires Python 3.11+.

```bash
python -m unittest discover -s tests -v
```

Example:

```python
from rooom_ui.core import SessionState

session = SessionState({"customer_id": "C001"})
session.patch({"status": "review"})
session.request_tool("update_record", {"id": "C001"}, "write")
print(session.events())
```

## Current status

`0.1.0` is an early working core. It is an independent ROOOMTECH implementation and does not claim feature parity with CopilotKit or other agent-UI frameworks. CopilotKit is listed in `THIRD_PARTY_NOTICES.md` as a design/reference project; its source code is not bundled into RooomUI.

## Commercial licensing

ROOOMTECH-authored code is available under the PolyForm Noncommercial License 1.0.0 for permitted noncommercial use. Business, production, commercial-purpose and other uses outside those permissions require a separate paid ROOOMTECH Commercial Software License.

Commercial licensing, implementation, maintenance, private builds, security support and custom development are available from ROOOMTECH.

Contact: `support@rooomtech.com`

See `LICENSE`, `COMMERCIAL_LICENSE.md`, `SECURITY.md`, and `THIRD_PARTY_NOTICES.md`.
