## **MLOps CI/CD Pipeline for Simple Linear Regression Model**

This project demonstrates a simple Machine Learning pipeline using **MLOps** principles. It contains a basic linear regression model and includes scripts for training, testing, and CI/CD integration using **GitHub Actions**. The pipeline trains a simple model, runs tests to validate correctness, and handles model artifact uploads for future use.

---

### **Project Structure**

```
MLOps_Pipeline/
├── .github/
│   └── workflows/
│       └── mlops-ci.yml      # GitHub Actions workflow for CI/CD
├── model/
│   ├── __init__.py            # Optional (empty for package structure)
│   ├── model.py               # Contains the SimpleModel class (Linear Regression)
│   └── train.py               # Training script to generate synthetic data & save the model
├── tests/
│   └── test_model.py          # Unit test script using pytest for validating model functionality
├── requirements.txt           # Dependencies for the project
└── trained_model.pkl          # Model artifact saved during training (generated via CI/CD)
```

---

### **Overview**

This pipeline allows for the following:
- **Simple Model Implementation**: A basic **Linear Regression** model (SimpleModel) that predicts outputs for synthetic data.
- **Training and Testing**: It generates synthetic data, trains the model, and runs unit tests to check model correctness.
- **CI/CD with GitHub Actions**: Automated testing and model training through GitHub Actions, pushing updates to `MLOps_Dev_Branch_2`.

---

### **Dependencies**

- `numpy`: For mathematical operations and data manipulation.
- `pytest`: For running the tests to ensure correctness.

---

### **Steps to Get Started**

#### **1. Set Up the Project**

Clone the repository to your local machine or directly to your GitHub repository.

```bash
git clone https://github.com/iSPYadav01/MLOps_Pipeline.git
cd MLOps_Pipeline
```

#### **2. Install Dependencies**

Before running the project, install the required dependencies:

```bash
pip install -r requirements.txt
```

#### **3. Run Training and Tests Locally (Optional)**

You can train the model locally and check the test results by running the following commands:

- **Train the Model**:
  
  ```bash
  python model/train.py
  ```

  This script will generate synthetic data, train the model, and save it to `trained_model.pkl`.

- **Run the Tests**:

  ```bash
  pytest tests/test_model.py
  ```

  This will test the model's training and prediction functionalities.

---

### **CI/CD with GitHub Actions**

This repository uses GitHub Actions for Continuous Integration (CI) and Continuous Delivery (CD). The workflow will automatically trigger on changes or pull requests to the `MLOps_Dev_Branch_2` branch.

#### **What Happens in the CI Pipeline?**

1. **Code Checkout**: The code is checked out from the repository.
2. **Python Setup**: Python 3.9 is configured for the project.
3. **Install Dependencies**: Dependencies from `requirements.txt` are installed.
4. **Run Tests**: The `pytest` runs the tests defined in the `tests/test_model.py` file.
5. **Train the Model**: If all tests pass, the model is trained and saved as `trained_model.pkl`.
6. **Upload the Artifact**: The trained model (`trained_model.pkl`) is uploaded as an artifact to GitHub for future use.

#### **How to Monitor the Workflow**

- Go to the **Actions** tab in your GitHub repository to monitor the status of each workflow run.
- You will be able to view the logs for every step in the process, including test results, training steps, and artifact uploads.

---

### **GitHub Actions Workflow**

The GitHub Actions pipeline configuration is located in `.github/workflows/mlops-ci.yml`. It defines the steps to execute on each push or pull request made to the `MLOps_Dev_Branch_2` branch.

Below is the updated version of the action defined in `mlops-ci.yml` for uploading artifacts:

```yaml
name: MLOps CI/CD Pipeline

on:
  push:
    branches:
      - MLOps_Dev_Branch_2
  pull_request:
    branches:
      - MLOps_Dev_Branch_2

jobs:
  build:
    runs-on: ubuntu-latest
    
    steps:
    # Step 1: Checkout the code from GitHub
    - name: Checkout code
      uses: actions/checkout@v2

    # Step 2: Set up Python 3.9 for the project
    - name: Set up Python 3.9
      uses: actions/setup-python@v4
      with:
        python-version: '3.9'

    # Step 3: Install dependencies from requirements.txt
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt

    # Step 4: Run pytest to execute tests
    - name: Run Tests
      run: |
        pytest tests/test_model.py

    # Step 5: Train and save the model
    - name: Train and Save Model
      run: |
        python model/train.py

    # Step 6: Upload the trained model
    - name: Upload trained model
      uses: actions/upload-artifact@v3
      with:
        name: trained-model
        path: trained_model.pkl
```

---

### **Next Steps**

1. **Run the Pipeline**: On any push to the `MLOps_Dev_Branch_2` or pull request targeting this branch, the GitHub Actions pipeline will trigger and run the complete CI/CD pipeline.
2. **Review the Results**: Check the GitHub Actions logs to review the tests and confirm the model is trained and artifacts are uploaded successfully.
3. **Update Your Branch**: Continue to develop new features by creating new branches or updating `MLOps_Dev_Branch_2`. When changes are pushed, the pipeline will automatically retrain the model and rerun tests.

---