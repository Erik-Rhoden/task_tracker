# task_tracker

Task Tracker is a CLI tool that can add, modify, and delete tasks. This was done as part of the Roadmap.sh Projects (https://roadmap.sh/projects/task-tracker)

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installion](#installation)

## Features

* Add tasks
* Set status (todo, in-progress, done)
* Produce an easy to parse list formatted in columns/rows
* Update the status of a task anytime
* Delete a task when it's no longer needed
* Reset the task manager for a clean wipe

## Requirements

* iniconfig==2.0.0
* markdown-it-py==3.0.0
* mdurl==0.1.2
* packaging==24.2
* pluggy==1.5.0
* Pygments==2.19.1
* pytest==8.3.4
* rich==13.9.4

## Installation

1. Clone the repository

```bash
https://github.com/Erik-Rhoden/task_tracker.git
```

2. Navigate to directory

```bash
cd task_tracker
```

3. Add your first task

```bash
$ task-cli add foo
```

4. Change status when you need to focus on a task or move it to the backburner

```bash
$ task-cli update 1 --status in-progress
```

5. Use the helpful help menu to learn other useful commands

```bash
$ task-cli update --help
```
