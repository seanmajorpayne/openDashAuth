# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Label(Component):
    """A Label component.
A component for adding labels to inputs in forms with added sizing controls.

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
- hidden (boolean; optional): Hide label from UI, but allow it to be discovered by screen-readers.
- size (string; optional): Set size of label. Options 'sm', 'md' (default) or 'lg'.
- html_for (string; optional): Set the `for` attribute of the label to bind it to a particular element
- width (optional): Specify width of label for use in grid layouts. Accepts the same values
as the Col component.
- xs (optional): Specify label width on extra small screen

Valid arguments are boolean, an integer in the range 1-12 inclusive, or a
dictionary with keys 'offset', 'order', 'size'. See the documentation for
more details.
- sm (optional): Specify label width on a small screen

Valid arguments are boolean, an integer in the range 1-12 inclusive, or a
dictionary with keys 'offset', 'order', 'size'. See the documentation for
more details.
- md (optional): Specify label width on a medium screen

Valid arguments are boolean, an integer in the range 1-12 inclusive, or a
dictionary with keys 'offset', 'order', 'size'. See the documentation for
more details.
- lg (optional): Specify label width on a large screen

Valid arguments are boolean, an integer in the range 1-12 inclusive, or a
dictionary with keys 'offset', 'order', 'size'. See the documentation for
more details.
- xl (optional): Specify label width on an extra large screen

Valid arguments are boolean, an integer in the range 1-12 inclusive, or a
dictionary with keys 'offset', 'order', 'size'. See the documentation for
more details.
- align (a value equal to: 'start', 'center', 'end'; default 'center'): Set vertical alignment of the label, options: 'start', 'center', 'end',
default: 'center'
- color (string; optional): Text color, options: primary, secondary, success, warning, danger, info,
muted, light, dark, body, white, black-50, white-50.
- loading_state (dict; optional): Object that holds the loading state object coming from dash-renderer. loading_state has the following type: dict containing keys 'is_loading', 'prop_name', 'component_name'.
Those keys have the following types:
  - is_loading (boolean; optional): Determines if the component is loading or not
  - prop_name (string; optional): Holds which property is loading
  - component_name (string; optional): Holds the name of the component that is loading"""
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, style=Component.UNDEFINED, className=Component.UNDEFINED, key=Component.UNDEFINED, hidden=Component.UNDEFINED, size=Component.UNDEFINED, html_for=Component.UNDEFINED, width=Component.UNDEFINED, xs=Component.UNDEFINED, sm=Component.UNDEFINED, md=Component.UNDEFINED, lg=Component.UNDEFINED, xl=Component.UNDEFINED, align=Component.UNDEFINED, color=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'style', 'className', 'key', 'hidden', 'size', 'html_for', 'width', 'xs', 'sm', 'md', 'lg', 'xl', 'align', 'color', 'loading_state']
        self._type = 'Label'
        self._namespace = 'dash_bootstrap_components'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'style', 'className', 'key', 'hidden', 'size', 'html_for', 'width', 'xs', 'sm', 'md', 'lg', 'xl', 'align', 'color', 'loading_state']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(Label, self).__init__(children=children, **args)
