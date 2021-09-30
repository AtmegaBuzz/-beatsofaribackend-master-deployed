from django.contrib import messages
from .models import Contact
from django.utils.translation import gettext_lazy as _
from phonenumber_field.phonenumber import to_python
            

class ContactForm:
    def __init__(self,request,first_name,last_name,email,phone,message):
        self.request = request
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.message = message



    def save(self):

        Contact.objects.create(
            first_name=self.first_name,
            last_name=self.last_name,
            email=self.email,
            phone=self.phone,
            message=self.message
        )
    
    
    def cleanFname(self):
        if(len(self.first_name)==0):
            messages.error(self.request,"Enter First Name")
            return False

        
        else:
            return True
    
    def cleanLname(self):
        if(len(self.last_name)==0):
            messages.error(self.request,"Enter Last Name")
            return False
              
        else:
            return True
        
        
    def cleanemail(self):
        if(len(self.email)==0 or (self.email).endswith(".com")==False):
            messages.error(self.request,"Invalid Email")
            return False
        
        else:
            return True
        
    def cleanphone(self):
            phone_number = to_python(self.phone)
            if phone_number and not phone_number.is_valid():
                messages.error(self.request,"Invalid Phone Number")
                return False
            else:
                return True


    def is_valid(self):
        form_valid = self.cleanFname() and self.cleanLname() and self.cleanemail() and self.cleanphone()

        if(form_valid):
            messages.error(self.request,"Form Submitted!")
            return True
        else:
            return False

    
    
        