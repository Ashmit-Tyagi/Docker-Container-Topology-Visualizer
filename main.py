import json

from src.parser import parse_compose_file
from src.graph_builder import build_graph


file_path = "sample/docker-compose.yml"

services = parse_compose_file(file_path)

graph = build_graph(services)

print("Services:")
for service_name, service_data in services.items():
    print(f"\n{service_name}")
    print(f"  Image: {service_data['image']}")
    print(f"  Ports: {service_data['ports']}")
    print(f"  Networks: {service_data['networks']}")
    print(f"  Volumes: {service_data['volumes']}")
    print(f"  Depends on: {service_data['depends_on']}")

print("\nGraph:")
print(json.dumps(graph, indent=4))