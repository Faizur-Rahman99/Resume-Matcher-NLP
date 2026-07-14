#!/bin/bash

set -e

echo "Starting FastAPI..."

uvicorn src.api.app:app \
    --host 0.0.0.0 \
    --port 8000 &

echo "Waiting for FastAPI..."

until python -c "
import requests
import sys
try:
    r = requests.get('http://127.0.0.1:8000/health', timeout=2)
    sys.exit(0 if r.status_code == 200 else 1)
except Exception:
    sys.exit(1)
"
do
    sleep 1
done

echo "FastAPI is ready."

PORT=${PORT:-8501}

echo "Starting Streamlit on port ${PORT}..."

exec streamlit run frontend/app.py \
    --server.address=0.0.0.0 \
    --server.port=${PORT}