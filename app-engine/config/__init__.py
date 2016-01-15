# Configuration Settings
import os

# Set stage: production (default), development, or test
stage = 'production'

if os.environ.get('SERVER_SOFTWARE', '').startswith('Development'):
    stage = 'development'
elif os.environ.get('SERVER_SOFTWARE', '') == 'TEST':
    stage = 'test'
