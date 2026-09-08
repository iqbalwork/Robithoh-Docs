#!/usr/bin/env python3
"""
Robithoh Document Manifest Generator
Generates manifest.json containing metadata and SHA-256 hash for all liturgy markdown documents.
"""

import hashlib
import json
import os
import sys
from datetime import datetime, timezone

DOCS_DIR = os.path.join(os.path.dirname(__file__), "..", "documents")
OUTPUT_FILE = os.path.join(os.path.dirname(__file__), "..", "manifest.json")

# Base URL for static hosting (GitHub Pages or jsDelivr)
# Default points to raw/pages on GitHub
BASE_RAW_URL = "https://raw.githubusercontent.com/iqbalwork/Robithoh-Docs/main/documents/"
BASE_PAGES_URL = "https://iqbalwork.github.io/Robithoh-Docs/documents/"
BASE_JSDELIVR_URL = "https://cdn.jsdelivr.net/gh/iqbalwork/Robithoh-Docs@main/documents/"

def compute_sha256(filepath: str) -> str:
    sha256 = hashlib.sha256()
    with open(filepath, "rb") as f:
        while chunk := f.read(8192):
            sha256.update(chunk)
    return sha256.hexdigest()

def generate_manifest():
    if not os.path.isdir(DOCS_DIR):
        print(f"Error: Documents directory '{DOCS_DIR}' not found.", file=sys.stderr)
        sys.exit(1)

    # Read existing manifest if present to preserve version or track changes
    existing_version = 1
    if os.path.isfile(OUTPUT_FILE):
        try:
            with open(OUTPUT_FILE, "r", encoding="utf-8") as f:
                old_data = json.load(f)
                existing_version = old_data.get("version", 1) + 1
        except Exception:
            existing_version = 1

    documents = []
    files = sorted([f for f in os.listdir(DOCS_DIR) if f.endswith(".md")])

    for filename in files:
        filepath = os.path.join(DOCS_DIR, filename)
        file_hash = compute_sha256(filepath)
        file_size = os.path.getsize(filepath)

        # Generate standard document entry
        documents.append({
            "fileName": filename,
            "sha256": file_hash,
            "size": file_size,
            "url": f"{BASE_RAW_URL}{filename}",
            "rawUrl": f"{BASE_RAW_URL}{filename}",
            "pagesUrl": f"{BASE_PAGES_URL}{filename}"
        })

    manifest = {
        "version": existing_version,
        "updatedAt": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "totalDocuments": len(documents),
        "documents": documents
    }

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print(f"✅ Successfully generated manifest with {len(documents)} documents (Version: {existing_version}) -> {OUTPUT_FILE}")

if __name__ == "__main__":
    generate_manifest()
