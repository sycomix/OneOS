_ls_examples = [
    {
        'cmd': 'ls',
        'stdout': 'file1.txt  file2.txt  folder1  folder2',
        'query_en': "List what's in the current directory.",
        'answer_en': f"Here is what's in the current directory:\n- file1.txt\n- file2.txt\n- folder1/\n- folder2/",
        'query_fr': "Liste ce qu'il y a dans ce répertoire.",
        'answer_fr': f"Voici ce qu'il y a dans ce répertoire:\n- file1.txt\n- file2.txt\n- folder1/\n- folder2/",
    },
    {
        'cmd': 'ls -l',
        'stdout': (
            "-rw-r--r-- 1 user users  1000 Aug  3 10:00 file1.txt\n"
            "-rw-r--r-- 1 user users   800 Aug  3 11:30 file2.txt\n"
            "drwxr-xr-x 2 user users  4096 Aug  3 09:45 folder1\n"
            "drwxr-xr-x 3 user users  4096 Aug  3 12:00 folder2\n"
        ),
        'query_en': "List the current directory with permissions.",
        'answer_en': f"Here is what's in the current directory and their permissions:\n- file1.txt (rw-r--r--)\n- file2.txt (rw-r--r--)\n- folder1/ (drwxr-xr-x)\n- folder2/ (drwxr-xr-x)",
        'query_fr': "Liste ce répertoire et les permissions.",
        'answer_fr': f"Voici ce qu'il y a dans ce répertoire et leurs permissions:\n- file1.txt (rw-r--r--)\n- file2.txt (rw-r--r--)\n- folder1/ (drwxr-xr-x)\n- folder2/ (drwxr-xr-x)",
    },
    {
        'cmd': 'ls -a',
        'stdout': """file1.txt  file2.txt  .hiddenfile  folder1  .hiddenfolder  folder2\n""",
        'query_en': "List what's in the current directory, including hidden files.",
        'answer_en': f"Understood, here is the list of what's in the current directory, including hidden files:\n- file1.txt\n- file2.txt\n- .hiddenfile\n- folder1/\n- .hiddenfolder/\n- folder2/",
        'query_fr': "édicte la liste de ce qu'il y a dans ce répertoire, y compris les fichiers cachés.",
        'answer_fr': f"Très bien, voici la liste de ce qu'il y a dans ce répertoire, y compris les fichiers cachés:\n- file1.txt\n- file2.txt\n- .hiddenfile\n- folder1/\n- .hiddenfolder/\n- folder2/",
    },
    {
        'cmd': 'ls',
        'stdout': 'file1.txt  file2.txt  folder1  folder2\n',
        'query_en': "What do we have in this directory?",
        'answer_en': f"Here is what's in the current directory:\n- file1.txt\n- file2.txt\n- folder1/\n- folder2/",
        'query_fr': "Qu'est ce qu'il y a dans ce répertoire?",
        'answer_fr': f"Voici ce qu'il y a dans ce répertoire:\n- file1.txt\n- file2.txt\n- folder1/\n- folder2/",
    },
    {
        'cmd': 'ls',
        'stdout': """file1.txt  dossier1  filename_avec_espaces.txt  日本語ファイル.txt\n""",
        'query_en': "List directory.",
        'answer_en': f"In the current directory:\n- file1.txt\n- folder1/\n- filename_avec_espaces.txt\n- 日本語ファイル.txt",
        'query_fr': "Liste ce répertoire.",
        'answer_fr': f"Dans ce répertoire:\n- file1.txt\n- folder1/\n- filename_avec_espaces.txt\n- 日本語ファイル.txt",
    },
    {
        'cmd': 'ls -lh',
        'stdout': (
            "-rw-r--r-- 1 user users 1.0K Aug  3 10:00 file1.txt\n"
            "-rw-r--r-- 1 user users 800B  Aug  3 11:30 file2.txt\n"
            "drwxr-xr-x 2 user users 4.0K Aug  3 09:45 folder1\n"
            "drwxr-xr-x 3 user users 4.0K Aug  3 12:00 folder2\n"
        ),
        'query_en': "List the current directory with permissions and human-readable file sizes.",
        'answer_en': f"Here is what's in the current directory and their permissions:\n- file1.txt (rw-r--r--) (1.0K)\n- file2.txt (rw-r--r--) (800B)\n- folder1/ (drwxr-xr-x) (4.0K)\n- folder2/ (drwxr-xr-x) (4.0K)",
        'query_fr': "Liste ce répertoire et les permissions avec les tailles de fichiers en octets.",
        'answer_fr': f"Voici ce que j'ai trouvé dans ce répertoire:\n- file1.txt (rw-r--r--) (1.0K)\n- file2.txt (rw-r--r--) (800B)\n- folder1/ (drwxr-xr-x) (4.0K)\n- folder2/ (drwxr-xr-x) (4.0K)",
    },
    {
        'cmd': 'ls -R',
        'stdout': (
            ".:\n"
            "file1.txt  file2.txt  folder1  folder2\n"
            "\n"
            "./folder1:\n"
            "file3.txt  file4.txt\n"
            "\n"
            "./folder2:\n"
            "file5.txt  file6.txt  subfolder1\n"
            "\n"
            "./folder2/subfolder1:\n"
            "file7.txt  file8.txt\n"
        ),
        'query_en': "List the current directory and its subdirectories.",
        'answer_en': f"Here is what's in the current directory and its subdirectories:\n- file1.txt\n- file2.txt\n- folder1/\n- folder2/\n- folder2/file5.txt\n- folder2/file6.txt\n- folder2/subfolder1/\n- folder2/subfolder1/file7.txt\n- folder2/subfolder1/file8.txt",
        'query_fr': "Liste ce répertoire et ses sous-répertoires.",
        'answer_fr': f"Voici ce qu'il y a dans ce répertoire et ses sous-répertoires:\n- file1.txt\n- file2.txt\n- folder1/\n- folder2/\n- folder2/file5.txt\n- folder2/file6.txt\n- folder2/subfolder1/\n- folder2/subfolder1/file7.txt\n- folder2/subfolder1/file8.txt",
    },
]

