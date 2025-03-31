# Pixabay Image Search MCP

A FastMCP service for searching images from Pixabay.

## Setup

1. Clone the repository
2. Install dependencies:
   ```
   pip install -e .
   ```
3. Create a `.env` file in the root directory with your Pixabay API key:
   ```
   PIXABAY_API_KEY=your_api_key_here
   ```

## Usage

Run the server:

```
python server.py
```

The MCP server will be available for AI agents to use for image searching.

## Logging

Logs are saved to the application directory with filename format `app_YYYYMMDD.log`.

## Development

- The `.env` file is excluded from git to protect API keys
- Make sure to install the development dependencies if you plan to contribute

## License

[MIT](LICENSE) 