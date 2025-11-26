let tasks = []; // store user-added tasks

function addTask() {
    let title = document.getElementById("title").value;
    let due = document.getElementById("due_date").value;
    let hours = document.getElementById("hours").value;
    let importance = document.getElementById("importance").value;
    let deps = document.getElementById("deps").value;

    if (!title || !due || !hours || !importance) {
        alert("Please fill all fields");
        return;
    }

    let depArray = deps ? deps.split(",").map(i => parseInt(i.trim())) : [];

    tasks.push({
        title: title,
        due_date: due,
        estimated_hours: parseFloat(hours),
        importance: parseInt(importance),
        dependencies: depArray
    });

    alert("Task added!");
}

function analyzeTasks() {
    let jsonText = document.getElementById("jsonInput").value.trim();

    let finalTasks = tasks;

    if (jsonText.length > 0) {
        try {
            finalTasks = JSON.parse(jsonText);
        } catch (e) {
            alert("Invalid JSON");
            return;
        }
    }

    fetch("http://127.0.0.1:9000/api/tasks/analyze/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(finalTasks)
    })
    .then(res => res.json())
    .then(data => displayResults(data))
    .catch(err => alert("Error connecting to backend"));
}

function displayResults(data) {
    let box = document.getElementById("results");
    box.innerHTML = "";

    data.forEach((task, index) => {
        box.innerHTML += `
            <div class='result-item'>
                <h3>${index + 1}. ${task.title}</h3>
                <p><b>Score:</b> ${task.score}</p>
                <p><b>Due Date:</b> ${task.due_date}</p>
                <p><b>Importance:</b> ${task.importance}</p>
                <p><b>Hours:</b> ${task.estimated_hours}</p>
                <p><b>Explanation:</b> ${task.explanation}</p>
            </div>
        `;
    });
}

function fetchSuggestedTasks() {
    // Show the floating note
    showFloatingNote();

    // Fetch the suggested tasks
    fetch("http://127.0.0.1:9000/api/tasks/suggest/")
        .then(res => res.json())
        .then(data => displaySuggestedTasks(data))
        .catch(err => alert("Error fetching suggested tasks"));
}

function showFloatingNote() {
    const note = document.getElementById("floating-note");

    // Make the note visible
    note.style.display = "block";

    // // Hide the note after 5 seconds
    // setTimeout(() => {
    //     note.style.display = "none";
    // }, 5000); // 5 seconds
}

function displaySuggestedTasks(data) {
    let box = document.getElementById("suggested-tasks");
    box.innerHTML = "";

    data.forEach((task, index) => {
        box.innerHTML += `
            <div class='result-item'>
                <h3>${index + 1}. ${task.title}</h3>
                <p><b>Score:</b> ${task.score}</p>
                <p><b>Due Date:</b> ${task.due_date}</p>
                <p><b>Importance:</b> ${task.importance}</p>
                <p><b>Hours:</b> ${task.estimated_hours}</p>
                <p><b>Explanation:</b> ${task.explanation}</p>
            </div>
        `;
    });
}

