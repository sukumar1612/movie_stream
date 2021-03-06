DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost"
]

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        # For each OAuth based provider, [either] add a ``SocialApp``
        # (``socialaccount`` app) containing the required client
        # credentials, or list them here:
        'APP': {
            'client_id': '1058649480880-d22empu464lhr9b10dd7c84v6dhf0v7h.apps.googleusercontent.com',
            'secret': 'P-osVEW1x-CjnVGKqi6UGpwP',
            'key': ''
        },
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}

SITE_ID = 2