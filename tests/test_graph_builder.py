from src.graph_builder import build_graph


def test_graph_nodes():
    services = {
        "web": {
            "image": "nginx",
            "ports": [],
            "networks": [],
            "volumes": [],
            "depends_on": ["db"]
        },
        "db": {
            "image": "postgres",
            "ports": [],
            "networks": [],
            "volumes": [],
            "depends_on": []
        }
    }

    graph = build_graph(services)

    assert len(graph["nodes"]) == 2
    assert graph["nodes"][0]["id"] == "web"
    assert graph["nodes"][1]["id"] == "db"


def test_graph_edges():
    services = {
        "web": {
            "image": "nginx",
            "ports": [],
            "networks": [],
            "volumes": [],
            "depends_on": ["db"]
        },
        "db": {
            "image": "postgres",
            "ports": [],
            "networks": [],
            "volumes": [],
            "depends_on": []
        }
    }

    graph = build_graph(services)

    assert len(graph["edges"]) == 1
    assert graph["edges"][0]["source"] == "web"
    assert graph["edges"][0]["target"] == "db"