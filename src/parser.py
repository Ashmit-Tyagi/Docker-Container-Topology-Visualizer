import yaml


def parse_compose_file(file_path):

    try:
        with open(file_path, "r") as file:
            data = yaml.safe_load(file)
    except yaml.YAMLError:
        raise ValueError("Invalid YAML format.")
    except OSError:
        raise ValueError("Could not read the Compose file.")

    if not data:
        raise ValueError("The Compose file is empty.")

    if "services" not in data:
        raise ValueError(
            "The Compose file does not contain a services section."
        )

    if not isinstance(data["services"], dict):
        raise ValueError(
            "The services section must contain service definitions."
        )

    services = {}

    for service_name, service_data in data["services"].items():

        if not isinstance(service_data, dict):
            raise ValueError(
                f"Invalid configuration for service: {service_name}"
            )

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