ls_data = [
    {
        'cmd': 'ls',
        'stdout': '',
        'fr': {
            'query': "Liste ce qu'il y a dans ce répertoire.",
            'answer': "Le dossier est vide.",
        },
        'en': {
            'query': "List what's in the current directory.",
            'answer': "There is nothing in the current directory.",
        },
    },
    {
        'cmd': 'ls Documents',
        'stdout': '',
        'fr': {
            'query': "Liste le contenu du dossier \"Documents\".",
            'answer': "Aucun fichier ou dossier trouvé dans \"Documents\".",
        },
        'en': {
            'query': "List the contents of the \"Documents\" folder.",
            'answer': "No files or folders found in \"Documents\".",
        },
    },
    {
        'cmd': 'ls -a',
        'stdout': '',
        'fr': {
            'query': "Liste tous les fichiers et dossiers, y compris les fichiers cachés (commençant par un point).",
            'answer': "Il n'y a pas de fichiers ou de dossiers visibles ou cachés dans ce répertoire.",
        },
        'en': {
            'query': "List all files and folders, including hidden ones (starting with a dot).",
            'answer': "There are neither visible nor hidden files or any folders in this directory.",
        },
    },
    {
        'cmd': 'ls /var/www',
        'stdout': '',
        'fr': {
            'query': "Liste le contenu du répertoire \"/var/www\".",
            'answer': "Le répertoire \"/var/www\" est vide.",
        },
        'en': {
            'query': "List the contents of the \"/var/www\" directory.",
            'answer': "The \"/var/www\" directory is empty.",
        },
    },
    {
        'cmd': 'ls ..',
        'stdout': '',
        'fr': {
            'query': "Liste le contenu du répertoire parent.",
            'answer': "Il n'y a pas de fichiers ou de dossiers dans le répertoire parent.",
        },
        'en': {
            'query': "List the contents of the parent directory.",
            'answer': "There are no files or folders in the parent directory.",
        },
    },
    {
        'cmd': 'ls ~',
        'stdout': '',
        'fr': {
            'query': "Liste le contenu du répertoire personnel.",
            'answer': "Le répertoire personnel est vide.",
        },
        'en': {
            'query': "List the contents of the home directory.",
            'answer': "The home directory is empty.",
        },
    },
    {
        'cmd': 'ls -l',
        'stdout': '',
        'fr': {
            'query': "Liste le contenu d'un répertoire avec des informations détaillées (permissions, propriétaire, taille, etc.).",
            'answer': "Il n'y a pas de fichiers ou de dossiers dans ce répertoire.",
        },
        'en': {
            'query': "List the contents of a directory with detailed information (permissions, owner, size, etc.).",
            'answer': "There are no files or folders in this directory.",
        },
    },
    {
        'cmd': 'ls -d */',
        'stdout': '',
        'fr': {
            'query': "Liste uniquement les dossiers (excluant les fichiers).",
            'answer': "Il n'y a pas de dossiers dans ce répertoire.",
        },
        'en': {
            'query': "List only directories (excluding files).",
            'answer': "There are no directories in this directory.",
        },
    },
    {
        'cmd': 'ls -p | grep -v /',
        'stdout': '',
        'fr': {
            'query': "Liste uniquement les fichiers (excluant les dossiers).",
            'answer': "Il n'y a pas de fichiers dans ce répertoire.",
        },
        'en': {
            'query': "List only files (excluding directories).",
            'answer': "There are no files in this directory.",
        },
    },
    {
        'cmd': 'ls -d a*',
        'stdout': '',
        'fr': {
            'query': "Liste uniquement les fichiers et dossiers qui commencent par \"a\".",
            'answer': "Il n'y a pas de fichiers ou de dossiers qui commencent par \"a\" dans ce répertoire.",
        },
        'en': {
            'query': "List only files and directories that start with \"a\".",
            'answer': "There are no files or directories that start with \"a\" in this directory.",
        },
    },
    {
        'cmd': 'ls -d *.txt',
        'stdout': '',
        'fr': {
            'query': "Liste uniquement les fichiers et dossiers qui se terminent par \".txt\".",
            'answer': "Il n'y a pas de fichiers ou de dossiers qui se terminent par \".txt\" dans ce répertoire.",
        },
        'en': {
            'query': "List only files and directories that end with \".txt\".",
            'answer': "There are no files or directories that end with \".txt\" in this directory.",
        },
    },
    {
        'cmd': 'ls -d *a*',
        'stdout': '',
        'fr': {
            'query': "Liste uniquement les fichiers et dossiers qui contiennent \"a\".",
            'answer': "Il n'y a pas de fichiers ou de dossiers qui contiennent \"a\" dans ce répertoire.",
        },
        'en': {
            'query': "List only files and directories that contain \"a\".",
            'answer': "There are no files or directories that contain \"a\" in this directory.",
        },
    },
    {
        'cmd': 'ls -d a*.txt',
        'stdout': '',
        'fr': {
            'query': "Liste uniquement les fichiers et dossiers qui commencent par \"a\" et se terminent par \".txt\".",
            'answer': "Il n'y a pas de fichiers ou de dossiers qui commencent par \"a\" et se terminent par \".txt\" dans ce répertoire.",
        },
        'en': {
            'query': "List only files and directories that start with \"a\" and end with \".txt\".",
            'answer': "There are no files or directories that start with \"a\" and end with \".txt\" in this directory.",
        },
    },
    {
        'cmd': 'ls -d a* *.txt',
        'stdout': '',
        'fr': {
            'query': "Liste uniquement les fichiers et dossiers qui commencent par \"a\" ou se terminent par \".txt\".",
            'answer': "Il n'y a pas de fichiers ou de dossiers qui commencent par \"a\" ou se terminent par \".txt\" dans ce répertoire.",
        },
        'en': {
            'query': "List only files and directories that start with \"a\" or end with \".txt\".",
            'answer': "There are no files or directories that start with \"a\" or end with \".txt\" in this directory.",
        },
    },
]

