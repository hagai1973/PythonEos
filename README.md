```markdown
# Python Web Automation Project

This project is designed to automate the login process for a web application using Python, Playwright, and pytest.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- You have installed Python 3.10 or later.
- You have installed Playwright.
- You have installed pytest.
- You have created a `.env` file with the necessary environment variables.

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/your-repo-name.git
    cd your-repo-name
    ```

2. **Create a virtual environment:**

    ```sh
    python -m venv venv
    ```

3. **Activate the virtual environment:**

    - On Windows:

        ```sh
        venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```sh
        source venv/bin/activate
        ```

4. **Install the required packages:**

    ```sh
    pip install -r requirements.txt
    ```

5. **Install Playwright browsers:**

    ```sh
    playwright install
    ```

## Configuration

1. **Create a `.env` file in the root directory of the project and add the following environment variables:**

    ```dotenv
    URL=https://web.eos.bnk-il.com/auth
    USER=john_doe@company.com
    PASS=123456
    ```

## Running Tests

To run all the tests, use the following command:

```sh
pytest tests/test_login.py
```

To run tests with a specific tag (e.g., `sanity`), use the following command:

```sh
pytest -m sanity
```

## Project Structure

```
project_root/
    pages/
        __init__.py
        login_page.py
    tests/
		__init__.py
        test_login.py
    .env
    requirements.txt
    README.md
    pytest.ini
```

## License

This project is licensed under the MIT License.
```
