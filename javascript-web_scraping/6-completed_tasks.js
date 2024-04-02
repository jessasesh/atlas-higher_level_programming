#!/usr/bin/node

// Import the required module
const request = require('request');

// Get the URL from command line arguments
const apiUrl = process.argv[2];

// Initialize an object to store the count of completed tasks for each user
const completedTasksByUser = {};

// Make a GET request to the API URL
request.get(apiUrl, function (err, response, body) {
  // Handle errors, if any
  if (err) {
    console.error(err);
    return;
  }

  // Parse the response body to JSON format
  const tasks = JSON.parse(body);

  // Iterate through each task
  tasks.forEach(function(task) {
    // Check if the task is completed
    if (task.completed === true) {
      // Check if the user ID is already in the dictionary
      if (task.userId in completedTasksByUser) {
        // If yes, increment the count of completed tasks for the user
        completedTasksByUser[task.userId] += 1;
      } else {
        // If no, set the count of completed tasks for the user to 1
        completedTasksByUser[task.userId] = 1;
      }
    }
  });

  // Print the object containing the count of completed tasks for each user
  console.log(completedTasksByUser);
});