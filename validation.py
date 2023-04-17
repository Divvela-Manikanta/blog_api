from marshmallow import Schema,fields,validate,ValidationError


def valid_blog_content(blogBody):
    content = blogBody.split(" ")
    if(len(content)>200):
        raise ValidationError("Blog content should exceed greater than 200 words")
    else:
        length = len(content)
        return True

class validate(Schema):
    id = fields.Str(required=True)
    name =fields.Str(required=True)
    description =fields.Str(required=True)
    createdBy = fields.Str(required=True)
    topic:str =fields.Str(required=True)
    blogBody = fields.Str(required=True,validate=valid_blog_content)
    isPosted = fields.Str(required=True)

def blog_method(val):
    try:
         blog = validate()
         valid_to_return = blog.load(val)
         return valid_to_return
    except ValidationError as err:
        return(err.messages)