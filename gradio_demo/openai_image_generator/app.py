import gradio as gr
import os
import openai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set your OpenAI API key directly for debugging
openai.api_key = os.getenv("OPENAI_API_KEY")

# Hardcoded suggestions
HARDCODED_SUGGESTIONS = [
    "A cyberpunk alley at night, glowing neon signs in Japanese and English, with clear, legible stylized fonts. The word 'Dreamscape' in glowing pink cursive neon above a ramen shop. Rain-soaked pavement reflects the sign's light.",
    "An urban brick wall covered in colorful graffiti art with the word 'Revolution' in large, wild-style spray-painted letters. Each letter is a different vibrant color and has unique stylized textures, shadows, and drips.",
    "A high-fantasy book cover design with the title 'Chronicles of the Lost Realm' in ornate gold embossed lettering, written in a medieval fantasy font. The text sits over a dramatic mountain landscape with a glowing sword in the background.",
    "A chalkboard café menu with handwritten-style typography listing drinks like 'Latte', 'Espresso', and 'Matcha Tea'. Include detailed flourishes, doodles, and price tags in a realistic hand-drawn chalk style.",
    "A retro-futuristic 1980s-style poster with the word 'HYPERDRIVE' in bold chrome and magenta gradient text, styled with a glowing grid in the background and palm trees. Lettering should have a metallic 3D effect."
]

def generate_image(prompt, size="1024x1024", quality="standard", style="vivid"):
    print(f"DEBUG: generate_image called with prompt='{prompt}'")
    try:
        response = openai.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size=size,
            quality=quality,
            n=1,
            style=style
        )
        image_url = response.data[0].url
        print(f"DEBUG: Image URL generated: {image_url}")
        return image_url
    except Exception as e:
        print(f"DEBUG: Error in generate_image: {e}")
        return f"Error generating image: {e}"

js_func = """
function refresh() {
    const url = new URL(window.location);

    if (url.searchParams.get('__theme') !== 'dark') {
        url.searchParams.set('__theme', 'dark');
        window.location.href = url.href;
    }
}
"""

with gr.Blocks(js=js_func) as demo:
    gr.Image(
        value="/Users/syedaanshrahgillani/Documents/github/gemini-cli/TextPixs/assets/logo.png",
        label="TextPixs Logo",
        show_label=False,
        scale=1,
        min_width=0,
        container=False
    )
    gr.Markdown(
        """
        ### Revolutionizing Text Rendering in AI-Generated Images
        
        This application showcases the core capabilities of TextPixs, a research project focused on generating images with coherent, legible, and accurately spelled text. Explore how our model tackles the challenges of typography in AI-generated visuals.
        """
    )

    # Display suggestions at the top
    gr.Markdown("## Suggested Prompts for Text Rendering Accuracy")
    
    # Display suggestions in a read-only textbox for copying
    gr.Textbox(
        label="Copy a suggestion below and paste it into the Image Prompt field:", 
        interactive=False, 
        lines=len(HARDCODED_SUGGESTIONS) * 2, # Adjust lines to fit all suggestions
        value="\n\n".join([f"{i+1}. {s}" for i, s in enumerate(HARDCODED_SUGGESTIONS)]),
        visible=True
    )

    with gr.Tab("Generate Image with Accurate Text") as generate_tab:
        with gr.Row():
            prompt_input = gr.Textbox(
                label="Image Prompt", 
                placeholder="Describe the image, including any specific text you want rendered (e.g., 'a vintage sign saying \"Welcome Home\"')...",
                lines=3
            )
            generate_button = gr.Button("Generate Image", variant="primary")
        
        with gr.Row():
            size_dropdown = gr.Dropdown(
                choices=["1024x1024", "1792x1024", "1024x1792"], 
                label="Image Size", 
                value="1024x1024",
                interactive=True
            )
            quality_dropdown = gr.Dropdown(
                choices=["standard", "hd"], 
                label="Image Quality", 
                value="standard",
                interactive=True
            )
            style_dropdown = gr.Dropdown(
                choices=["vivid", "natural"], 
                label="Image Style", 
                value="vivid",
                interactive=True
            )
        output_image = gr.Image(label="Generated Image with Accurate Text", show_label=True)

    generate_button.click(
        generate_image,
        inputs=[prompt_input, size_dropdown, quality_dropdown, style_dropdown],
        outputs=output_image
    )

demo.launch()
