import yaml
import json

# Load the OpenAPI spec
with open('openapi-spec.yaml', 'r') as f:
    spec = yaml.safe_load(f)

endpoints = []

# Parse all paths
for path, methods in spec.get('paths', {}).items():
    for method, details in methods.items():
        if method in ['get', 'post', 'put', 'delete', 'patch']:
            endpoint = {
                'path': path,
                'method': method.upper(),
                'summary': details.get('summary', ''),
                'description': details.get('description', '').strip()[:200],
                'operationId': details.get('operationId', ''),
                'tags': details.get('tags', []),
                'parameters': len(details.get('parameters', [])),
            }
            endpoints.append(endpoint)

# Group by category (first part of path after /api/)
categories = {}
for ep in endpoints:
    parts = ep['path'].split('/')
    if len(parts) >= 3:
        category = parts[2]  # Get category from /api/{category}/...
        if category not in categories:
            categories[category] = []
        categories[category].append(ep)

# Print summary
print(f"Total Endpoints: {len(endpoints)}\n")
print("Categories:")
for cat, eps in sorted(categories.items()):
    print(f"  - {cat}: {len(eps)} endpoints")

# Save detailed breakdown
with open('endpoints_breakdown.json', 'w') as f:
    json.dump({
        'total': len(endpoints),
        'categories': categories,
        'all_endpoints': endpoints
    }, f, indent=2)

print("\n✓ Saved detailed breakdown to endpoints_breakdown.json")
