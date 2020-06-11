# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Nav(Component):
    """A Nav component.
Nav can be used to group together a collection of navigation links.

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
- pills (boolean; optional): Apply pill styling to nav items. Active items will be indicated by a pill.
- card (boolean; optional): Set to True when using Nav with pills styling inside a CardHeader.
- fill (boolean; optional): Expand the nav items to fill available horizontal space.
- justified (boolean; optional): Expand the nav items to fill available horizontal space, making sure
every nav item has the same width.
- vertical (boolean | string; optional): Stack NavItems vertically. Set to True for a vertical Nav on all screen
sizes, or pass one of the Bootstrap breakpoints ('xs', 'sm', 'md', 'lg',
'xl') for a Nav which is vertical at that breakpoint and above, and
horizontal on smaller screens.
- horizontal (a value equal to: 'start', 'center', 'end', 'between', 'around'; optional): Specify the horizontal alignment of the NavItems. Options are 'start',
'center', or 'end'.
- navbar (boolean; optional): Set to True if using Nav in Navbar component. This applies the `navbar-nav`
class to the Nav which uses more lightweight styles to match the parent
Navbar better.
- loading_state (dict; optional): Object that holds the loading state object coming from dash-renderer. loading_state has the following type: dict containing keys 'is_loading', 'prop_name', 'component_name'.
Those keys have the following types:
  - is_loading (boolean; optional): Determines if the component is loading or not
  - prop_name (string; optional): Holds which property is loading
  - component_name (string; optional): Holds the name of the component that is loading"""
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, style=Component.UNDEFINED, className=Component.UNDEFINED, key=Component.UNDEFINED, pills=Component.UNDEFINED, card=Component.UNDEFINED, fill=Component.UNDEFINED, justified=Component.UNDEFINED, vertical=Component.UNDEFINED, horizontal=Component.UNDEFINED, navbar=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'style', 'className', 'key', 'pills', 'card', 'fill', 'justified', 'vertical', 'horizontal', 'navbar', 'loading_state']
        self._type = 'Nav'
        self._namespace = 'dash_bootstrap_components'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'style', 'className', 'key', 'pills', 'card', 'fill', 'justified', 'vertical', 'horizontal', 'navbar', 'loading_state']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(Nav, self).__init__(children=children, **args)
