# Assessment 2 – Docker Container Topology Visualizer

## 1. Project Title and Description

### Project Title

**Docker Container Topology Visualizer**

### Description

Docker Compose files can become difficult to understand when there are many services and dependencies. This project is a small web-based tool that takes a Docker Compose YAML file and converts it into a visual representation of the services and their relationships.

The final project will allow the user to view services, basic configuration details and dependencies in an interactive graph.


## 2. Major Components

The project will have three main parts: **UI, Data and Logic**.

### UI

The UI will eventually contain:

* A place to upload the Compose file
* The interactive service graph
* A details panel for the selected service
* An option to export the diagram as an image

### Data

A database is not required for this project.

The Docker Compose file uploaded by the user is the main input data. The file will be read and processed while the application is running. The extracted information will be kept in memory while the graph is being generated.
The project will not permanently store user files or application data.

### Logic

The logic part of the project will:

* Read and validate the YAML file
* Extract services
* Extract basic information such as images, ports, networks and volumes
* Find service dependencies using `depends_on`
* Convert the extracted information into graph nodes and edges
* Handle invalid YAML files


## 3. Architecture

I will use a **simple layered architecture** because the project has a straightforward flow. There is no need for microservices architecture.

```text
                    User
                      |
                      v
             +------------------+
             |       UI         |
             | HTML/CSS/JS      |
             | + Cytoscape.js   |
             +--------+---------+
                      |
                      v
             +------------------+
             |  Flask Backend   |
             +--------+---------+
                      |
                      v
             +------------------+
             |   Logic Layer    |
             |                  |
             | Parser           |
             | Graph Builder    |
             +--------+---------+
                      |
                      v
             +------------------+
             | Docker Compose   |
             |     YAML File    |
             +------------------+
```

The browser will eventually send the uploaded Compose file to the Flask backend. The backend will pass the file to the parser. The parser will extract the required information, and the graph builder will convert it into nodes and edges.

Keeping the parser and graph logic separate from the web code will make the project easier to test and modify.


## 4. Minimal Features for the Next 4 Days

### Deliverable Features

1. Set up the basic project structure
2. Accept a Docker Compose YAML file as input
3. Parse the YAML safely using PyYAML `safe_load`
4. Validate that the file contains a `services` section
5. Extract service names
6. Extract basic service information such as:

   * Image
   * Ports
   * Networks
   * Volumes
   * Dependencies
7. Build graph nodes for the services
8. Build basic graph edges using `depends_on`
9. Write unit tests for the parser and graph builder
10. Produce a working output containing the generated nodes and edges

The first deliverable will **not** require the complete interactive web interface.


## 5. Users Who Can Benefit

The final project can be useful for:

* **Developers** – to understand the structure of a Docker Compose project without reading the complete YAML file.
* **DevOps engineers** – to quickly view service dependencies, ports and other basic configuration.
* **Students** – to understand Docker Compose service relationships visually.
* **Project managers or non-technical users** – to get a simple high-level view of the application structure.


## 6. Components of the First Deliverable

### 1. Compose File Input

Accepts a Docker Compose YAML file or sample YAML content for processing.

### 2. YAML Parser

Reads the YAML file using PyYAML and extracts:

* Services
* Images
* Ports
* Networks
* Volumes
* Dependencies

### 3. Graph Builder

Converts the parsed service information into:

* Nodes representing services
* Edges representing `depends_on` relationships

### 4. Basic Output

Displays or returns the generated graph data so that it can be checked before connecting it to the graphical frontend.

### 5. Unit Tests

Tests the parser and graph builder with valid and invalid input files.

The interactive graph, service details panel and export functionality will be implemented in later deliverables.


## 7. Interfaces of the Components

### Compose File Input

**Input:** Docker Compose YAML file

**Output:** Raw YAML content passed to the parser

---

### Parser

**Input:** Raw YAML content

**Output:** Structured information about the Compose services.

---

### Graph Builder

**Input:** Structured data returned by the parser

**Output:** Graph nodes and edges.

The graph data will later be passed to Cytoscape.js for visualization.

---

### Basic Output

**Input:** Nodes and edges generated by the graph builder

**Output:** A simple representation of the generated graph data for testing and verification.


## 8. Technology Stack

| Area                 | Technology              |
| -------------------- | ----------------------- |
| Programming Language | Python                  |
| Backend              | Flask                   |
| YAML Parsing         | PyYAML                  |
| Frontend             | HTML, CSS, JavaScript   |
| Graph Visualization  | Cytoscape.js            |
| Container Technology | Docker / Docker Compose |
| Version Control      | Git / GitHub            |
| Database             | None                    |

No Docker SDK or database is required.


## 9. Final Project Scope

The final version of the project is planned to provide the following flow:

```text
Docker Compose File
        |
        v
     Parser
        |
        v
  Graph Builder
        |
        v
 Cytoscape.js Graph
        |
        v
 Service Details
        |
        v
    PNG Export
```

### Out of Scope

The following features are outside the scope of the project:

* Kubernetes support
* Docker Swarm support
* Starting, stopping or restarting containers
* User login or authentication
* Database storage
* Merging multiple Compose files
* `.env` file processing
* Advanced Docker management
