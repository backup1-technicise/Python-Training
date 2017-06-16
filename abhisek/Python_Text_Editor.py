'''
Write a Python program to make a chain of function decorators (bold, italic, underline etc.).
'''


def make_bold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped


def make_italic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped


def make_underline(fn):
    def wrapped():
        return "<u>" + fn() + "</u>"
    return wrapped


@make_bold
@make_italic
@make_underline


def hello():
    return "hello world"


fp = open("xyz.html", 'w')
mod_string = hello()    ## returns "<b><i><u>hello world</u></i></b>"
fp.write("<html>")
fp.write("<br>")
fp.write(mod_string)
fp.write("</html>")
