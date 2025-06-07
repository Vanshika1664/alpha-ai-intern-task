import React, { useEffect, useState } from 'react';
import axios from 'axios';

function App() {
  const [tasks, setTasks] = useState([]);
  const [newTask, setNewTask] = useState('');

  // Load from cache or server
  useEffect(() => {
    const cachedTasks = localStorage.getItem('tasks');
    if (cachedTasks) {
      setTasks(JSON.parse(cachedTasks));
    } else {
      fetchTasksFromServer();
    }
  }, []);

  // Fetch from server
  const fetchTasksFromServer = async () => {
    try {
      const response = await axios.get('http://localhost:5000/tasks');
      setTasks(response.data);
      localStorage.setItem('tasks', JSON.stringify(response.data));
    } catch (error) {
      console.error('Error fetching tasks:', error);
    }
  };

  // Add a task
  const addTask = () => {
    if (!newTask) return;
    axios.post('http://localhost:5000/tasks', { task: newTask })
      .then(() => {
        const updatedTasks = [...tasks, { name: newTask }]; // Assuming each task is an object
        setTasks(updatedTasks);
        localStorage.setItem('tasks', JSON.stringify(updatedTasks));
        setNewTask('');
      })
      .catch(error => console.error('Error adding task:', error));
  };

  // Delete a task
  const deleteTask = (taskToDelete) => {
    axios.delete('http://localhost:5000/tasks', { data: { task: taskToDelete } })
      .then(() => {
        const updatedTasks = tasks.filter(task => task.name !== taskToDelete);
        setTasks(updatedTasks);
        localStorage.setItem('tasks', JSON.stringify(updatedTasks));
      })
      .catch(error => console.error('Error deleting task:', error));
  };

  // ✅ The actual UI (make sure Refresh button is here!)
  return (
    <div>
      <h1>Task List</h1>
      <input
        type="text"
        placeholder="Enter new task"
        value={newTask}
        onChange={e => setNewTask(e.target.value)}
      />
      <button onClick={addTask}>Add Task</button>
      <button onClick={fetchTasksFromServer}>Refresh Cache</button>

      <ul>
        {tasks.map((task, index) => (
          <li key={index}>
            {task.name}
            <button onClick={() => deleteTask(task.name)}>❌</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
