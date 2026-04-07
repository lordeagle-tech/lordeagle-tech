# Gifted Maurice - GitHub Profile Page

## Project Overview
A static HTML page that renders the GitHub profile README of Gifted Maurice (mauricegift) as a web page. Originally a GitHub profile README, converted to a simple static website.

## Architecture
- **Type**: Static HTML website
- **Server**: Python `http.server` (SimpleHTTPRequestHandler)
- **Port**: 5000 (0.0.0.0)
- **Entry point**: `index.html`

## Key Files
- `index.html` - Main HTML page rendering the profile content
- `serve.py` - Simple Python HTTP server
- `README.md` - Original GitHub profile README (source content)

## Running the Project
The workflow "Start application" runs `python serve.py` which serves `index.html` on port 5000.

## Deployment
Configured as a static site deployment.
