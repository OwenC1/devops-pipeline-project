
const taskForm = document.getElementById("task-form");
const taskInput = document.getElementById("task-input");
const taskList = document.getElementById("task-list");
const message = document.getElementById("message");

// Retrieve tasks from our FastAPI backend
async function loadTasks() {
    try {
        const response = await fetch("/tasks");

        if (!response.ok) {
            throw new Error("Failed to load tasks");
        }

        const tasks = await response.json();

        taskList.innerHTML = "";

        for (const task of tasks) {
            const listItem = document.createElement("li");
            listItem.textContent = task.title;
            taskList.appendChild(listItem);
        }

        message.textContent = "";
    } catch (error) {
        message.textContent = error.message;
    }
}

// Send a new task to the backend
taskForm.addEventListener("submit", async (event) => {
    event.preventDefault();

    const title = taskInput.value.trim();

    if (!title) {
        return;
    }

    try {
        const response = await fetch("/tasks", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ title: title })
        });

        if (!response.ok) {
            throw new Error("Failed to add task");
        }

        taskInput.value = "";
        await loadTasks();
    } catch (error) {
        message.textContent = error.message;
    }
});

// Load existing tasks when the page opens
loadTasks();
