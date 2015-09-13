"""
    Summer Forms
"""
from wtforms import Form, validators, TextAreaField, TextField

class SummerForm(Form):
    numbers = TextAreaField('Number Set (space-separated integers)', [validators.Required()])
    target = TextField('', [
        validators.Required(),
        validators.Length(min=1, max=12)
    ])
