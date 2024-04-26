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

If you haven't already initialized DVC in your project, start by doing so with the following command:

```bash
$ dvc init
```

### Step 3: Run DVC Pipeline

The DVC pipeline is configured to automate the data preparation, model training, and logging processes. To execute the entire pipeline, run:

```bash
$ dvc repro
```

This command triggers the following actions in order:

1. **Data Ingestion**: DVC fetches the necessary howler monkey dataset files from a specified [Google Drive location](https://drive.google.com/drive/folders/1MMPtw-QlWyaVzy0Visqdzsmlur5nhnXM?usp=sharing).
   
2. **Model Fine-Tuning**: The YOLO model is then fine-tuned using the downloaded dataset. 

3. **Training Logging**: Throughout the training process, key metrics and model parameters are logged systematically using MLflow.

   
### Step 3: Accessing MLflow Logs

To view the training logs and metrics:

- Open your web browser and navigate to [MLflow web page](https://dagshub.com/GMainardi/Howler-Monkey.mlflow). Here, you'll find a detailed overview of the training runs, including parameters, metrics, and model artifacts.

By following these steps, you'll successfully download the required data, fine-tune the YOLO model for howler monkey detection, and log the training process for analysis and reproducibility.

## Running the API

This guide will help you get started with the YOLO Model API, allowing you to process videos and train the model using our FastAPI application.


### Getting Started

To run the application, follow these steps:

1. **Start the API Server:** run the following command:

    ```bash
    uvicorn main:app --reload
    ```

    The `--reload` flag enables live reloading so the server will automatically restart upon any code changes. This is useful for development.

2. **Access the Application:** Once the server is up and running, you can access the API at:

    ```
    http://localhost:8000
    ```

    You should see a message indicating that the YOLO Model API is running.

### Swagger Documentation

FastAPI automatically generates interactive API documentation using Swagger UI. You can access this documentation to test the API endpoints directly from your browser.

1. **Open Swagger UI:** Navigate to the following URL in your web browser:

    ```
    http://localhost:8000/docs
    ```

2. **Interact with the API:**

    - **Train the Model:** To initiate model training, use the `/train/` endpoint. Click on the `Try it out` button, execute the request, and you should receive a confirmation message that the model training has started.

    - **Process Videos:** To process a video, use the `/process-video/` endpoint. Click on the `Try it out` button, choose a video file (with a `.mp4` extension) to upload, and execute the request. The API will return the processed video, which you can download.


## Contributing

We're thrilled that you're interested in contributing to the Howler Monkey project! This project aims to leverage technology for wildlife conservation, focusing on the detection of howler monkeys in urban environments. Your contributions can help us make significant strides in this research area.

### How to Contribute

Contributing to this project can take various forms, from writing code and documentation to reporting bugs and suggesting enhancements. Here's how you can get started:

#### Reporting Bugs

If you encounter a bug in the project, we encourage you to report it. Please use the GitHub Issues page for this. When creating a bug report, ensure to include:

- A clear and descriptive title
- A detailed description of the bug
- Steps to reproduce the behavior
- Expected and actual outcomes
- Any relevant screenshots or error messages

#### Suggesting Enhancements

Got an idea to make this project better? We'd love to hear it! Please submit your suggestions as an issue on GitHub, detailing:

- Your proposed enhancement
- How this enhancement would be beneficial to the project
- Any potential implications or considerations

#### Pull Requests

Ready to contribute code or documentation? Great! Here's the process:

1. **Fork the Repository**: Start by forking the project repository to your GitHub account.
2. **Clone Your Fork**: Clone your fork to your local machine and set up the development environment.
3. **Create a Branch**: For each new contribution, create a branch with a meaningful name that reflects the nature of your change.
4. **Make Your Changes**: Implement your changes, adhering to the project's coding standards and guidelines.
5. **Test Your Changes**: Ensure your changes do not break any existing functionality and that all tests pass.
6. **Submit a Pull Request**: Push your branch to your fork on GitHub and then submit a pull request to the main project. Provide a clear description of the problem you're solving and the proposed solution.

### Getting Help

If you need help or have questions, feel free to reach out to the project maintainers. We're more than happy to assist you.

### Acknowledgements

Your contributions are deeply appreciated and will be duly recognized. We maintain a list of contributors in our project documentation, celebrating the efforts of those who have contributed to making this project what it is today.

### Thank You!

Thank you for considering contributing to the Howler Monkey Detection project. Your support helps us advance research in wildlife conservation and urban ecology.

