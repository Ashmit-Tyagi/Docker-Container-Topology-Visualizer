let services = {};
let cy = null;


const fileInput = document.getElementById("composeFile");
const analyzeButton = document.getElementById("analyzeButton");
const errorMessage = document.getElementById("errorMessage");
const fileName = document.getElementById("fileName");
const serviceCount = document.getElementById("serviceCount");
const details = document.getElementById("details");


fileInput.addEventListener("change", function () {

    if (fileInput.files.length > 0) {
        fileName.textContent =
            "Selected file: " + fileInput.files[0].name;
    }

});


analyzeButton.addEventListener("click", async function () {

    errorMessage.textContent = "";

    if (fileInput.files.length === 0) {
        errorMessage.textContent =
            "Please select a Docker Compose file.";

        return;
    }

    const formData = new FormData();

    formData.append("file", fileInput.files[0]);


    try {

        analyzeButton.disabled = true;
        analyzeButton.textContent = "Analyzing...";


        const response = await fetch("/api/parse", {
            method: "POST",
            body: formData
        });


        const data = await response.json();


        if (!data.success) {
            throw new Error(data.error);
        }


        services = data.services;

        displayGraph(data.graph);

        serviceCount.textContent =
            Object.keys(services).length + " services";

    }
    catch (error) {

        errorMessage.textContent =
            "Error: " + error.message;

    }
    finally {

        analyzeButton.disabled = false;
        analyzeButton.textContent = "Analyze Compose File";

    }

});


function displayGraph(graph) {

    const elements = [];


    graph.nodes.forEach(function (node) {

        elements.push({
            data: {
                id: node.id,
                label: node.label
            }
        });

    });


    graph.edges.forEach(function (edge, index) {

        elements.push({
            data: {
                id: "edge-" + index,
                source: edge.source,
                target: edge.target
            }
        });

    });


    cy = cytoscape({

        container: document.getElementById("cy"),

        elements: elements,

        style: [

            {
                selector: "node",

                style: {
                    "label": "data(label)",
                    "background-color": "#2563eb",
                    "color": "#ffffff",
                    "text-valign": "center",
                    "text-halign": "center",
                    "width": "70px",
                    "height": "70px",
                    "font-size": "13px"
                }

            },

            {
                selector: "edge",

                style: {
                    "width": 2,
                    "line-color": "#6b7280",
                    "target-arrow-color": "#6b7280",
                    "target-arrow-shape": "triangle",
                    "curve-style": "bezier"
                }

            },

            {
                selector: ":selected",

                style: {
                    "background-color": "#16a34a",
                    "line-color": "#16a34a",
                    "target-arrow-color": "#16a34a"
                }

            }

        ],

        layout: {
            name: "breadthfirst",
            directed: true,
            padding: 40,
            spacingFactor: 1.4
        }

    });


    cy.on("tap", "node", function (event) {

        const serviceName = event.target.id();

        showServiceDetails(serviceName);

    });

}


function showServiceDetails(serviceName) {

    const service = services[serviceName];

    if (!service) {
        return;
    }


    details.innerHTML = `

        <div class="detail-item">
            <h3>Service</h3>
            <p>${serviceName}</p>
        </div>

        <div class="detail-item">
            <h3>Image</h3>
            <p>${service.image || "Not specified"}</p>
        </div>

        <div class="detail-item">
            <h3>Ports</h3>
            ${createList(service.ports)}
        </div>

        <div class="detail-item">
            <h3>Networks</h3>
            ${createList(service.networks)}
        </div>

        <div class="detail-item">
            <h3>Volumes</h3>
            ${createList(service.volumes)}
        </div>

        <div class="detail-item">
            <h3>Depends On</h3>
            ${createList(service.depends_on)}
        </div>

    `;
}


function createList(items) {

    if (!items || items.length === 0) {
        return "<p>None</p>";
    }

    return `
        <ul>
            ${items.map(item => `<li>${item}</li>`).join("")}
        </ul>
    `;
}