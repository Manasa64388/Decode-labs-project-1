const API_URL = "http://127.0.0.1:5000/api/projects";

const projectForm = document.getElementById("projectForm");
const projectName = document.getElementById("projectName");
const technology = document.getElementById("technology");
const projectList = document.getElementById("projectList");
const message = document.getElementById("message");

// Display projects in the DOM
function displayProjects(projects) {

    projectList.innerHTML = "";

    if (projects.length === 0) {
        projectList.innerHTML = "<p>No projects available.</p>";
        return;
    }

    projects.forEach(project => {

        const projectElement = document.createElement("div");

        projectElement.className = "project";

        projectElement.innerHTML = `
            <h3>${project.name}</h3>
            <p>Technology: ${project.technology}</p>

            <button
                class="edit-btn"
                onclick="editProject(${project.id})">
                Edit
            </button>

            <button
                class="delete-btn"
                onclick="deleteProject(${project.id})">
                Delete
            </button>
        `;

        projectList.appendChild(projectElement);

    });
}


// POST — Add a project
projectForm.addEventListener("submit", async function(event) {

    event.preventDefault();

    const name = projectName.value.trim();
    const tech = technology.value.trim();

    if (!name || !tech) {
        message.textContent = "Please fill in all fields.";
        return;
    }

    try {

        const response = await fetch(API_URL, {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                name: name,
                technology: tech
            })

        });

        if (!response.ok) {
            throw new Error(`HTTP Error: ${response.status}`);
        }

        await response.json();

        message.textContent = "Project added successfully.";

        projectForm.reset();

        await loadProjects();

    } catch (error) {

        message.textContent = "Failed to add project.";

        console.error(error);

    }

});


// PUT — Update a project
async function editProject(id) {

    const newName = prompt("Enter new project name:");
    const newTechnology = prompt("Enter new technology:");

    if (!newName || !newTechnology) {
        return;
    }

    try {

        const response = await fetch(`${API_URL}/${id}`, {

            method: "PUT",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                name: newName,
                technology: newTechnology
            })

        });

        if (!response.ok) {
            throw new Error(`HTTP Error: ${response.status}`);
        }

        await response.json();

        message.textContent = "Project updated successfully.";

        await loadProjects();

    } catch (error) {

        message.textContent = "Failed to update project.";

        console.error(error);

    }

}


// DELETE — Delete a project
async function deleteProject(id) {

    const confirmed = confirm(
        "Are you sure you want to delete this project?"
    );

    if (!confirmed) {
        return;
    }

    try {

        const response = await fetch(`${API_URL}/${id}`, {

            method: "DELETE"

        });

        if (!response.ok) {
            throw new Error(`HTTP Error: ${response.status}`);
        }

        await response.json();

        message.textContent = "Project deleted successfully.";

        await loadProjects();

    } catch (error) {

        message.textContent = "Failed to delete project.";

        console.error(error);

    }

}


// Load projects when page opens
async function loadProjects() {

    try {

        message.textContent = "Loading projects...";

        const response = await fetch(API_URL);

        if (!response.ok) {
            throw new Error(`HTTP Error: ${response.status}`);
        }

        const projects = await response.json();

        displayProjects(projects);

        message.textContent = "";

    } catch (error) {

        message.textContent = "Failed to load projects.";

        console.error(error);

    }
}