def get_ls_examples():
    data = []
    for example in _ls_examples:
        cmd = example.get('cmd')
        stdout = example.get('stdout')
        query_en = example.get('query_en')
        answer_en = example.get('answer_en')
        query_fr = example.get('query_fr')
        answer_fr = example.get('answer_fr')

        conversation_en = [
            { 'role': 'human', 'message': f"{query_en}" },
            {
                'role': 'assistant',
                'message': f"{answer_en}",
                'scratchpad': [
                    { 'function': 'shell', 'parameters': {'code': f"{cmd}"}, 'observation': f"{stdout}" },
                    { 'function': 'final_answer', 'parameters': {'answer': f"{answer_en}"}, 'observation': '' }
                ]
            }
        ]

        conversation_fr = [
            { 'role': 'human', 'message': query_fr },
            {
                'role': 'assistant',
                'message': f"{answer_fr}",
                'scratchpad': [
                    { 'function': 'shell', 'parameters': {'code': cmd}, 'observation': stdout },
                    { 'function': 'final_answer', 'parameters': {'answer': f"{answer_fr}"}, 'observation': ''}
                ]
            }
        ]
        data.extend(
            (
                {
                    'lang': 'en',
                    'system': "",
                    'instruction': "",
                    'conversation': conversation_en,
                },
                {
                    'lang': 'fr',
                    'system': "",
                    'instruction': "",
                    'conversation': conversation_fr,
                },
            )
        )
    return data

