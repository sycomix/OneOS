# Set prompts
# Leave empty to use default values
system_prompt = intruction_prompt= {
    'en': "",
    'fr': ""
}

# intruction_prompt = {
#     'en': "",
#     'fr': ""
# }
# 

mkdir_examples = [
    {
        'lang': 'en',
        'system': system_prompt.get('en', ""),
        'instruction': intruction_prompt.get('en', ""),
        'conversation': [
            {'role': "human", 'message': "Make directory test"},
            {
                'role': "assistant",
                'message': "I created a new directory test.",
                'scratchpad': [
                    {
                        'function': 'shell',
                        'parameters': {'code': "mkdir test"},
                        'observation': "",
                    },
                    {
                        'function': 'final_answer',
                        'parameters': {
                            'answer': "I created a new directory test."
                        },
                        'observation': "",
                    },
                ],
            },
        ],
    },
    {
        'lang': 'fr',
        'system': system_prompt.get('fr', ""),
        'instruction': intruction_prompt.get('fr', ""),
        'conversation': [
            {'role': "human", 'message': "Crée un répertoire test"},
            {
                'role': "assistant",
                'message': "J'ai créé un nouveau répertoire test.",
                'scratchpad': [
                    {
                        'function': 'shell',
                        'parameters': {'code': "mkdir test"},
                        'observation': "",
                    },
                    {
                        'function': 'final_answer',
                        'parameters': {
                            'answer': "J'ai créé un nouveau répertoire test."
                        },
                        'observation': "",
                    },
                ],
            },
        ],
    },
]

def get_mkdir_examples():
    return mkdir_examples
