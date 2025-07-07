# TextPixs Application Code

This directory contains the core application logic and Gradio demo files for the TextPixs project. The scripts here are responsible for setting up the user interface, handling user input, orchestrating the image generation process, and ensuring content safety.

## Directory Contents

*   `app_textpixs.py`: This is the main script that defines and runs the Gradio web interface. It integrates various components of the TextPixs system, including the diffusion pipeline and safety checker, to provide an interactive demo.

*   `textpixs_pipeline.py`: This file encapsulates the TextPixs diffusion pipeline. It is responsible for loading the underlying model, managing the image generation steps, and applying the core TextPixs architecture (Glyph-Conditioned Diffusion with Character-Aware Attention) to produce high-fidelity images with accurate text rendering.

*   `safety_check.py`: This module implements a safety mechanism to filter out potentially harmful or inappropriate content. It uses a pre-trained language model to analyze user prompts and generated images, ensuring that the demo adheres to safety guidelines.

## How it Relates to TextPixs Architecture

The files in this `app/` directory are the operational heart of the TextPixs system. They implement the user-facing aspects and integrate the core research components:

*   `app_textpixs.py` acts as the **presentation layer**, providing the interactive interface for users to experiment with TextPixs.
*   `textpixs_pipeline.py` is the **core model implementation**, where the theoretical concepts of the Glyph-Conditioned Diffusion with Character-Aware Attention (GCDA) framework are put into practice for image generation.
*   `safety_check.py` ensures the **ethical and responsible deployment** of the TextPixs model by filtering content based on predefined safety criteria.

Together, these components demonstrate the end-to-end functionality of the TextPixs research, from user input to generated output, while adhering to safety standards.