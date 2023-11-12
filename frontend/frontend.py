import streamlit as st
from PIL import Image
import requests
import json
from time import time
import pandas as pd

# General settings
st.set_page_config(layout="wide", page_title="Pavlova's LSML-2 final project")
col1, col2 = st.columns(2, gap="medium")

# Left side
col1.header("Welcome to the Sentiment Classification!")
image = Image.open('./materials/sephora_label.png')
col1.image(image, caption='www.sephora.com')
col1.write("##### *Description:*")
col1.write(f"""
Sentiment classification is the automated process of identifying and classifying emotions in text 
as positive sentiment or negative sentiment sentiment based on the customers' opinions expressed within.
We use transfer learning and adopt the DistillBert from HuggingFase :hugging_face: to our downstream task!
The model is a neural network with very high accuracy (around 95%).
It was trained on a big amount beauty products' reviews from Sephora's site :lips:
So, you can check the sentiment of a review on beauty product yourself!
More information about Sephora's brand you can find on its official web-site (the link is below):
""")

with open("./materials/NLP_SEPHORA_TRAINING.zip", "rb") as zipfile:
    col1.download_button(
        "Download IPYNB",
        zipfile,
        mime="application/zip",
        help="Here is the training process of the neural network"
    )

# Right side
upload = col2.text_area(
    label="##### *Please, enter the review:* ",
    value="""Best makeup remover EVER!! I got the sweet apple one and can not recommend it
enough. This is the first makeup remover that actually gets rid of all my makeup and it is so easy to use. 
For the first time ever I don’t wake up with black stains under my eyes from leftover mascara, and the impact 
on my lashes from rubbing the makeup off is soooo much less than before. I would recommend rinsing your face with 
warm water once you are done and applying serum since it can feel like it leaves your face a little oily but it is 
purely mental I have realized. So if you are a freak like me about leaving anything on your face just rinse it.
You won’t regret buying it.""",
    help="Your text should be in English!"
)
start = time()
req = requests.post("http://backend:5000/predict", data=json.dumps({"text": upload}))
result = req.json()["predictions"]
stop = time()
col2.write(f"##### *Result*: {'**:green[Positive]** :+1:' if result else '**:red[Negative]** :-1:'}")
col2.write(f"##### *Evaluation of the service quality:*")

col2.table(
    pd.DataFrame(
        {
            f"Execution time (in seconds)": f"{(stop - start): .2f}",
            "RPS (requests per second)": f"{1/(stop - start): .2f}",
            "Lenght of review (in characters)": f"{len(upload)}"
        }, index=['results']
    )
)
