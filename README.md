# edgecore-vibecode

This is a repo for EdgeCore vibecoding!

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <repo-url>
   cd edgecore-vibecode
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment variables**
   - Copy the example environment file:
     ```bash
     cp .env.example .env
     ```
   - Open `.env` and set your values for:
     - `NOCODB_API_TOKEN` (your NocoDB API token)
     - `NOCODB_TABLE_ID` (your NocoDB table ID)

4. **Run the script**
   ```bash
   export $(cat .env | xargs)
   python main.py
   ```

## .env.example

```
NOCODB_API_TOKEN=your_nocodb_api_token_here
NOCODB_TABLE_ID=your_nocodb_table_id_here
```

## Notes

- Never commit your real `.env` file or API tokens to version control.
- The script will print a user-friendly error if required environment variables
  are missing.
