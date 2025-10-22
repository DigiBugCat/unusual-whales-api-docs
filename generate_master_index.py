import json

# Load the endpoints breakdown
with open('endpoints_breakdown.json', 'r') as f:
    data = json.load(f)

# Create master index markdown
output = """# Unusual Whales API - Master Index

**Total Endpoints**: {total}

**Categories**: 20

**Documentation Status**: In Progress

**Last Updated**: 2025-10-22

---

## Progress Overview

| Category | Endpoints | Documented | Status |
|----------|-----------|------------|--------|
""".format(total=data['total'])

# Add category rows
for category, endpoints in sorted(data['categories'].items()):
    count = len(endpoints)
    output += f"| {category} | {count} | 0/{count} | 🔴 Not Started |\n"

output += """
---

## Endpoints by Category

"""

# Add detailed endpoint listings by category
for category, endpoints in sorted(data['categories'].items()):
    output += f"\n### {category.title()} ({len(endpoints)} endpoints)\n\n"
    output += "| # | Path | Method | Summary | Status |\n"
    output += "|---|------|--------|---------|--------|\n"
    
    for i, ep in enumerate(sorted(endpoints, key=lambda x: x['path']), 1):
        path = ep['path']
        method = ep['method']
        summary = ep['summary'] or 'N/A'
        output += f"| {i} | `{path}` | {method} | {summary} | 🔴 |\n"

output += """

---

## Legend

- 🔴 Not Started
- 🟡 In Progress
- 🟢 Completed
- ✅ Validated

---

## Notes

- Each endpoint will have its own dedicated markdown file
- Files are organized by category in the `docs/` directory
- Use the ENDPOINT_TEMPLATE.md as a starting point for new documentation
- All endpoints should be tested with actual API calls before marking as completed
"""

# Write to file
with open('MASTER_INDEX.md', 'w') as f:
    f.write(output)

print("✓ Created MASTER_INDEX.md")

# Also create a simple progress tracker JSON
progress = {
    "total_endpoints": data['total'],
    "documented": 0,
    "validated": 0,
    "in_progress": 0,
    "categories": {}
}

for category, endpoints in data['categories'].items():
    progress["categories"][category] = {
        "total": len(endpoints),
        "documented": 0,
        "validated": 0,
        "endpoints": {}
    }
    for ep in endpoints:
        progress["categories"][category]["endpoints"][ep['path']] = {
            "method": ep['method'],
            "status": "not_started",
            "validated": False,
            "file_path": ""
        }

with open('progress.json', 'w') as f:
    json.dump(progress, f, indent=2)

print("✓ Created progress.json")
