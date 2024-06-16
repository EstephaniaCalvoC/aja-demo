# Project Name / Back


## How to run

**Note:** Run the following steps in the `back` directory

1. **Set environment variables in `.env`** <a id="env-vars"></a>

    This API uses Azure cloud resources like Blob Storage and Azure AI Search.

    ~~~bash
    VARIALBE_NAME=
    ~~~   

2. **Set virtual environment** <a id="venv"></a>

    ~~~bash
    python -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    ~~~


3. **Run service**

    ~~~bash
    python run_api.py
    ~~~

## How to call

- **Using request**
    ~~~python
    import requests

    response = requests.post(
        "http://localhost:8000/the/endpoint/path",
        json={'key': 'value'}
    )
    print(response.json())
    ~~~
