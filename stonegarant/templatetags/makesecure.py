from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.tag(name='makesecure')
def do_makesecure(parser, token):
    nodelist = parser.parse(('endmakesecure',))
    parser.delete_first_token()
    return MakeSecureNode(nodelist)

class MakeSecureNode(template.Node):
    def __init__(self, nodelist):
        self.nodelist = nodelist

    def render(self, context):
        output = self.nodelist.render(context)
        # return output
        return output.replace('http://', '//')
