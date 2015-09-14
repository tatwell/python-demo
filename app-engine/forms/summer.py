"""
    Summer Forms
"""
import re

from wtforms import Form, validators, TextAreaField, TextField


class NumberListField(TextAreaField):
    def _value(self):
        if self.data:
            return u' '.join([format(v, ",d") for v in self.data])
        else:
            return u''

    def process_formdata(self, values):
        if values:
            self.data = self.input_to_list(values[0])
        else:
            self.data = []

    def input_to_list(self, values):
        non_decimal = re.compile(r'[^\d.]+')
        normalized = lambda v: non_decimal.sub('', v)
        values = [normalized(v) for v in values.split(' ') if v.strip()]
        return [int(round(float(v))) for v in values if v]

class TargetField(TextField):
    def _value(self):
        if self.data:
            return format(self.data, ",d")
        else:
            return u''

    def process_formdata(self, values):
        # Normalize field value
        non_decimal = re.compile(r'[^\d.]+')
        self.data = non_decimal.sub('', values[0])

    def post_validate(self, form, validation_stopped):
        # Convert field value to int
        if self.data:
            self.data = int(round(float(self.data)))

class SummerForm(Form):
    numbers = NumberListField('Number Set (space-separated positive integers)',
                              [validators.Required()])
    target = TargetField('', [
        validators.Required(),
        validators.Length(min=1, max=12)
    ])
