#!/usr/bin/env python3
"""
Simple Sanic service that reports the CUDA version line from `nvcc --version`
and exposes a /ping health-check endpoint.

RunPod sets the PORT env var for serverless containers; we bind to it so the
ingress can reach the process.
"""

import os
import asyncio
import subprocess
from sanic import Sanic
from sanic.response import text

app = Sanic("cuda_version_service")


@app.get("/ping")
async def ping(request):
    """Health-check route: always returns HTTP 200."""
    return text("pong\n", status=200)


@app.get("/")
async def cuda_version(request):
    """Return CUDA version (the 4th line from `nvcc --version`)."""
    # Simulate a long-running job
    await asyncio.sleep(10)

    # This log should be visible in sls-local-server
    print("this is a log that should be captured by sls-local-server")

    # Run nvcc without blocking the event loop
    loop = asyncio.get_running_loop()
    raw = await loop.run_in_executor(
        None, subprocess.check_output, ["nvcc", "--version"]
    )

    line = raw.decode("utf-8").split("\n")[3]  # same slice as your original code
    return text(line + "\n")


if __name__ == "__main__":
    # Default to 8080 when testing locally
    port = int(os.getenv("PORT", 8080))
    app.run(host="0.0.0.0", port=port, access_log=True)
