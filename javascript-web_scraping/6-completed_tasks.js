#!/usr/bin/node

// Import the required module
const request = require('request');

// Define the API URL
const apiUrl = 'https://jsonplaceholder.typicode.com/todos';

// Make a GET request to the API URL
request.get(apiUrl, function (error, response, body) {
  // Handle errors, if any
  if (error) {
    console.error(error);
    return;
  }

  // Parse the response body to JSON format
  const tasks = JSON.parse(body);

  // Initialize an object to store the count of completed tasks for each user
  const completedTasksByUser = {};

  // Iterate through each task
  tasks.forEach(function(task) {
    // Check if the task is completed
    if (task.completed) {
      // Increment the count of completed tasks for the user
      if (!completedTasksByUser[task.userId]) {
        completedTasksByUser[task.userId] = 1;
      } else {
        completedTasksByUser[task.userId] += 1;
      }
    }
  });

  // Print the object containing the count of completed tasks for each user as JSON
  console.log(JSON.stringify(completedTasksByUser));
});