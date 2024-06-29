# Python FastAPI App

This repository contains a Python FastAPI app.

## Installation

1. Clone the repository

2. Install the dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. Start the FastAPI app:

```bash
uvicorn main:app --reload
```

2. Open your browser and navigate to `http://localhost:8000` to access the app.

## API Endpoints

- `/`: Home endpoint
- `/forms`: Get all forms
- `/answers/{form_id}`: Get all answer that belongs to a form
- `/form`: Create a new form
- `/answer`: Create a new answer

## License

This project is licensed under the [MIT License](LICENSE).
