"""
This program translate the english to french and vice versa.
"""

import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator('LiE6BvM5ZzunIjuAhn-EccQQWPZHo1s__HujzoDkBe9v')
language_translator = LanguageTranslatorV3(
    version = '{version}',
    authenticator = authenticator
)

language_translator.set_service_url('https://api.us-south.language-translator.watson.cloud.ibm.com/instances/81c75a29-7564-4100-b6d0-1bdddc2f3475')

def english_to_french(request):
    """
    This fuction translates english into french.
    """
    if request is None:
        return None
    response = language_translator.translate(text=request, model_id="en-fr").get_result()
    translation = response['translations'][0]['translation']
    return translation

def french_to_english(request):
    """
    This fuction translates english into french.
    """
    if request is None:
        return None
    response = language_translator.translate(text=request, model_id="fr-en").get_result()
    translation = response['translations'][0]['translation']
    return translation
