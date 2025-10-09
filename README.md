# mini_RAG


## Installation (Conda + pip)

Follow these steps to set up the Python environment and install dependencies.

### 1) Install Miniconda (if you don't have it)
- Download from: https://docs.conda.io/en/latest/miniconda.html
- Follow the installer steps for your OS

### 2) Create the Conda environment (Python 3.8)
```bash
conda create -n mini_rag_app python=3.8 -y
```

### 3) Activate the environment
```bash
conda activate mini_rag_app
```

### 4) Install Python dependencies
```bash
python -m pip install -r requirments.txt
```


### 5) Verify installation
```bash
conda run -n mini_rag_app python -m pip show fastapi uvicorn python-multipart
```

