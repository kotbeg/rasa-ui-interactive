# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
import requests
import json
from rasa_core_sdk import Action

logger = logging.getLogger(__name__)


class ActionPainResponse(Action):
    def name(self):
        # define the name of the action which can then be included in training stories
        return "action_pain_response"

    def run(self, dispatcher, tracker, domain):
        # what your action should do
        url = 'https://icanhazdadjoke.com/'
        headers = {'Accept': 'application/json'}
        request = json.loads(requests.get(url, headers=headers).text)
        joke = request['joke']  # extract a joke from returned json response
        dispatcher.utter_message(joke)  # send the message back to the user
        return []