from django.core.exceptions import ValidationError

#  checks wether a file is .mp3 or not
def audio_only(value):

    from os.path import splitext

    ext = (splitext(value.name)[1]).lower() # spllit name and extension in an array of 2 element

    if(ext!=".mp3" and ext!=".wav"):
        raise ValidationError("file format not supported")
    


    