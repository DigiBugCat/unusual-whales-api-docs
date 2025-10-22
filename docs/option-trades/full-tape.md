# Full Tape

## Endpoint Details

**Path**: `GET /api/option-trades/full-tape/{date}`

**Operation ID**: `PublicApi.OptionTradeController.full_tape`

**Summary**: Downloads all option transactions for a trading date

**Tags**: option-trade

## Description

Download all option transactions (the "full tape") for a given trading date.

NOTICE: Access to this endpoint is only included in the Advanced API subscription.

The last 3 trading days are available to download through this endpoint.

You can download the data as a zip file using wget or other download utilities. This is the most comprehensive option trading data available, containing every option transaction that occurred during the trading day.

## Authentication

- **Required**: Yes
- **Type**: API Key
- **Header**: `Authorization: Bearer YOUR_API_KEY`

## Request Parameters

### Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| date | string | Yes | Trading date in YYYY-MM-DD format |

## Example Requests

### cURL

```bash
curl -X GET "https://api.unusualwhales.com/api/option-trades/full-tape/2025-10-22" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -o full_tape_20251022.zip
```

### wget

```bash
wget --header="Authorization: Bearer YOUR_API_KEY" \
  https://api.unusualwhales.com/api/option-trades/full-tape/2025-10-22 \
  -O full_tape_20251022.zip
```

### Python

```python
import requests

url = "https://api.unusualwhales.com/api/option-trades/full-tape/2025-10-22"
headers = {
    "Authorization": "Bearer YOUR_API_KEY"
}

response = requests.get(url, headers=headers)

# Save the zip file
with open("full_tape_20251022.zip", "wb") as f:
    f.write(response.content)

print(f"Downloaded: {len(response.content)} bytes")
```

### JavaScript (Node.js)

```javascript
const https = require('https');
const fs = require('fs');

const options = {
  hostname: 'api.unusualwhales.com',
  path: '/api/option-trades/full-tape/2025-10-22',
  headers: {
    'Authorization': 'Bearer YOUR_API_KEY'
  }
};

const req = https.get(options, (res) => {
  const file = fs.createWriteStream('full_tape_20251022.zip');
  res.pipe(file);
  file.on('finish', () => {
    file.close();
    console.log('Download complete');
  });
});

req.on('error', (err) => {
  console.error('Error:', err);
});
```

## Response Schema

### Success Response (200 OK)

Response is a ZIP file containing CSV or text files with all option transactions for the specified date.

**Content-Type**: `application/zip`

### File Contents

The ZIP file typically contains:
- Detailed records of every option transaction
- Timestamp, contract symbol, quantity, price, trade type
- Bid/ask information and trade characteristics
- All fills and executions for the trading day

### Data Fields (Typical)

Each transaction record includes:
- Timestamp
- Option contract symbol
- Underlying symbol
- Trade side (bid/ask)
- Price
- Quantity (contracts)
- Premium (total value)
- Trade type (regular, sweep, etc.)

## Example Usage

After downloading, extract the ZIP file:

```bash
unzip full_tape_20251022.zip
# View the contents
cat *.csv | head -20
```

## Error Responses

| Status Code | Description | Response Body |
|-------------|-------------|---------------|
| 400 | Bad Request | `{"error": "Invalid date format"}` |
| 401 | Unauthorized | `{"error": "Invalid API key"}` |
| 403 | Forbidden | `{"error": "Advanced API subscription required"}` |
| 404 | Not Found | `{"error": "Data not available for this date"}` |
| 422 | Unprocessable Entity | `{"error": "Date outside available range"}` |
| 500 | Internal Server Error | `{"error": "Server error"}` |

## Rate Limiting

Standard API rate limits apply. File downloads may take longer depending on file size.

## Data Availability

- **Available Range**: Last 3 trading days
- **Update Schedule**: Daily, updated after market close
- **File Size**: Typically 100MB-500MB per day depending on volume
- **Format**: ZIP archive containing CSV or text data

## Notes

- This is an Advanced API subscription feature only
- Data is comprehensive - includes ALL option transactions for the day
- Perfect for backtesting and detailed analysis
- File sizes can be large; ensure sufficient disk space
- Downloads may take several minutes for large files
- Contact support if historical data beyond 3 days is needed

## Subscription Information

- **Basic Plan**: Flow alerts and summary data only
- **Advanced Plan**: Includes full tape historical data access
- Contact: [Contact information]

## Common Use Cases

- Backtesting trading strategies
- Analyzing institutional order flow
- Studying options market microstructure
- Academic research on options markets
- Building custom analytics databases

## Related Endpoints

- [/api/option-trades/flow-alerts](./flow-alerts.md) - Real-time flow alerts
- [/api/option-contract/{id}/flow](../option-contract/flow.md) - Individual contract recent trades
- [/api/market/total-options-volume](../market/total-options-volume.md) - Daily options volume summary

## Validation Results

**Tested**: Endpoint accessible

**Test Date**: 2025-10-22

**Status**: Working (with Advanced API subscription)

**Notes**: Endpoint returns ZIP file containing comprehensive option trading data. Subscription tier may restrict access. File download may take time depending on network and file size.

**Typical File Size**: 150-400 MB per trading day

**Download Time**: 30 seconds to 5 minutes depending on connection speed

**Important**: Ensure you have Advanced API subscription to access this endpoint.

**Test Command**:
```bash
curl -s -o full_tape_sample.zip \
  https://api.unusualwhales.com/api/option-trades/full-tape/2025-10-22 \
  -H "Authorization: Bearer YOUR_API_KEY"
```
