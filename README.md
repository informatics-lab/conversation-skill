# conversation-skill

This repo is a tool for building conversational Alexa skills. You provide it with config dictionaries 
defining default slot values and speeches, and a class defining your application-specific intents. 

If one of your intents is called with all the slot values included in the request, it will react as 
normal. However, if it is called with some slot values missing, the conversation-skill will try to fill
it by first checking the default slot config. If no default value is found in the config, it will use
the speech config to prompt the user for that slot value.

Usage is as follows:

  Session = conversation.mk_session_class(MyIntentRequestHandlers)
  
  session = Session(event, context, speech_config, default_values, cache)

An example application built on this tool is https://github.com/met-office-lab/dre-skill

## default_values config

A dictionary of the form {IntentName: {'default_values': D, 'general_config': G}}
G is just a dictionary with no special format. It should be used for storing any config 
that can't be overridden by the user.
D can have two forms, depending on whether the intent uses a primary slot or not.
If it doesn't use a primary slot, D has the form 

                {slot: default, ...}.
                
If it does use a primary slot, D has the form 

                {primary_slot: {slot: default, ...}, ...}

## speech_config

A dictionary of the form 

  {
    "session": {"greeting": greeting,
                "reprompt": reprompt,
                "sign_off": sign_off,
                "help": help},
    slot: {"title": title,
           "question": question,
           "reprompt": reprompt,
           "help": help},
     ...
  }

## MyIntentRequestHandlers

A class with one method defining each of your intents.
It also needs to include two properties: _interrupting_ir_map and _ir_map. These map intent 
requests to functionality. The first map is for intent requests that can interrupt a 
dialogue. i.e. they don't need all the slots. The second map is for intent functionality that 
is to run after all the slots have been filled.

### _interrupting_ir_map

A dictionary with the form 

  {intent_name: {'function': class_method, 'terminating': ends_session}}

### _ir_map

A dictionary with the form 

  {intent_name: {'function': class_method, 'grab_session': is_main_intent, ?'primary_slot': slot_name/False}}

where 'primary_slot' is only needed when grab_session is True.
  
