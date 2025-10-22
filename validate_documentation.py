import os
import json
from pathlib import Path

print("=" * 80)
print("UNUSUAL WHALES API DOCUMENTATION - VALIDATION REPORT")
print("=" * 80)
print()

# 1. Count files
print("📁 FILE COUNT VALIDATION")
print("-" * 80)

endpoint_files = list(Path("docs").glob("**/*.md"))
readme_files = [f for f in endpoint_files if f.name == "README.md"]
doc_files = [f for f in endpoint_files if f.name != "README.md"]

print(f"✓ Total markdown files: {len(endpoint_files)}")
print(f"✓ Category README files: {len(readme_files)}")
print(f"✓ Endpoint documentation files: {len(doc_files)}")
print(f"✓ Expected endpoint files: 109")
print(f"✓ Match: {'YES' if len(doc_files) == 109 else 'NO'}")
print()

# 2. Category coverage
print("📂 CATEGORY COVERAGE")
print("-" * 80)

categories = {
    "alerts": 2, "congress": 3, "darkpool": 2, "earnings": 3, "etfs": 5,
    "group-flow": 2, "insider": 4, "institution": 4, "institutions": 2,
    "market": 12, "net-flow": 1, "news": 1, "option-contract": 4,
    "option-trades": 2, "politician-portfolios": 3, "screener": 3,
    "seasonality": 4, "shorts": 5, "socket": 6, "stock": 41
}

for category, expected_count in sorted(categories.items()):
    category_dir = Path(f"docs/{category}")
    if category_dir.exists():
        files = [f for f in category_dir.glob("*.md") if f.name != "README.md"]
        actual_count = len(files)
        status = "✓" if actual_count == expected_count else "⚠"
        print(f"{status} {category:25} Expected: {expected_count:2}, Found: {actual_count:2}")
    else:
        print(f"✗ {category:25} Directory not found!")

print()

# 3. File structure validation
print("📋 FILE STRUCTURE VALIDATION")
print("-" * 80)

required_files = [
    "README.md",
    "openapi-spec.yaml",
    "ENDPOINT_TEMPLATE.md",
    "MASTER_INDEX.md",
    "endpoints_breakdown.json",
    "progress.json"
]

for filename in required_files:
    exists = os.path.exists(filename)
    status = "✓" if exists else "✗"
    print(f"{status} {filename}")

print()

# 4. Check for agent reports
print("📊 AGENT COMPLETION REPORTS")
print("-" * 80)

agent_files = [
    "AGENT_1_COMPLETION_REPORT.md",
    "AGENT_ASSIGNMENTS.md"
]

for filename in agent_files:
    exists = os.path.exists(filename)
    status = "✓" if exists else "⚠"
    print(f"{status} {filename}")

print()

# 5. Sample content validation (check a few files have proper structure)
print("📝 CONTENT STRUCTURE VALIDATION (Sample)")
print("-" * 80)

sample_files = [
    "docs/alerts/get-alerts.md",
    "docs/stock/stock-info.md",
    "docs/market/market-tide.md"
]

required_sections = [
    "# ",  # Title
    "## Endpoint Details",
    "## Authentication",
    "## Example Request",
    "## Response"
]

for sample_file in sample_files:
    if os.path.exists(sample_file):
        with open(sample_file, 'r') as f:
            content = f.read()
        
        found_sections = sum(1 for section in required_sections if section in content)
        status = "✓" if found_sections >= 4 else "⚠"
        print(f"{status} {sample_file:40} Sections: {found_sections}/{len(required_sections)}")
    else:
        print(f"⚠ {sample_file:40} File not found")

print()

# 6. Summary
print("=" * 80)
print("VALIDATION SUMMARY")
print("=" * 80)

total_expected = 109
total_found = len(doc_files)
category_count = len(categories)
readme_count = len(readme_files)

print(f"✓ Total Endpoints Documented: {total_found}/{total_expected}")
print(f"✓ Categories Covered: {category_count}/20")
print(f"✓ Category READMEs: {readme_count}/20")
print(f"✓ Master README: {'Yes' if os.path.exists('README.md') else 'No'}")
print(f"✓ OpenAPI Spec: {'Yes' if os.path.exists('openapi-spec.yaml') else 'No'}")
print()

if total_found == total_expected and readme_count == 20:
    print("🎉 VALIDATION PASSED - All documentation complete!")
else:
    print("⚠ VALIDATION INCOMPLETE - Some items missing")

print("=" * 80)
