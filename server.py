#!/usr/bin/env python3
"""
Custom ADK Server that bypasses OpenAPI schema generation issues
"""
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
import uvicorn

# Import our agent
from agents.agent import root_agent

# Create FastAPI app with custom configuration
app = FastAPI(
    title="GitHub Agent API",
    description="A simple API server for the GitHub agent",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url=None  # Disable automatic OpenAPI generation
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", response_class=HTMLResponse)
async def root():
    return """
    <html>
        <head>
            <title>GitHub Agent API</title>
        </head>
        <body>
            <h1>GitHub Agent API Server</h1>
            <p>The server is running successfully!</p>
            <ul>
                <li><a href="/docs">API Documentation (Swagger UI)</a></li>
                <li><a href="/health">Health Check</a></li>
            </ul>
        </body>
    </html>
    """

@app.get("/health")
async def health_check():
    return {"status": "healthy", "agent": root_agent.name}

@app.get("/docs", response_class=HTMLResponse)
async def docs():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>GitHub Agent API Documentation</title>
        <link type="text/css" rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui.css">
    </head>
    <body>
        <div id="swagger-ui">
        </div>
        <script src="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui-bundle.js"></script>
        <script>
        const ui = SwaggerUIBundle({
            url: '/openapi.json',
            dom_id: '#swagger-ui',
            presets: [
                SwaggerUIBundle.presets.apis,
                SwaggerUIBundle.SwaggerUIStandalonePreset
            ],
        })
        </script>
    </body>
    </html>
    """

@app.get("/openapi.json")
async def openapi_spec():
    """Return a basic OpenAPI spec"""
    return {
        "openapi": "3.0.0",
        "info": {
            "title": "GitHub Agent API",
            "version": "1.0.0",
            "description": "API for GitHub agent operations"
        },
        "paths": {
            "/": {
                "get": {
                    "summary": "Root endpoint",
                    "responses": {
                        "200": {"description": "Welcome message"}
                    }
                }
            },
            "/health": {
                "get": {
                    "summary": "Health check",
                    "responses": {
                        "200": {"description": "Server is healthy"}
                    }
                }
            }
        }
    }

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
