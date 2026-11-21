# Network Latency Visualizer

An interactive geographic visualization experiment for illustrating network paths, transit hubs, endpoint locations, and latency annotations on a map.

**Status:** Prototype using illustrative coordinates and static latency values. It does not measure real network performance.

## Features
- Geographic source, transit, and destination markers.
- Multi-hop path rendering with animated overlays.
- Latency annotations and geodesic distance calculation.
- Standalone HTML map output.

## Implementation
- Python
- Folium
- Geopy
- Folium AntPath plugin

## Run locally
```bash
python -m pip install -r requirements.txt
python main.py
```
The script writes `latency_path_map.html`. Open the generated file in a browser.

## Repository files
- `main.py` — map creation, sample topology, latency values, and HTML output.
- `requirements.txt` — Python dependencies.

## Limitations
- Coordinates and latency values are illustrative and static.
- Several example destination points share coordinates.
- The visualization is not a traceroute, telemetry collection, or latency measurement tool.
- Path color and marker placement are for demonstration only.

## Roadmap
- Accept path data from JSON or CSV.
- Add real measurement input and timestamps.
- Separate topology data from rendering code.
- Add validation and tests for input data.

## Security and data handling
Use anonymized example locations and topology in public demonstrations. Do not add private network paths, customer circuits, or confidential location data.

## License
No license is currently provided. Until one is added, reuse and redistribution are not granted by default.
