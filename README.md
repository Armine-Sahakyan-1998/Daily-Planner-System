# Daily Planner System (CLI Task Manager)

A lightweight, terminal-based day planning application built with Python. It allows users to effectively map out their daily schedules, 
organize activities, assign priority vectors, and manage dynamic check-lists efficiently.

## Features
* **Task Prioritization:** Categorize activities based on urgency (e.g., *a lot, not a lot, a little*).
* **Live Schedule Tracking:** Real-time console logs mapping out current schedules and ongoing targets.
* **Database Management:** Full capability to insert new plans, review schedules, and instantly prune or clear records.
* **Modular Codebase:** Organizes independent business routines into secure Python helper functions.

## Technical Concepts Used
* **Hash-Map Inventories (`dict`):** Employs key-value dictionaries to map target names directly to their weight criteria.
* **Sanitation Loops:** Incorporates membership verification pipelines to avoid null modifications or registry conflicts.
* **Dynamic Record Purging:** Implements the `del` utility to prune dictionary storage buffers on demand.
* **Interactive Control Matrix:** Relies on an explicit `while True` engine coupled with state evaluations to capture menu inputs.
## Preview Example
```text
Task Management System:
1. Add Task
2. View Tasks
3. Remove Task
4. Exit
Enter your choice (1, 2, 3 or 4): 1
Enter the task name: Study Python OOP
How important is it? (a lot, not a lot, a little): a lot
Task 'Study Python OOP' added with priority: a lot.
```
