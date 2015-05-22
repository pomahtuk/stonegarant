from compressor.filters.base import FilterBase
from react import jsx


def compile_jsx(content, is_file):
    """Perform jsx.transform"""

    transformer = jsx.JSXTransformer()

    if is_file is True:
        target_file = open(content, 'r')
        jsx_string = target_file.read()
    else:
        jsx_string = content

    return transformer.transform_string(jsx_string)


class JSXCompiler(FilterBase):
    def __init__(self, content, attrs=None, filter_type=None, charset=None, filename=None):
        # FilterBase doesn't handle being passed attrs, so fiddle the signature
        super(JSXCompiler, self).__init__(content, filter_type, filename)

    def input(self, **kwargs):
        if self.filename:
            return compile_jsx(content=self.filename, is_file=True)
        else:
            return compile_jsx(content=self.content, is_file=False)
