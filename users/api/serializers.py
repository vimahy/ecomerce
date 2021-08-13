from rest_framework import serializers
from users.models import User


class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('username','email','name','last_name')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields ='__all__'
    
    def create(self,validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    def update(self,instance,validated_data):
        updated_user= super().update(instance,validated_data)
        updated_user.set_password(validated_data['password'])
        updated_user.save()
        return updated_user
        
        
class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
    # Cambiar los valores que queremos impŕimir
    # Solo se traen los valores que se mecesitan
    def to_representation(self,instance):
        return{
            'id': instance['id'],
            'username': instance['username'],
            'email':instance['email'],
            'password':instance['password']
        }
        
        

class TestUserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    email = serializers.EmailField()
    
    # Aqui generamos nuestras propias validaciones
    # Validaciones de campos
    def validate_name(self,value):
        print(self.context)
        if 'developer' in value:
            raise serializers.ValidationError("Error nuede existir ese nombre")
        return value
    # Aqui generamos nuestras propias validaciones        
    def validate_email(self,value):
        if value=='':
            raise serializers.ValidationError("Debe indicar un correo ")
        # LLAMAMOS A VALIDATE_NAME
        
        return value
        
    # Aqui generamos nuestras propias validaciones 
    # Validacion general       
    def validate(self, data):
        return data
        
    def create(self, validated_data):
        return self.model.objects.create(**validated_data)
       
    def update(self,instance,validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.email = validated_data.get('email',instance.email)
        instance.save()
        return instance
        

