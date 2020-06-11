# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DropdownMenu(Component):
    """A DropdownMenu component.
DropdownMenu creates an overlay useful for grouping together links and other
content to organise navigation or other interactive elements.

Keyword arguments:
- children (a list of or a singular dash component, string or number; optional): The children of this component.
- id (string; optional): The ID of this component, used to identify dash components
in callbacks. The ID needs to be unique across all of the
components in an app.
- style (dict; optional): Defines CSS styles which will override styles previously set.
- className (string; optional): Often used with CSS to style elements with common properties.
- key (string; optional): A unique identifier for the component, used to improve
performance by React.js while rendering components
See https://reactjs.org/docs/lists-and-keys.html for more info
- label (string; optional): Label for the DropdownMenu toggle.
- direction (a value equal to: 'down', 'left', 'right', 'up'; optional): Direction in which to expand the DropdownMenu. Default: 'down'.
- right (boolean; optional): Align the DropdownMenu along the right side of its parent. Default: False.
- in_navbar (boolean; optional): Set this to True if the DropdownMenu is inside a navbar. Default: False.
- addon_type (boolean | a value equal to: 'prepend', 'append'; optional): Set this to 'prepend' or 'append' if the DropdownMenu is being used in an input group.
- disabled (boolean; default False): Disable the dropdown.
- nav (boolean; optional): Set this to True if the DropdownMenu is inside a nav for styling consistent
with other nav items. Default: False.
- caret (boolean; default True): Add a caret to the DropdownMenu toggle. Default: True.
- color (string; optional): Set the color of the DropdownMenu toggle. Available options are: 'primary',
'secondary', 'success', 'warning', 'danger', 'info', 'link'. Default: 'secondary'
- toggle_style (dict; optional): Defines CSS styles which will override styles previously set. The styles
set here apply to the DropdownMenu toggle.
- toggleClassName (string; optional): Often used with CSS to style elements with common properties. The classes
specified with this prop will be applied to the DropdownMenu toggle.
- bs_size (a value equal to: 'sm', 'md', 'lg'; optional): Size of the DropdownMenu. 'sm' corresponds to small, 'md' to medium
and 'lg' to large.
- loading_state (dict; optional): Object that holds the loading state object coming from dash-renderer. loading_state has the following type: dict containing keys 'is_loading', 'prop_name', 'component_name'.
Those keys have the following types:
  - is_loading (boolean; optional): Determines if the component is loading or not
  - prop_name (string; optional): Holds which property is loading
  - component_name (string; optional): Holds the name of the component that is loading
- group (boolean; optional): Set group to True if the DropdownMenu is inside a ButtonGroup."""
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, style=Component.UNDEFINED, className=Component.UNDEFINED, key=Component.UNDEFINED, label=Component.UNDEFINED, direction=Component.UNDEFINED, right=Component.UNDEFINED, in_navbar=Component.UNDEFINED, addon_type=Component.UNDEFINED, disabled=Component.UNDEFINED, nav=Component.UNDEFINED, caret=Component.UNDEFINED, color=Component.UNDEFINED, toggle_style=Component.UNDEFINED, toggleClassName=Component.UNDEFINED, bs_size=Component.UNDEFINED, loading_state=Component.UNDEFINED, group=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'style', 'className', 'key', 'label', 'direction', 'right', 'in_navbar', 'addon_type', 'disabled', 'nav', 'caret', 'color', 'toggle_style', 'toggleClassName', 'bs_size', 'loading_state', 'group']
        self._type = 'DropdownMenu'
        self._namespace = 'dash_bootstrap_components'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'style', 'className', 'key', 'label', 'direction', 'right', 'in_navbar', 'addon_type', 'disabled', 'nav', 'caret', 'color', 'toggle_style', 'toggleClassName', 'bs_size', 'loading_state', 'group']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(DropdownMenu, self).__init__(children=children, **args)
