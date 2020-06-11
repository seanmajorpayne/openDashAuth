# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class NavbarSimple(Component):
    """A NavbarSimple component.
A self-contained navbar ready for use. If you need more customisability try
`Navbar` instead.

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
- brand (string; optional): Brand text, to go top left of the navbar.
- brand_href (string; optional): Link to attach to brand.
- brand_style (dict; optional): CSS style options for brand.
- brand_external_link (boolean; optional): If true, the browser will treat the brand link as external,
forcing a page refresh at the new location. If false,
this just changes the location without triggering a page
refresh. Use this if you are observing dcc.Location, for
instance. Defaults to true for absolute URLs and false
otherwise.
- fluid (boolean; default False): The contents of the Navbar are wrapped in a container, use fluid=True to
make this container fluid, so that in particular, the contents of the
navbar fill the available horizontal space.
- light (boolean; default True): Applies the `navbar-light` class to the NavbarSimple, causing text in the
children of the Navbar to use dark colors for contrast / visibility.
- dark (boolean; optional): Applies the `navbar-dark` class to the NavbarSimple, causing text in the
children of the Navbar to use light colors for contrast / visibility.
- fixed (string; optional): Fix the navbar's position at the top or bottom of the page, options: top,
bottom
- sticky (string; optional): Stick the navbar to the top or the bottom of the viewport, options: top, bottom

With `sticky`, the navbar remains in the viewport when you scroll. By
contrast, with `fixed`, the navbar will remain at the top or bottom of
the page.
- color (string; default 'light'): Sets the color of the NavbarSimple. Main options are primary, light and dark, default light.

You can also choose one of the other contextual classes provided by Bootstrap
(secondary, success, warning, danger, info, white) or any valid CSS color of
your choice (e.g. a hex code, a decimal code or a CSS color name)
- expand (boolean | string; default 'md'): Specify breakpoint at which to expand the menu bar. Options are: 'xs',
'sm', 'md', 'lg', or 'xl'. Below this breakpoint the navbar will collapse
and navitems will be placed in a togglable collapse element.
- loading_state (dict; optional): Object that holds the loading state object coming from dash-renderer. loading_state has the following type: dict containing keys 'is_loading', 'prop_name', 'component_name'.
Those keys have the following types:
  - is_loading (boolean; optional): Determines if the component is loading or not
  - prop_name (string; optional): Holds which property is loading
  - component_name (string; optional): Holds the name of the component that is loading"""
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, style=Component.UNDEFINED, className=Component.UNDEFINED, key=Component.UNDEFINED, brand=Component.UNDEFINED, brand_href=Component.UNDEFINED, brand_style=Component.UNDEFINED, brand_external_link=Component.UNDEFINED, fluid=Component.UNDEFINED, light=Component.UNDEFINED, dark=Component.UNDEFINED, fixed=Component.UNDEFINED, sticky=Component.UNDEFINED, color=Component.UNDEFINED, expand=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'style', 'className', 'key', 'brand', 'brand_href', 'brand_style', 'brand_external_link', 'fluid', 'light', 'dark', 'fixed', 'sticky', 'color', 'expand', 'loading_state']
        self._type = 'NavbarSimple'
        self._namespace = 'dash_bootstrap_components'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'style', 'className', 'key', 'brand', 'brand_href', 'brand_style', 'brand_external_link', 'fluid', 'light', 'dark', 'fixed', 'sticky', 'color', 'expand', 'loading_state']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(NavbarSimple, self).__init__(children=children, **args)
