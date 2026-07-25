"""
Configuration for the batch translation pipeline.
Update these values to match your API setup.
"""

# === API Settings ===
API_BASE_URL = "https://your-api.com/api"  # Your API base URL
API_TOKEN = "your-token-here"               # Bearer token for authentication

# === Batch Settings ===
BATCH_SIZE = 30  # Number of titles per batch file

# === Paths (relative to scripts/ directory) ===
DATA_DIR = "data"
BATCHES_DIR = f"{DATA_DIR}/batches"
RESULTS_DIR = f"{DATA_DIR}/results"
