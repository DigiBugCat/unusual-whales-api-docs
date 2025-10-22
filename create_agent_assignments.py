import json

# Load the endpoints breakdown
with open('endpoints_breakdown.json', 'r') as f:
    data = json.load(f)

# Define agent assignments
assignments = {
    "agent_1": {
        "name": "Agent 1: Core Operations",
        "categories": ["alerts", "congress", "darkpool", "earnings"],
        "endpoints": []
    },
    "agent_2": {
        "name": "Agent 2: ETFs & Institutions",
        "categories": ["etfs", "group-flow", "insider", "institution", "institutions"],
        "endpoints": []
    },
    "agent_3": {
        "name": "Agent 3: Market & Options",
        "categories": ["market", "net-flow", "news", "option-contract", "option-trades"],
        "endpoints": []
    },
    "agent_4": {
        "name": "Agent 4: Screening & Analysis",
        "categories": ["politician-portfolios", "screener", "seasonality", "shorts"],
        "endpoints": []
    },
    "agent_5": {
        "name": "Agent 5: Stocks & WebSocket",
        "categories": ["socket", "stock"],
        "endpoints": []
    }
}

# Populate endpoints for each agent
for agent_id, agent_info in assignments.items():
    for category in agent_info['categories']:
        if category in data['categories']:
            for ep in data['categories'][category]:
                assignments[agent_id]['endpoints'].append({
                    "category": category,
                    "path": ep['path'],
                    "method": ep['method'],
                    "summary": ep['summary'],
                    "description": ep['description'],
                    "operationId": ep['operationId'],
                    "parameters": ep['parameters']
                })

# Save each agent's assignment
for agent_id, agent_info in assignments.items():
    filename = f"{agent_id}_assignment.json"
    with open(filename, 'w') as f:
        json.dump(agent_info, f, indent=2)
    print(f"✓ Created {filename} - {len(agent_info['endpoints'])} endpoints")

# Create a summary
summary = """# Agent Assignments Summary

## Overview

Total of 5 agents will work in parallel to document and validate all 109 endpoints.

## Agent Breakdown

"""

for agent_id, agent_info in assignments.items():
    summary += f"\n### {agent_info['name']}\n"
    summary += f"**Endpoints**: {len(agent_info['endpoints'])}\n"
    summary += f"**Categories**: {', '.join(agent_info['categories'])}\n"
    summary += f"**Assignment File**: `{agent_id}_assignment.json`\n"

with open('AGENT_ASSIGNMENTS.md', 'w') as f:
    f.write(summary)

print("\n✓ Created AGENT_ASSIGNMENTS.md")
