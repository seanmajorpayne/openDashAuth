# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Col(Component):
    """A Col component.
Component for creating Bootstrap columns to control the layout of your page.

Use the width argument to specify width, or use the breakpoint arguments
(xs, sm, md, lg, xl) to control the width of the columns on different screen
sizes to achieve a responsive layout.

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
- width (optional): Specify the width of the column. Behind the scenes this sets behaviour at
the xs breakpoint, and will be overriden if xs is specified.

Valid arguments are boolean, an integer in the range 1-12 inclusive, or a
dictionary with keys 'offset', 'order', 'size'. See the documentation for
more details.
- xs (optional): Specify column behaviour on an extra small screen.

Valid arguments are boolean, an integer in the range 1-12 inclusive, or a
dictionary with keys 'offset', 'order', 'size'. See the documentation for
more details.
- sm (optional): Specify column behaviour on a small screen.

Valid arguments are boolean, an integer in the range 1-12 inclusive, or a
dictionary with keys 'offset', 'order', 'size'. See the documentation for
more details.
- md (optional): Specify column behaviour on a medium screen.

Valid arguments are boolean, an integer in the range 1-12 inclusive, or a
dictionary with keys 'offset', 'order', 'size'. See the documentation for
more details.
- lg (optional): Specify column behaviour on a large screen.

Valid arguments are boolean, an integer in the range 1-12 inclusive, or a
dictionary with keys 'offset', 'order', 'size'. See the documentation for
more details.
- xl (optional): Specify column behaviour on an extra large screen.

Valid arguments are boolean, an integer in the range 1-12 inclusive, or a
dictionary with keys 'offset', 'order', 'size'. See the documentation for
more details.
- align (a value equal to: 'start', 'center', 'end', 'stretch', 'baseline'; optional): Set vertical alignment of this column's content in the parent row. Options
are 'start', 'center', 'end', 'stretch', 'baseline'.
- loading_state (dict; optional): Object that holds the loading state object coming from dash-renderer. loading_state has the following type: dict containing keys 'is_loading', 'prop_name', 'component_name'.
Those keys have the following types:
  - is_loading (boolean; optional): Determines if the component is loading or not
  - prop_name (string; optional): Holds which property is loading
  - component_name (string; optional): Holds the name of the component that is loading"""
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, style=Component.UNDEFINED, className=Component.UNDEFINED, key=Component.UNDEFINED, width=Component.UNDEFINED, xs=Component.UNDEFINED, sm=Component.UNDEFINED, md=Component.UNDEFINED, lg=Component.UNDEFINED, xl=Component.UNDEFINED, align=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'style', 'className', 'key', 'width', 'xs', 'sm', 'md', 'lg', 'xl', 'align', 'loading_state']
        self._type = 'Col'
        self._namespace = 'dash_bootstrap_components'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'style', 'className', 'key', 'width', 'xs', 'sm', 'md', 'lg', 'xl', 'align', 'loading_state']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(Col, self).__init__(children=children, **args)
