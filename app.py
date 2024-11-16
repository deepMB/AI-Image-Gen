import os
from openai import OpenAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()
# openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_image(prompt):
    client = OpenAI()
    response  = client.images.generate(prompt=prompt,model="dall-e-2",n=1,size = "1024x1024")
    print(f"---Response --- {response}")
    image_url = response.data[0].url
    return image_url

def main():
    st.title("Image Generation using DALL-E 🖼️")
    input_text = st.text_area("Write your prompt here 🎨")
    if st.button("Generate Image 🖌️") and input_text:
        st.subheader("Your prompt")
        st.text(input_text)
        st.markdown("---")
        url = generate_image(input_text)
        st.image(url,caption="DALL-e generated image")
        
    else:
        st.error("Write your prompt first")

if __name__ == "__main__":
    main()