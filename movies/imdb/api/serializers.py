from rest_framework import serializers
from imdb.models import Movie

# [2 types of serializer, one is Serializer, ModelSerializer ]



# this is using validators and function based for each value!!!
# def len_name(value):
#     if len(value) <= 2:
#         raise serializers.ValidationError(" the name must be more than 5 charcters")

# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     movie_name = serializers.CharField(validators = [len_name])
#     movie_desc = serializers.CharField()
#     movie_status = serializers.BooleanField()

    
#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
#     # [if data posted/created is valid then create a new object of data]


#     def update(self, instance ,validated_data):
#         instance.movie_name = validated_data.get('movie_name', instance.movie_name)
#         instance.movie_desc = validated_data.get('movie_desc', instance.movie_desc)
#         instance.movie_status = validated_data.get('movie_status', instance.movie_status)
#         instance.save()
#         return instance
#     # [HERE THE instance IS OLD DATA AND THE validated_data IS NEW DATA]
#     #  SO WE ARE ADDING NEW DATA INTO OLD DATA, EVEN IF IT IS UPDATED OR NOT
    
    
#     # this is the function/field level validation.
#     def validate_movie_name(self, value):

#         if len(value) <= 2:
#             raise serializers.ValidationError('The name length should be more than 5 characters')
#         return value

#     # this is object level validation, we are validation for all the objects in class and for every field as well.
#     def validate(self, data):

#         if data['movie_name'] == data['movie_desc']:
#             raise serializers.ValidationError("the name and description cannot be same")
#         return data
    
#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
#     # [if data posted/created is valid then create a new object of data]


#     def update(self, instance ,validated_data):
#         instance.movie_name = validated_data.get('movie_name', instance.movie_name)
#         instance.movie_desc = validated_data.get('movie_desc', instance.movie_desc)
#         instance.movie_status = validated_data.get('movie_status', instance.movie_status)
#         instance.save()
#         return instance
#     # [HERE THE instance IS OLD DATA AND THE validated_data IS NEW DATA]
#     #  SO WE ARE ADDING NEW DATA INTO OLD DATA, EVEN IF IT IS UPDATED OR NOT
    
    
#     # this is the function/field level validation.
#     def validate_movie_name(self, value):

#         if len(value) <= 2:
#             raise serializers.ValidationError('The name length should be more than 5 characters')
#         return value

#     # this is object level validation, we are validation for all the objects in class and for every field as well.
#     def validate(self, data):

#         if data['movie_name'] == data['movie_desc']:
#             raise serializers.ValidationError("the name and description cannot be same")
#         return data
    
# #  The above one was serializers.Serializer 


###############################################################################################
# [but now learning ModelSerializer]

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"
        # exclude =['movie_name']

    
    def validate_movie_name(self, value):

        if len(value) <= 2:
            raise serializers.ValidationError("The movie name should be more than 5 character")
    
    def validate(self, data):

        if data['movie_name'] == data['movie_desc']:
            raise serializers.ValidationError(" name and description cannot be same")
        return data
    
    