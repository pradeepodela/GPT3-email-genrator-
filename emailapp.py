import streamlit as st
import openai

def generate_email( userPrompt ="Write me a professionally sounding email", start="Dear"):
        """Returns a generated an email using GPT3 with a certain prompt and starting sentence"""

        response = openai.Completion.create(
        engine="davinci",
        prompt=userPrompt + "\n\n" + start,
        temperature=0.71,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0.36,
        presence_penalty=0.75
        )
        return response.get("choices")[0]['text']
st.title("Email Generator App")


with st.form(key="form"):
    prompt = st.text_input("Describe the Kind of Email.")
    st.text(f"(Example: Write me a professional sounding email to my boss)")

    start = st.text_input("Begin writing the first few or several words of your email:")

    slider = st.slider("How many characters do you want your email to be? ", min_value=64, max_value=750)
    st.text("(A typical email is usually 100-500 characters)")

    submit_button = st.form_submit_button(label='Generate Email')

    if submit_button:
        with st.spinner("Generating Email..."):
            output = generate_email(prompt, start)
        st.markdown("# Email Output:")
        st.subheader(start + output)
