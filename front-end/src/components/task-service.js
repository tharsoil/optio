import { Class } from '@mui/icons-material';
import { isAuthenticated } from '../utils/auth';



class Task {

    baseUrl = "http://localhost:8000/tasks";

    constructor(
        title = '',
        projectId = null,
        id = null,
        subtasks = [],
        dueDate = '',
        comments = [],
        description = '',
        taskStatus = ''
    ) {
        this.id = id;
        this.projectId = projectId;
        this.title = title;
        this.subtasks = subtasks;
        this.comments = comments;
        this.dueDate = dueDate;
        this.description = description;
        this.taskStatus = taskStatus;
    }

    async getTasks(params = {}) {
        const loggedIn = isAuthenticated();
        if (!loggedIn) {
            return;
        }

        const projectId = params["projectId"]
        const endpoint = `/get-tasks/?project_id=${projectId}`;
        const accessToken = localStorage.getItem("access_token");

        try {
            const response = await fetch(`${this.baseUrl}${endpoint}`, {
                method: 'GET',
                headers: {
                    "Content-Type": "application/json",
                    "Authorization": `Bearer ${accessToken}`,
                },
            })
            const tasks = await response.json();
            return tasks;
        }
        catch (err) {
            console.log("SOME ERROR OCCURED WHILE FETCHING PROJECT TASKS: ", err);
        }
    }

    async getTask(taskId) {
        const loggedIn = isAuthenticated();
        if (!loggedIn) {
            return;
        }
        const accessToken = localStorage.getItem("access_token");

        const endpoint = `/get-task-by-id/${taskId}`;

        try {
            console.log("FETCHING TASK WITH ID : ", taskId);
            const response = await fetch(`${this.baseUrl}${endpoint}`, {
                method: 'GET',
                headers: {
                    "Content-Type": "application/json",
                    "Authorization": `Bearer ${accessToken}`,
                },
            })
            const task = await response.json();
            if (response.ok) {
                console.log("SUCCESSFULLY FETCHED TASK ", task);
                return task;
            }
            else {
                console.log("COULDN'T FETCH TASK");
            }
        }
        catch (error) {
            console.log("AN ERROR OCCURED WHILE FETCHING THE TASK WITH ID : ", error);
        }

    }

    async updateTask(params = {}) {
        const loggedIn = isAuthenticated();
        if (!loggedIn) {
            return;
        }
        const accessToken = localStorage.getItem("access_token");

        const requestBody = Object.fromEntries(
            Object.entries(params).filter(([key, value]) => value != undefined)
        );
        console.log("UPDATES IN TASK ARE :", requestBody);

        if (!requestBody['id']) {
            console.log("TASK ID IS MISSING CANNOT UPDATE THE TASK");
            return;
        }
        const updateEndpoint = `/update-task/${requestBody['id']}/`


        try {
            const response = await fetch(`${this.baseUrl}${updateEndpoint}`, {
                method: "PUT",
                headers: {
                    "Content-Type": "application/json",
                    "Authorization": `Bearer ${accessToken}`,
                },
                body: JSON.stringify(requestBody),
            });
            const updatedTask = await response.json();
            if (response.ok) {
                console.log("TASK WAS UPDATED SUCCESSFULLY");
                console.log("new comments ", updatedTask["comments"]);
                return updatedTask;
            }
            else {
                console.log("FAILED TO UPDATE THE TASK:", response.statusText);
            }
        } catch (error) {
            console.log("ERROR DURING THE TASK UPDATE :", error);
        }
    }

    async search(searchTexts = {}) {
        const loggedIn = isAuthenticated();
        if (!loggedIn) {
            return;
        }
        const accessToken = localStorage.getItem("access_token");

        const taskTitle = searchTexts["task"];
        const projectName = searchTexts["project"];
        const taskStatus = searchTexts["status"];

        const endpoint = `/search/?title=${taskTitle}&status=${taskStatus}&project=${projectName}`;
        const url = `${this.baseUrl}${endpoint}`;

        try {
            const response = await fetch(url, {
                method: 'GET',
                headers: {
                    "Content-Type": "application/json",
                    "Authorization": `Bearer ${accessToken}`,
                },
            });

            const tasks = await response.json();
            console.log("search texts are ", searchTexts);
            console.log("founded tasks ", tasks);
            return tasks;
        }
        catch (error) {
            console.log("An error occured while searching for task ", error);
        }
    }

}


class Sanitize {

    const defaultProperties = {
        comments: [],                    
        subtasks: [],                    
        title: "Untitled",               
        due_date: null,                  
        description: "",                 
        task_status: "Pending",          
        created_time: new Date().toISOString(), // Default to current time as ISO string
        project_id: null                 
    };

    sanitizeTaskData(task) {
        return Object.keys(task).reduce((sanitizedTask, key) => {
            sanitizedTask[key] = sanitizeValue(task[key], key);
            return sanitizedTask;
        }, {});
    }

    sanitizeValue(value, key) {
        return value ?? defaultValues[key] ?? "N/A";  // Fallback to default
    }

}


export default Task;


