# Prototype Notes

## Purpose
Explore how geographic network paths, transit hubs and latency annotations can be presented in an interactive map.

## Current implementation
- `main.py` defines synthetic topology, illustrative paths and sample per-hop latency.
- Folium renders the map and route overlays.
- Geopy calculates approximate geodesic distance for each route hop.
- `requirements.txt` declares the Python dependencies.

## Standardization changes
- Route distance is calculated as the sum of the displayed hops rather than a direct source-to-destination line.
- Source, hub and destination markers are added once instead of being repeated for every route.
- The map explicitly labels all values as illustrative and not live measurements.
- Route data and rendering responsibilities are documented.

## Known limitations
- No real measurement or telemetry collection.
- No JSON/CSV input interface yet.
- No automated tests or CI workflow.
- Some destination examples intentionally share coordinates.
- Geographic distance does not represent actual network path length.

## Next steps
1. Add a validated input schema for measured paths.
2. Include measurement timestamp, method and source.
3. Separate data parsing from visualization.
4. Add unit tests for coordinate and route validation.
5. Keep synthetic data in the public demonstration.
