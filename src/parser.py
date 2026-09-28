import yaml


def parse_compose_file(file_path):
    with open(file_path, "r") as file:
        data = yaml.safe_load(file)

    if not data:
        raise ValueError("The Compose file is empty.")

    if "services" not in data:
        raise ValueError("The Compose file does not contain a services section.")

    services = {}

    for service_name, service_data in data["services"].items():

        depends_on = service_data.get("depends_on", [])

        if isinstance(depends_on, dict):
            depends_on = list(depends_on.keys())

        services[service_name] = {
            "image": service_data.get("image"),
            "ports": service_data.get("ports", []),
            "networks": service_data.get("networks", []),
            "volumes": service_data.get("volumes", []),
            "depends_on": depends_on
        }

    return services