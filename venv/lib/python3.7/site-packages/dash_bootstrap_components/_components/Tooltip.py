# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Tooltip(Component):
    """A Tooltip component.
A component for adding tooltips to any element, no callbacks required!

Simply add the Tooltip to you layout, and give it a target (id of a
component to which the tooltip should be attached)

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
- target (string; optional): The id of the element to attach the tooltip to
- boundaries_element (string; optional): Boundaries for popper, can be scrollParent, window, viewport, or any DOM
element
- hide_arrow (boolean; optional): Hide arrow on tooltip
- container (string; optional): Where to inject the popper DOM node, default body
- delay (dict; optional): optionally override show/hide delays - default { show: 0, hide: 250 }. delay has the following type: dict containing keys 'show', 'hide'.
Those keys have the following types:
  - show (number; optional)
  - hide (number; optional) | number
- innerClassName (string; optional): CSS classes to apply to the inner-tooltip
- arrowClassName (string; optional): CSS classes to apply to the arrow-tooltip ('arrow' by default)
- autohide (boolean; optional): Optionally hide tooltip when hovering over tooltip content - default true
- placement (a value equal to: 'auto', 'auto-start', 'auto-end', 'top', 'top-start', 'top-end', 'right', 'right-start', 'right-end', 'bottom', 'bottom-start', 'bottom-end', 'left', 'left-start', 'left-end'; optional): How to place the tooltip.
- offset (string | number; optional): Tooltip offset
- loading_state (dict; optional): Object that holds the loading state object coming from dash-renderer. loading_state has the following type: dict containing keys 'is_loading', 'prop_name', 'component_name'.
Those keys have the following types:
  - is_loading (boolean; optional): Determines if the component is loading or not
  - prop_name (string; optional): Holds which property is loading
  - component_name (string; optional): Holds the name of the component that is loading"""
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, style=Component.UNDEFINED, className=Component.UNDEFINED, key=Component.UNDEFINED, target=Component.UNDEFINED, boundaries_element=Component.UNDEFINED, hide_arrow=Component.UNDEFINED, container=Component.UNDEFINED, delay=Component.UNDEFINED, innerClassName=Component.UNDEFINED, arrowClassName=Component.UNDEFINED, autohide=Component.UNDEFINED, placement=Component.UNDEFINED, offset=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'style', 'className', 'key', 'target', 'boundaries_element', 'hide_arrow', 'container', 'delay', 'innerClassName', 'arrowClassName', 'autohide', 'placement', 'offset', 'loading_state']
        self._type = 'Tooltip'
        self._namespace = 'dash_bootstrap_components'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'style', 'className', 'key', 'target', 'boundaries_element', 'hide_arrow', 'container', 'delay', 'innerClassName', 'arrowClassName', 'autohide', 'placement', 'offset', 'loading_state']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(Tooltip, self).__init__(children=children, **args)
