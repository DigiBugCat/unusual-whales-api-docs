# FDA Calendar

## Endpoint Details

**Path**: `GET /api/market/fda-calendar`

**Operation ID**: `PublicApi.MarketController.fda_calendar`

**Summary**: Returns FDA calendar events and drug approval information

**Tags**: market

## Description

Returns FDA calendar data with filtering options. The FDA calendar contains information about:
- PDUFA (Prescription Drug User Fee Act) dates
- Advisory Committee Meetings
- FDA Decisions
- Clinical Trial Results
- New Drug Applications
- Biologics License Applications

The target_date parameters support various FDA-specific date formats for flexibility in querying.

## Authentication

- **Required**: Yes
- **Type**: API Key
- **Header**: `Authorization: Bearer YOUR_API_KEY`

## Request Parameters

### Query Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| announced_date_min | string | No | null | Minimum announced date in YYYY-MM-DD format |
| announced_date_max | string | No | null | Maximum announced date in YYYY-MM-DD format |
| target_date_min | string | No | null | Minimum target date (supports Q1-Q4, H1-H2, MID, LATE formats) |
| target_date_max | string | No | null | Maximum target date (supports Q1-Q4, H1-H2, MID, LATE formats) |
| drug | string | No | null | Filter by drug name (partial match supported) |
| ticker | string | No | null | Filter by company ticker symbol |
| limit | integer | No | 100 | Maximum number of results (max: 200, min: 1) |

### Date Format Support

The target_date parameters support various FDA-specific date formats:
- Quarters: YYYY-Q[1-4] (e.g. 2024-Q1, 2025-Q3)
- Half years: YYYY-H[1-2] (e.g. 2024-H1, 2025-H2)
- Mid-year: YYYY-MID (e.g. 2024-MID, 2025-MID)
- Late-year: YYYY-LATE (e.g. 2024-LATE, 2025-LATE)
- Standard dates: YYYY-MM-DD

## Example Requests

### cURL

```bash
curl -X GET "https://api.unusualwhales.com/api/market/fda-calendar?limit=5" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

Filter by ticker:
```bash
curl -X GET "https://api.unusualwhales.com/api/market/fda-calendar?ticker=AMGN&limit=10" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

Filter by target date quarter:
```bash
curl -X GET "https://api.unusualwhales.com/api/market/fda-calendar?target_date_min=2025-Q1&target_date_max=2025-Q4" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

### Python

```python
import requests

url = "https://api.unusualwhales.com/api/market/fda-calendar"
headers = {
    "Authorization": "Bearer YOUR_API_KEY"
}
params = {
    "limit": 5,
    "ticker": "GERN"
}

response = requests.get(url, headers=headers, params=params)
data = response.json()
print(data)
```

### JavaScript (Fetch)

```javascript
const url = "https://api.unusualwhales.com/api/market/fda-calendar?limit=5";
const options = {
  method: 'GET',
  headers: {
    'Authorization': 'Bearer YOUR_API_KEY'
  }
};

fetch(url, options)
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));
```

## Response Schema

### Success Response (200 OK)

```json
{
  "data": [
    {
      "ticker": "string",
      "drug": "string",
      "indication": "string",
      "status": "string",
      "event_type": "string",
      "target_date": "string",
      "announcement_date": "string",
      "description": "string",
      "outcome": "string",
      "source_type": "string",
      "marketcap": "string",
      "has_options": "boolean"
    }
  ]
}
```

### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| ticker | string | Company stock ticker symbol |
| drug | string | Drug name or codename |
| indication | string | Medical indication the drug targets |
| status | string | Development status (e.g., Phase 1, Phase 2, Phase 3) |
| event_type | string | Type of FDA event (PDUFA, Advisory Committee, Decision, etc.) |
| target_date | string | Expected FDA decision date |
| announcement_date | string | When the event was announced |
| description | string | Detailed description of the event |
| outcome | string | Outcome or progress of the trial/application |
| source_type | string | Source of information (Press Release, SEC Filing, etc.) |
| marketcap | string | Company market capitalization |
| has_options | boolean | Whether the company has listed options |

## Example Response

```json
{
  "data": [
    {
      "status": "Phase 3",
      "time": "07:44:07",
      "description": "Geron Announces First Patient Dosed in IMpactMF Phase 3 Clinical Trial in Refractory Myelofibrosis",
      "ticker": "GERN",
      "created_at": "2021-04-13T13:22:07Z",
      "event_type": "Top-line Data Due",
      "updated_at": "2021-04-13T13:23:09Z",
      "outcome": "Final analysis from the trial are expected in 2025",
      "source_type": "Press Release",
      "start_date": "2021-04-13",
      "end_date": null,
      "has_options": true,
      "marketcap": "810281683",
      "notes": "Geron Announces First Patient Dosed in IMpactMF Phase 3 Clinical Trial",
      "target_date": "2025-MID",
      "drug": "Imetelstat (IMpactMF)",
      "indication": "Refractory Myelofibrosis (MF)"
    }
  ]
}
```

## Error Responses

| Status Code | Description | Response Body |
|-------------|-------------|---------------|
| 400 | Bad Request | `{"error": "Invalid date format"}` |
| 401 | Unauthorized | `{"error": "Invalid API key"}` |
| 422 | Unprocessable Entity | `{"error": "Invalid parameters"}` |
| 500 | Internal Server Error | `{"error": "Server error"}` |

## Rate Limiting

Standard API rate limits apply.

## Notes

- FDA events can serve as significant catalysts for biotech and pharmaceutical stocks
- The calendar includes both positive outcomes (approvals) and negative outcomes (rejections)
- Some events may have multi-month or quarterly windows (Q1, H1, MID, LATE formats)
- Not all companies with FDA events have options available - check `has_options` field
- Market cap can help filter for micro-cap vs larger pharma companies
- Source type indicates how reliable the information is
- This endpoint is useful for traders interested in biotech catalysts and event-driven strategies

## Related Endpoints

- [/api/market/economic-calendar](./economic-calendar.md) - Broader economic events calendar
- [/api/market/top-net-impact](./top-net-impact.md) - Stocks with highest options activity
- [/api/screener/option-contracts](../screener/option-contracts.md) - Option contract screener

## Validation Results

**Tested**: Yes

**Test Date**: 2025-10-22

**Status**: Working

**Notes**: Endpoint returns comprehensive FDA calendar data with various event types, development stages, and target dates in multiple formats.

**Response Time**: < 1 second

**Sample Events Include**:
- Phase 3 trials with mid-year targets
- Phase 2b data presentations
- PDUFA date announcements

**Test Command**:
```bash
curl -s "https://api.unusualwhales.com/api/market/fda-calendar?limit=5" \
  -H "Authorization: Bearer 5d1ec006-49f0-4a2a-90ae-5176c72425e3"
```
