from rest_framework import serializers

    
class CustomLengthValidator(serializers.Serializer):
    def __init__(self, min_length=None, max_length=None, min_value=None, max_value=None, field_name=None):
        self.min_length = min_length
        self.max_length = max_length
        self.min_value = min_value
        self.max_value = max_value
        self.field_name = field_name
        
    def __call__(self, value):
        
        
        if value is None:
            raise serializers.ValidationError(f'{self.field_name} field is required')
        
        elif self.min_length is not None and len(value) < self.min_length:
            message = f'The length of {self.field_name} should be more than or equal to {self.min_length} characters'
            raise serializers.ValidationError(message)
        elif self.max_length is not None and len(value) > self.max_length:
            message = f'The length of {self.field_name} should be less than or equal to {self.max_length} characters'
            raise serializers.ValidationError(message)
        
        elif self.min_value == 0:
            message = f'{value} cannot be Zero'
            raise serializers.ValidationError(message)
        elif self.min_value is not None and value < self.min_value:
            message = f'The value of {self.field_name} should be more than or equal to {self.min_value}'
            raise serializers.ValidationError(message)
        elif self.max_value is not None and value > self.max_value:
            message = f'The value of {self.field_name} should be less than or equal to {self.max_value}'
            raise serializers.ValidationError(message)
        
        return value
    
    