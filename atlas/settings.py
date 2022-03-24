import os
import warnings

ALGOLIA_APPLICATION_ID = os.environ.get("ALGOLIA_APPLICATION_ID", "")
ALGOLIA_API_KEY = os.environ.get("ALGOLIA_API_KEY", "")
ALGOLIA_INDEX_NAME = os.environ.get("ALGOLIA_INDEX_NAME", "")

if not ALGOLIA_APPLICATION_ID:
    warnings.warn("ALGOLIA_APPLICATION_ID environment variable is not set")

if not ALGOLIA_API_KEY:
    warnings.warn("ALGOLIA_API_KEY environment variable is not set")