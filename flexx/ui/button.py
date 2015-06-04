""" Button widgets.
"""

from ..pyscript import js
from ..properties import Prop, Instance, Str, Tuple, Float

from .widget import Widget



class Button(Widget):
    
    CSS = """
    .zf-button-xx {
        background: #fee;
    }
    """
    
    text = Str('push me')
    
    # def __init__(self):
    #     Mirrored.__init__(self)
    #     #self._js_init()  # todo: allow a js __init__
    
    @js
    def _js_create_node(self):
        this.node = document.createElement('button')
    
    @js
    def _text_changed__js(self, name, old, txt):
        this.node.innerHTML = txt


class Label(Widget):
    CSS = ".zf-label { border: 0px solid #454; }"

    text = Str('')
    
    @js
    def _js_create_node(self):
        # todo: allow setting a placeholder DOM element, or any widget parent
        this.node = document.createElement('div')
        #this.node.className = this.cssClassName
        flexx.get('body').appendChild(this.node);
        # this.node.innerHTML = 'a label'
        # super()._init()
    
    @js
    def _text_changed__js(self, name, old, txt):
        this.node.innerHTML = txt