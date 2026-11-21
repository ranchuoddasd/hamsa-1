"""Interactive geographic latency-path visualization prototype.

Uses illustrative coordinates and latency values. This is not live network telemetry.
"""
from pathlib import Path
import folium
from folium.plugins import AntPath
from geopy.distance import geodesic

# Illustrative endpoint and point-of-presence coordinates (Europe).
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
    "London POP B": (51.510, -0.130),  # Illustrative duplicate coordinate
    "Manchester": (53.483, -2.200),
}

# (source, hub, destination, style, segment_latency_ms)
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


def create_map(output_path: str = "latency_path_map.html") -> Path:
    """Render illustrative multi-hop paths to a standalone HTML map."""
    map_view = folium.Map(location=(51.8, 2.5), zoom_start=5, control_scale=True)
    title = """
    <h3 style='position:fixed;top:10px;left:50%;transform:translateX(-50%);
    z-index:999;background:white;padding:10px;border-radius:5px'>
    Geographic Latency Path Visualization
    </h3>
    """
    map_view.get_root().html.add_child(folium.Element(title))

    for source_name, hub_name, destination_name, color, latency in PATHS:
        source = SOURCES[source_name]
        hub = HUBS[hub_name]
        destination = DESTINATIONS[destination_name]
        path = [source, hub, destination]
        total_latency = sum(latency)
        distance_miles = geodesic(source, destination).miles

        folium.PolyLine(path, color=color, weight=3, tooltip=f"{source_name} → {destination_name}").add_to(map_view)
        AntPath(path, delay=400, weight=4, color=color).add_to(map_view)
        folium.Marker(
            destination,
            popup=f"{destination_name}<br>Illustrative latency: {total_latency} ms<br>Distance: {distance_miles:.1f} miles",
            icon=folium.Icon(color="red"),
        ).add_to(map_view)
        folium.Marker(source, popup=f"Source: {source_name}", icon=folium.Icon(color="blue")).add_to(map_view)
        folium.Marker(hub, popup=f"Transit hub: {hub_name}", icon=folium.Icon(color="green")).add_to(map_view)

    output = Path(output_path)
    map_view.save(str(output))
    return output


if __name__ == "__main__":
    result = create_map()
    print(f"Map saved to {result.resolve()}")
