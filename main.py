"""Interactive geographic latency-path visualization prototype.

All locations and latency values are illustrative. This is not live telemetry.
"""
from pathlib import Path

import folium
from folium.plugins import AntPath
from geopy.distance import geodesic

# Synthetic example locations. Do not replace these with private topology data
# in a public repository.
SOURCES = {
    "Source A": (51.507, -0.589),
    "Source B": (51.127, -0.016),
}
HUBS = {
    "UK South": (51.520, -0.098),
    "Amsterdam": (52.370, 4.895),
    "Frankfurt": (50.110, 8.682),
}
DESTINATIONS = {
    "London POP A": (51.510, -0.130),
    "London POP B": (51.510, -0.130),
    "Manchester": (53.483, -2.200),
}

# (source, transit hub, destination, line color, per-hop latency in ms)
PATHS = [
    ("Source A", "UK South", "London POP A", "blue", (12, 8)),
    ("Source A", "Amsterdam", "London POP A", "green", (20, 12)),
    ("Source A", "Frankfurt", "London POP A", "orange", (20, 12)),
    ("Source A", "UK South", "Manchester", "pink", (12, 8)),
    ("Source A", "Amsterdam", "Manchester", "brown", (20, 12)),
    ("Source A", "Frankfurt", "Manchester", "red", (20, 12)),
    ("Source B", "UK South", "London POP B", "blue", (22, 8)),
    ("Source B", "UK South", "London POP B", "green", (22, 12)),
    ("Source B", "UK South", "London POP B", "orange", (12, 12)),
    ("Source B", "UK South", "Manchester", "pink", (12, 12)),
    ("Source B", "Amsterdam", "Manchester", "brown", (20, 12)),
    ("Source B", "Frankfurt", "Manchester", "red", (20, 12)),
]


def _add_location_markers(map_view: folium.Map) -> None:
    """Add each synthetic endpoint and transit hub once."""
    for name, coordinates in SOURCES.items():
        folium.Marker(
            coordinates,
            tooltip=f"Source: {name}",
            icon=folium.Icon(color="blue", icon="upload"),
        ).add_to(map_view)

    for name, coordinates in HUBS.items():
        folium.Marker(
            coordinates,
            tooltip=f"Transit hub: {name}",
            icon=folium.Icon(color="green", icon="cloud"),
        ).add_to(map_view)

    for name, coordinates in DESTINATIONS.items():
        folium.Marker(
            coordinates,
            tooltip=f"Destination: {name}",
            icon=folium.Icon(color="red", icon="flag"),
        ).add_to(map_view)


def create_map(output_path: str = "latency_path_map.html") -> Path:
    """Render sample multi-hop routes and illustrative latency values."""
    map_view = folium.Map(
        location=(51.8, 2.5),
        zoom_start=5,
        control_scale=True,
    )
    title = """
    <div style="position:fixed;top:10px;left:50%;transform:translateX(-50%);
    z-index:999;background:white;padding:10px;border-radius:5px">
      <strong>Geographic Latency Path Visualization</strong><br>
      <small>Illustrative sample data — not live measurements</small>
    </div>
    """
    map_view.get_root().html.add_child(folium.Element(title))
    _add_location_markers(map_view)

    for source_name, hub_name, destination_name, color, hop_latency in PATHS:
        source = SOURCES[source_name]
        hub = HUBS[hub_name]
        destination = DESTINATIONS[destination_name]
        route = [source, hub, destination]

        total_latency_ms = sum(hop_latency)
        route_distance_miles = sum(
            geodesic(route[index], route[index + 1]).miles
            for index in range(len(route) - 1)
        )
        tooltip = (
            f"{source_name} → {hub_name} → {destination_name} | "
            f"Illustrative latency: {total_latency_ms} ms"
        )

        folium.PolyLine(
            route,
            color=color,
            weight=3,
            opacity=0.8,
            tooltip=tooltip,
        ).add_to(map_view)
        AntPath(
            route,
            delay=400,
            weight=4,
            color=color,
            opacity=0.7,
        ).add_to(map_view)

        folium.Tooltip(
            f"{total_latency_ms} ms · {route_distance_miles:.1f} miles",
            sticky=True,
        ).add_to(
            folium.PolyLine(
                route,
                color=color,
                weight=0,
                opacity=0,
            ).add_to(map_view)
        )

    output = Path(output_path)
    map_view.save(str(output))
    return output


if __name__ == "__main__":
    generated_map = create_map()
    print(f"Map saved to {generated_map.resolve()}")
