def build_graph(services):
    nodes = []
    edges = []

    for service_name in services:
        nodes.append({
            "id": service_name,
            "label": service_name
        })

    for service_name, service_data in services.items():
        for dependency in service_data["depends_on"]:
            edges.append({
                "source": service_name,
                "target": dependency
            })

    return {
        "nodes": nodes,
        "edges": edges
    }