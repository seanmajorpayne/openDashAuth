# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Popover(Component):
    """A Popover component.
Popover creates a toggleable overlay that can be used to provide additional
information or content to users without having to load a new page or open a
new window.

Use the `PopoverHeader` and `PopoverBody` components to control the layout
of the children.

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
- placement (a value equal to: 'auto', 'auto-start', 'auto-end', 'top', 'top-start', 'top-end', 'right', 'right-start', 'right-end', 'bottom', 'bottom-start', 'bottom-end', 'left', 'left-start', 'left-end'; optional): Specify popover placement.
- target (string; optional): ID of the component to attach the popover to.
- container (string; optional): Where to inject the popper DOM node, default body.
- is_open (boolean; optional): Whether the Popover is open or not.
- hide_arrow (boolean; optional): Hide popover arrow.
- innerClassName (string; optional): CSS class to apply to the popover.
- delay (dict; optional): Optionally override show/hide delays - default {show: 0, hide: 250}. delay has the following type: dict containing keys 'show', 'hide'.
Those keys have the following types:
  - show (number; optional)
  - hide (number; optional) | number
- offset (string | number; optional): Popover offset.
- flip (boolean; optional): Whether to flip the direction of the popover if too close to the container
edge, default True.
- loading_state (dict; optional): Object that holds the loading state object coming from dash-renderer. loading_state has the following type: dict containing keys 'is_loading', 'prop_name', 'component_name'.
Those keys have the following types:
  - is_loading (boolean; optional): Determines if the component is loading or not
  - prop_name (string; optional): Holds which property is loading
  - component_name (string; optional): Holds the name of the component that is loading"""
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, style=Component.UNDEFINED, className=Component.UNDEFINED, key=Component.UNDEFINED, placement=Component.UNDEFINED, target=Component.UNDEFINED, container=Component.UNDEFINED, is_open=Component.UNDEFINED, hide_arrow=Component.UNDEFINED, innerClassName=Component.UNDEFINED, delay=Component.UNDEFINED, offset=Component.UNDEFINED, flip=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'style', 'className', 'key', 'placement', 'target', 'container', 'is_open', 'hide_arrow', 'innerClassName', 'delay', 'offset', 'flip', 'loading_state']
        self._type = 'Popover'
        self._namespace = 'dash_bootstrap_components'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'style', 'className', 'key', 'placement', 'target', 'container', 'is_open', 'hide_arrow', 'innerClassName', 'delay', 'offset', 'flip', 'loading_state']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(Popover, self).__init__(children=children, **args)