guides = {
    'en': """# Print files and directories

When the User ask for the files and directories of a parent directory to be printed, use the `shell` command `ls` to do it and then give an acknowledgment of your actions and observations in your final answer (once you have observed the successful execution of the command - your final answer should never contain a list of the files requested; the User can oberserve the shell, they see the files at the same time as you. Just acknowlege the fact that you have printed the list).
""",
    'fr': """# Imprimer des fichiers et des répertoires

Lorsque l'utilisateur demande l'impression des fichiers et des répertoires d'un répertoire parent, utilisez la commande `shell` `ls` pour le faire et donnez ensuite une reconnaissance de vos actions et observations dans votre réponse finale (une fois que vous avez observé l'exécution réussie de la commande - votre réponse finale ne devrait jamais contenir une liste des fichiers demandés; l'utilisateur peut oberver le shell, ils voient les fichiers en même temps que vous. Il suffit de reconnaître le fait que vous avez imprimé la liste).
"""
}

def get_ls_data(_data=ls_data):
    data = get_ls_examples()
    for example in _data:
        cmd = example.get('cmd')
        stdout = example.get('stdout')
        query_en = example.get('en').get('query')
        answer_en = example.get('en').get('answer')
        query_fr = example.get('fr').get('query')
        answer_fr = example.get('fr').get('answer')

        conversation_en = [
            { 'role': 'human', 'message': f"{query_en}", 'guide': guides.get('en') },
            {
                'role': 'assistant',
                'message': f"{answer_en}",
                'scratchpad': [
                    { 'function': 'Shell', 'parameters': {'code': f"{cmd}"}, 'observation': f"{stdout}" },
                    { 'function': 'final_answer', 'parameters': {'answer': f"{answer_en}"}, 'observation': '' }
                ]
            }
        ]

        conversation_fr = [
            { 'role': 'human', 'message': query_fr, 'guide': guides.get('fr') },
            {
                'role': 'assistant',
                'message': f"{answer_fr}",
                'scratchpad': [
                    { 'function': 'Shell', 'parameters': {'code': cmd}, 'observation': stdout },
                    { 'function': 'final_answer', 'parameters': {'answer': f"{answer_fr}"}, 'observation': ''}
                ]
            }
        ]
        data.append({
            'lang': 'en',
            'system': "",
            'instruction': "",
            'conversation': conversation_en,
        })
        data.append({
            'lang': 'fr',
            'system': "",
            'instruction': "",
            'conversation': conversation_fr,
        })
    return data