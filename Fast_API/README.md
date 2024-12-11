# Fast API Instructions

## Setup Instructions

### A. Create a Virtual Environment
- Open Terminal
- Enter the following command
```bash
python -m venv venv
```
- As per device OS
```bash
venv\Scripts\activate #For Windows system operation

source venv/bin/activate #For UNIX system operation
```

### B. Install Dependencies
```bash
pip install -r requirements.txt
```

### C. Prepare Dataset and Model
- Place `Final_Dataset1.csv` in the `dataset/` directory
- Place `Recipe_Recomendation_Model_v2.h5` in the `model/` directory

### D. Run the API
```bash
uvicorn main:app --reload
```

## API Endpoints
- `/recommend` (POST): Get recipe recommendations
  - Input: 
    ```json
    {
      "CategoryUser": "string",
      "TempUser": int,
      "TimeUser": int
    }
    ```
  - Output: List of recommended recipes with their details
