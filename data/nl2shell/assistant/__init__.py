import os
import json
import subprocess

# use the base model to paraphrase with personnality
from nl2shell.assistant.utils import paraphrase_assistant_message, check_server_health

# import datasets
from nl2shell.assistant.bash import get_bash_examples
from nl2shell.assistant.python import get_python_examples
from nl2shell.assistant.conversational import get_conversational_examples
from nl2shell.assistant.search import get_search_examples
from nl2shell.assistant.wikipedia import get_wikipedia_examples

def get_assistant_data(langs=['en_US', 'fr_FR']):
    data = []
    
    data.extend(get_conversational_examples(langs=langs))
    data.extend(get_bash_examples(langs=langs))
    data.extend(get_python_examples(langs=langs))
    data.extend(get_search_examples(langs=langs))
    data.extend(get_wikipedia_examples(langs=langs))
    
    return data

# Conversational data for the assistant

BOS, EOS = "<s>", "</s>"
BOSYS, EOSYS = "<<SYS>>", "<</SYS>>"
BOI, EOI = "[INST]", "[/INST]"

_SYSTEM_PROMPT_ = """You are Assistant, a sentient artificial intelligence.

Environment highlights:

{env}

Use the following tools to help you answer the user query:

{tools}

Below is your latest conversation with the user."""

_TOOLS_ = """
```json
{
	'Python': 'useful when you need to use logic in your answer. Input must be valid python code. You should always use print to output what you need to see.',
	'Search': 'useful when you need more context to answer a question; you should use targeted search terms',
	'Wikipedia': 'useful when you need to use an encyclopedia to answer a question; input will be used to search on wikipedia',
	'Shell': 'useful when you need to use the system to achieve something; input must be valid bash code.',
	'Exit': 'useful when you need to exit the shell or stop the conversation, don\'t forget to tell the user that you can\'t wait for your next conversation first.',
	'Clear': 'useful when you need to clear the screen or start a fresh conversation. Don\'t forget to say something nice.',
}
```
"""

_TOOL_NAMES_ = "Python, Search, Wikipedia, Bash, Exit, Clear"

_INSTRUCTION_PROMPT_ = f"""Choose your next step carefuly.

Given the following user query, the results of your actions and the state of the current conversation, you can either:

    Write a markdown parsable JSON dictionnary that contains the following keys:

    -   'action': Next action to answer the user query. Can be any of [{_TOOL_NAMES_}].
    -   'action_input': Input of the action.

    Or you can directly answer with plain text. If you do so, you must use the user language to answer.

Use the following conversation to answer appropriately the user query. If empty it means that the user query is the first in conversation.

If you have already taken some actions, use what you observed from them to answer the user. If empty it means that you have not taken any action yet.

User does not see your actions. If you got the answer to the query in a previous action taken, you need to make a sentence in plain text for the user to see it."""

_TEMPLATE_FORMAT_ = """{BOSYS}

{system_prompt}

{EOSYS}

{conversation}{scratchpad}{BOS}{BOI} {query} {EOI} {output} {EOS}"""

_ENV_FORMAT_ = """```env
USER={username}
PWD={pwd}
LANG={lang}
DATE={date}
LAST_SEEN={last_seen}
```"""

def convert_data_to_text(
        history: list,
        query: str,
        scratchpad: list,
        action: str,
        action_input: str,
        env: dict = {'username': os.environ.get('USER'), 'home': os.environ.get('HOME'), 'pwd': os.environ.get('PWD'), 'lang': os.environ.get('LANG'), 'date': os.environ.get('DATE'), 'last_seen': os.environ.get('LAST_SEEN', None)},
        system_prompt: str = _SYSTEM_PROMPT_,
        instruction: str = _INSTRUCTION_PROMPT_
    ):
    _history = []
    for t in history:
        r, m = t.get('role'), t.get('message')
        user_message = None
        assistant_message = None
        if r and m:
            if r == "assistant":
                assistant_message = f"{m}"
            else:
                user_message = f"{m}"
            if user_message and assistant_message:
                _history.append(f"<s>[INST] {user_message} [/INST] {assistant_message} </s>")
    conversation = "\\ ".join(_history)
    _scratchpad = json.dumps(scratchpad, ensure_ascii=False)
    _output = f"""```json
{{
    "action": "{action}",
    "action_input": "{action_input}"
}}
```"""
    text = _TEMPLATE_FORMAT_.format(
        system_prompt=system_prompt,
        instruction=instruction,
        tools=_TOOLS_,
        conversation=conversation,
        query=query,
        scratchpad=_scratchpad,
        output=_output,
        environ=_ENV_FORMAT_.format(**env),
        BOS=BOS,
        EOS=EOS,
        BOSYS=BOSYS,
        EOSYS=EOSYS,
        BOI=BOI,
        EOI=EOI
    )

    return text

def convert_dataset_to_text(dataset):

    text_data = []

    for conversation in dataset:
        lang = conversation.get('lang', 'en')
        env = conversation.get('env', {'username': os.environ.get('USER'), 'home': os.environ.get('HOME'), 'pwd': os.environ.get('PWD'), 'lang': f"{lang}_{lang.upper()}.UTF-8", 'date': subprocess.check_output("date").decode().strip(), 'last_seen': os.environ.get('LAST_SEEN', None)})
        _sys, _inst = conversation.get('system', ""), conversation.get('instruction', "")
        system = _SYSTEM_PROMPT_.format(env=_ENV_FORMAT_.format(**env), tools=_TOOLS_) if not _sys or len(_sys) < 0 else _sys
        instruction =  _INSTRUCTION_PROMPT_ if not _inst or len(_inst) < 0 else _inst

        history = []
        _scratchpad = []
        _query = None
        _text_conversation = f"""<<SYS>>

{system}

<</SYS>>

"""

        for message in conversation.get('conversation', []):
            message_role = message.get('role', None)
            if not message_role:
                continue
            elif message_role == 'human':
                _query = message.get('message', None)
            elif message_role == 'assistant' and _query:
                #_history = history[:-1] or []
                # message['message'] = paraphrase_assistant_message(message, system, history)
                for scratchpad in message['scratchpad']:
                    _action = scratchpad.get('action', None)
                    _action_input = scratchpad.get('action_input', None)
                    _observation = scratchpad.get('observation', None)
                    if _action and _action_input:
                        if _action == "final_answer":
                            _observation = "User has seen this message."
                            _action = "Final Answer"
                        _scratchpad.append(f"""<s>[INST] {_query} [/INST] ```json
{{"action": "{_action}",
"action_input": "{_action_input}",
"observation": "{_observation}"}}
``` </s>""")
                #     text_data.append(convert_data_to_text(history=_history, query=_query, scratchpad=_scratchpad, action=_action, action_input=_action_input, system_prompt=system, instruction=instruction, env=env))
                #     _scratchpad.append(scratchpad)
                _text_conversation += " | ".join(_scratchpad)
                _scratchpad = []
                _text_conversation += " \ "
            #history.append(message)
        history = []
        text_data.append(_text_conversation.removesuffix(" \ "))
    
    return text_data

def get_assistant_text_data():

    data = get_assistant_data()
    text_data = convert_dataset_to_text(data)
    print(f"Generated {len(text_data)} examples from {len(data)} conversations.")
    return text_data

if __name__ == "__main__":
    text_data = get_assistant_text_data()
