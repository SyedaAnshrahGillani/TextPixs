# Sana Gradio Demo

This directory contains a Gradio demo for the Sana model, adapted from the `Sana_fork` repository.

## Setup

1.  **Navigate to the demo directory:**
    ```bash
    cd /Users/syedaanshrahgillani/Documents/github/gemini-cli/TextPixs/gradio_demo
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

    *Note: Some dependencies like `diffusers` and `clip` were originally installed from git repositories. The `requirements.txt` has been modified to use the PyPI versions. If you encounter issues, you may need to install them directly from their respective GitHub repositories as follows:*
    ```bash
    pip install "diffusers[torch]" --upgrade
    pip install git+https://github.com/openai/CLIP.git
    ```

## Running the Demo

To run the Gradio demo, execute the following command from within the `gradio_demo` directory:

```bash
python app.py
```

The demo should then be accessible in your web browser at the address provided in the console output (usually `http://127.0.0.1:7860`).
