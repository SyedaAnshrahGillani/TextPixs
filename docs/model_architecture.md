# TextPixs Model Architecture

This document outlines the core architecture of the TextPixs model, focusing on its key components and their synergistic interaction to achieve enhanced text rendering in text-to-image generation.

## Overview

TextPixs is built upon a novel, multi-pronged framework called **Glyph-Conditioned Diffusion with Character-Aware Attention (GCDA)**. This framework enhances a standard diffusion backbone by integrating three synergistic components:

1.  **Dual-Stream Text Encoder**: Processes both semantic contextual information and explicit visual glyph representations of the input text.
2.  **Character-Aware Attention Mechanism**: Guides the model to allocate distinct spatial focus to individual characters.
3.  **OCR-in-the-Loop Fine-Tuning Stage**: Optimizes for legibility and spelling accuracy using OCR-based feedback.

## Component Breakdown

### 1. Dual-Stream Text Encoder

This innovative encoder processes input text through two parallel streams:

*   **Semantic Stream**: Utilizes a pre-trained BERT encoder to capture high-level meaning, context, and relationships from the input text. This ensures the model understands *what* the text means.
*   **Orthographic Stream**: Employs a Glyph Renderer and a Character-Level Convolutional Neural Network (CNN) to extract precise visual representations of text structure, character shapes, and typographic information. This stream addresses *how* the text visually appears.

The outputs from both streams are then combined to create a rich, character-aware embedding of the input text, which is fed into the diffusion model.

### 2. Character-Aware Attention Mechanism

This mechanism is crucial for preventing common issues like character fusion and distortion in generated text. It is guided by a novel **Attention Segregation Loss** that:

*   Encourages the model to allocate distinct, non-overlapping spatial attention to individual characters during the generation process.
*   Ensures that each character maintains its unique visual identity and position within the generated image.

### 3. OCR-in-the-Loop Fine-Tuning Stage

This stage is a key innovation for achieving high text fidelity. It involves:

*   Leveraging a pre-trained Optical Character Recognition (OCR) model (e.g., TrOCR) as a differentiable critic.
*   Providing direct, targeted feedback on text legibility and spelling accuracy during the fine-tuning process.
*   Actively penalizing textual inaccuracies, leading to significant improvements in text fidelity and legibility in the final generated images.

## Diffusion Backbone

The GCDA framework is integrated with a **fine-tuned Stable Diffusion Model** which serves as the generative backbone. This allows TextPixs to leverage the powerful image synthesis capabilities of diffusion models while addressing their inherent limitations in text rendering.

## Training Protocol

The model employs a comprehensive two-stage training protocol:

1.  **Initial Training**: Focuses on general text-to-image generation with the dual-stream encoder and character-aware attention mechanism.
2.  **Fine-Tuning with OCR-in-the-Loop**: Refines the model's text rendering capabilities using the OCR feedback mechanism.

## Data

Training and evaluation are conducted using a comprehensive and diverse set of datasets, including:

*   **MARIO-10M**: A large-scale dataset for text-in-image generation.
*   **T2I-CompBench**: A benchmark specifically designed for compositional text-to-image generation with text rendering evaluation protocols.
*   **COCO-Text & TextCaps**: Datasets rich in text-image pairs for general text-to-image tasks.
*   **Custom Multilingual Datasets**: Developed to ensure broad applicability and robust performance across various languages and scripts.

## Performance Highlights

TextPixs demonstrates significant improvements in text fidelity and visual quality, achieving state-of-the-art results in character-based text rendering metrics while maintaining competitive image synthesis quality.
