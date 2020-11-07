c = get_config()

# Our user list
c.Authenticator.whitelist = [
    'suess_j1',
    'suess_j2'
]

c.Authenticator.admin_users = {
    'suess_j1',
    'suess_j2'
}

# instructor1 and instructor2 have access to different shared servers:
c.JupyterHub.load_groups = {
    'formgrade-kurs_j1': [
        'suess_j1',
    ],
    'formgrade-kurs_j2': [
        'suess_j2'
    ],
    'nbgrader-kurs_j1': [],
    'nbgrader-kurs_j2': []
}

# Start the notebook server as a service. The port can be whatever you want
# and the group has to match the name of the group defined above.
c.JupyterHub.services = [
    {
        'name': 'kurs_j1',
        'url': 'http://127.0.0.1:9999',
        'command': [
            'jupyterhub-singleuser',
            '--group=formgrade-kurs_j1',
            '--debug',
        ],
        'user': 'grader-kurs_j1',
        'cwd': '/home/suess_j1',
        'api_token': '{{kurs_j1_token}}'
    },
    
    {
        'name': 'kurs_j2',
        'url': 'http://127.0.0.1:9998',
        'command': [
            'jupyterhub-singleuser',
            '--group=formgrade-kurs_j2',
            '--debug',
        ],
        'user': 'grader-kurs_j2',
        'cwd': '/home/suess_j2',
        'api_token': '{{kurs_j2_token}}'
    },
    
]

