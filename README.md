# Howler Monkey Detector

## Introduction
This master's thesis project develops a machine learning model by fine-tuning the [YOLO](https://docs.ultralytics.com/) (You Only Look Once) model specifically for the detection of howler monkeys in video footage. This project is designed to assist the "Primatas Urbanos" research group at UFRGS by automating the detection of howler monkeys in urban environments. The goal is to facilitate the study of these primates by providing valuable metrics on their behavior, thereby contributing to both academic research and urban wildlife management.

## Table of Content
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Local Training](#local-training)
- [Running the API](#running-the-api)
- [Contributing](#contributing)

  
## Prerequisites

Before installing the project, ensure you have the following prerequisites installed:

### Docker

Docker is used to containerize your application, ensuring it runs the same in any environment.

#### Windows & macOS:

1. Download Docker Desktop from the [official Docker website](https://www.docker.com/products/docker-desktop).
2. Run the installer and follow the on-screen instructions.
3. Once installed, open Docker Desktop to complete the setup.

#### Linux:

1. Update your package index and install Docker using your distribution's package manager. For example, on Ubuntu, run:
   ```bash 
   $ sudo apt update && sudo apt upgrade -y
   $ sudo apt install docker.io
   ```
2. To ensure Docker runs on startup, enable the Docker service:
   ``` bash
   $ sudo systemctl enable --now docker
   ```
3. Verify the installation by running:
   ``` bash
   $ docker --version
   ```

### VS Code
setup vs code with dev container

## Installation

To set up this project locally, follow these steps:

### Step 1: Fork the Project

Start by forking the repository to your own GitHub account. This creates a personal copy of the project that you can modify freely without affecting the original codebase.

- Navigate to the GitHub page of the project.
- In the top-right corner of the page, click the "Fork" button.

### Step 2: Clone Your Fork

Once you have forked the repository, you can clone it to your local machine to start working on it.

- On your GitHub fork, click the "Clone or download" button and copy the URL provided.
- Open your terminal and run the following command, replacing `YOUR_USERNAME` with your GitHub username:

```bash
$ git clone https://github.com/YOUR_USERNAME/howler-monkey-detection.git
```

- Navigate into the project directory:

```bash
cd howler-monkey-detection
```

### Step 3: Add the Original Repository as a Remote

To keep your fork up to date with the original project, add the original repository as a remote:

```bash
git remote add upstream https://github.com/original-developer/howler-monkey-detection.git
```

You can fetch updates from the original repository and merge them into your fork with:

```bash
git fetch upstream
git merge upstream/main main
```

## Local Training

This project is structured to streamline the process of downloading the necessary dataset files from Google Drive, fine-tuning the YOLO model with these files, and logging the training process using MLflow. To facilitate version control and reproducibility, we use DVC (Data Version Control).

To initiate the process, ensure you are in the project's root directory and follow these steps:

### Step 1: Initialize Dev container



### Step 2: Initialize DVC

You need to setup your dataset on the `dataset` as the example that dir.


### Step 3: Config file

You need to adjust the `config/config.yaml` file with the traning configuration for the test you'll run.

### Step 4: Running the code

The training pipeline is configured to run on the main file, the data setup, model training and loggin will be executed on that script

```bash
$ python main.py
```

This command triggers the following actions in order:

1. Creates a K-fold document with the train/val splits for the training;
2. Loads the assistant dataset on the train and val folders respecting the number of images used;
3. Runs the model training for every fold on the kfold file;



### Getting Help

If you need help or have questions, feel free to reach out to the project maintainers. We're more than happy to assist you.

