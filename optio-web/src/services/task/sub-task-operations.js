import { Class } from "@mui/icons-material";
import { isAuthenticated } from "../../utils/auth";

const BASE_URL = "http://localhost:8000/tasks";

class SubTasksOperation {
  async getSubTasks(parentTaskId) {
    const loggedIn = isAuthenticated();
    if (!loggedIn) {
      return;
    }

    const endpoint = `/${parentTaskId}/get-subtask/`;
    const accessToken = localStorage.getItem("accessToken");

    try {
      const response = await fetch(`${BASE_URL}${endpoint}`, {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${accessToken}`,
        },
      });
      const subTasks = await response.json();
      console.log("SubTasks under parent tasks are ", subTasks);

      return subTasks;
    } catch (err) {
      console.error("Some error occured while fetching the subtasks ", err);
    }
  }
}

export default SubTasksOperation;
