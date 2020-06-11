# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Fade(Component):
    """A Fade component.
Hide or show content with a fading animation. Visibility of the children is
controlled by the `is_open` prop which can be targetted by callbacks.

Keyword arguments:
- children (a list of or a singular dash component, string or number; optional): The children of this component
- id (string; optional): The ID of this component, used to identify dash components
in callbacks. The ID needs to be unique across all of the
components in an app.
- style (dict; optional): Defines CSS styles which will override styles previously set.
- className (string; optional): Often used with CSS to style elements with common properties.
- key (string; optional): A unique identifier for the component, used to improve
performance by React.js while rendering components
See https://reactjs.org/docs/lists-and-keys.html for more info
- is_in (boolean; optional): Controls whether the children of the Fade component are currently visible
or not.
- timeout (dict; optional): The duration of the transition, in milliseconds.

You may specify a single timeout for all transitions like: `timeout=500`
or individually like: timeout={'enter': 300, 'exit': 500}. timeout has the following type: number | dict containing keys 'enter', 'exit'.
Those keys have the following types:
  - enter (number; optional)
  - exit (number; optional)
- appear (boolean; optional): Show fade-in animation on initial page load. Default: True.
- enter (boolean; optional): Enable or disable enter transitions. Default: True.
- exit (boolean; optional): Enable or disable exit transitions. Default: True.
- tag (string; optional): HTML tag to use for the fade component. Default: div.
- base_class (string; optional): CSS base class. Note that this class is always used, whether the
components are showing or hidden. Default: 'fade'
- base_class_active (string; optional): CSS class used when the fade contents are displayed. Default: 'show'.
- loading_state (dict; optional): Object that holds the loading state object coming from dash-renderer. loading_state has the following type: dict containing keys 'is_loading', 'prop_name', 'component_name'.
Those keys have the following types:
  - is_loading (boolean; optional): Determines if the component is loading or not
  - prop_name (string; optional): Holds which property is loading
  - component_name (string; optional): Holds the name of the component that is loading"""
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, style=Component.UNDEFINED, className=Component.UNDEFINED, key=Component.UNDEFINED, is_in=Component.UNDEFINED, timeout=Component.UNDEFINED, appear=Component.UNDEFINED, enter=Component.UNDEFINED, exit=Component.UNDEFINED, tag=Component.UNDEFINED, base_class=Component.UNDEFINED, base_class_active=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'style', 'className', 'key', 'is_in', 'timeout', 'appear', 'enter', 'exit', 'tag', 'base_class', 'base_class_active', 'loading_state']
        self._type = 'Fade'
        self._namespace = 'dash_bootstrap_components'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'style', 'className', 'key', 'is_in', 'timeout', 'appear', 'enter', 'exit', 'tag', 'base_class', 'base_class_active', 'loading_state']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(Fade, self).__init__(children=children, **args)
