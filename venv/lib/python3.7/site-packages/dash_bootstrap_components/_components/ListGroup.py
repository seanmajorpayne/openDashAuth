# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class ListGroup(Component):
    """A ListGroup component.
Bootstrap list groups are a flexible way to display a series of content. Use
in conjunction with `ListGroupItem`, `ListGroupItemHeading` and
`ListGroupItemText`.

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
- tag (string; optional): HTML tag to use for the list, default: ul
- flush (boolean; optional): When True the `list-group-flush` class is applied which removes some borders
and rounded corners from the list group in order that they can be rendered
edge-to-edge in the parent container (e.g. a Card).
- loading_state (dict; optional): Object that holds the loading state object coming from dash-renderer. loading_state has the following type: dict containing keys 'is_loading', 'prop_name', 'component_name'.
Those keys have the following types:
  - is_loading (boolean; optional): Determines if the component is loading or not
  - prop_name (string; optional): Holds which property is loading
  - component_name (string; optional): Holds the name of the component that is loading
- horizontal (boolean | string; optional): Set to True for a horizontal ListGroup, or supply one of the breakpoints
as a string for a ListGroup that is horizontal at that breakpoint and up.

Note that horizontal ListGroups cannot be combined with flush ListGroups,
so if flush is True then horizontal has no effect."""
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, style=Component.UNDEFINED, className=Component.UNDEFINED, key=Component.UNDEFINED, tag=Component.UNDEFINED, flush=Component.UNDEFINED, loading_state=Component.UNDEFINED, horizontal=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'style', 'className', 'key', 'tag', 'flush', 'loading_state', 'horizontal']
        self._type = 'ListGroup'
        self._namespace = 'dash_bootstrap_components'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'style', 'className', 'key', 'tag', 'flush', 'loading_state', 'horizontal']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(ListGroup, self).__init__(children=children, **args)
