# Docker-Container-Topology-Visualizer

A web-based tool that visualizes the topology and dependencies of services defined in a Docker Compose file.
The project accepts a Docker Compose YAML file, parses the services and their configurations, builds a service dependency graph, and displays the topology interactively.

## Features

* Upload a Docker Compose `.yml` or `.yaml` file
* Parse Docker Compose services using PyYAML
* Extract:
  * Service names
  * Docker images
  * Ports
  * Networks
  * Volumes
  * Service dependencies
* Generate a graph containing services and dependency relationships
* Display the topology
* Click a service to view its details
* Display the number of services and dependencies
* Reset the visualization
* Handle invalid files and invalid Compose structures
* Automated testing using pytest

## Project Structure

```text
Docker-Container-Topology-Visualizer/
│
├── src/
│   ├── __init__.py
│   ├── parser.py
│   └── graph_builder.py
│
├── tests/
│   ├── __init__.py
│   ├── test_parser.py
│   ├── test_graph_builder.py
│   └── test_app.py
│
├── sample/
│   └── docker-compose.yml
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
├── output/
│
├── app.py
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

## How the Application Works

The application follows this flow:

```text
Docker Compose YAML
        ↓
      Flask
        ↓
     parser.py
        ↓
  Parsed service data
        ↓
 graph_builder.py
        ↓
    Graph JSON
        ↓
   Cytoscape.js
        ↓
 Interactive topology
        ↓
  Service details
```

### 1. File Upload

The user selects a Docker Compose YAML file from the web interface.

Flask receives the uploaded file through the `/api/parse` endpoint.

### 2. YAML Parsing

`src/parser.py` uses PyYAML to safely read the Compose file.

It validates that:

* The file is not empty
* The YAML format is valid
* A `services` section exists
* Service definitions are valid

The parser extracts the important information for every service.

### 3. Graph Construction

`src/graph_builder.py` converts the parsed services into a graph.

Each service becomes a **node**.

Each `depends_on` relationship becomes a directed **edge**.

For example:

```text
web → backend → db
```

means that `web` depends on `backend`, and `backend` depends on `db`.

### 4. Visualization

The Flask backend returns the parsed information and graph as JSON.
The frontend uses Cytoscape.js to display the graph interactively.

Users can click a service node to see its:

* Image
* Ports
* Networks
* Volumes
* Dependencies

## Technologies Used

* **Python** - Application and backend logic
* **Flask** - Web server and API
* **PyYAML** - Docker Compose YAML parsing
* **HTML** - Frontend structure
* **CSS** - Frontend styling
* **JavaScript** - Frontend interaction
* **Cytoscape.js** - Graph visualization
* **pytest** - Automated testing
* **Git/GitHub** - Version control

## Testing

The project uses pytest for automated testing.
The current test suite contains tests for:

### Parser

* Valid Compose files
* Empty files
* Missing `services` section
* Invalid service configuration

### Graph Builder

* Correct number of graph nodes
* Correct dependency edges

### Flask Application

* Home page
* Valid Compose file upload
* Upload without a file
* Invalid Compose file


## Key Learnings

### 1. YAML Parsing

Learned how to use PyYAML to read structured configuration files and extract required information.

### 2. Graph Representation

Learned how service dependencies can be represented using graph nodes and directed edges.

### 3. Backend and Frontend Integration

Learned how Flask can receive an uploaded file, process it using Python code, and return JSON data to the frontend.

### 4. Interactive Visualization

Learned how Cytoscape.js can be used to convert graph data into an interactive service topology.

### 5. Error Handling

Implemented validation for invalid files, missing files, invalid YAML, and missing Compose service definitions.

### 6. Testing

Learned how to test individual Python modules as well as Flask API endpoints using pytest.

### 7. Modular Development

Separated parsing, graph construction, backend routing, frontend logic, and testing into different files so that each part has a clear responsibility.

## Current End-to-End Feature

The main implemented feature is:

> **Docker Compose upload → parsing → graph generation → interactive topology visualization → service details**

This feature has been implemented from the user interface through the backend/business logic to the final visualization and has been tested using automated tests.
