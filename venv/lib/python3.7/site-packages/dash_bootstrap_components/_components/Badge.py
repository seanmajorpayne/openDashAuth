# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Badge(Component):
    """A Badge component.
Badges can be used to add counts or labels to other components.

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
- color (string; optional): Badge color, options: primary, secondary, success, info, warning, danger,
link. Default: secondary.
- pill (boolean; optional): Make badge "pill" shaped (rounded ends, like a pill). Default: False.
- href (string; optional): Attach link to badge.
- tag (string; optional): HTML tag to use for the Badge. Default: span.
- loading_state (dict; optional): Object that holds the loading state object coming from dash-renderer. loading_state has the following type: dict containing keys 'is_loading', 'prop_name', 'component_name'.
Those keys have the following types:
  - is_loading (boolean; optional): Determines if the component is loading or not
  - prop_name (string; optional): Holds which property is loading
  - component_name (string; optional): Holds the name of the component that is loading
- external_link (boolean; optional): If true, the browser will treat this as an external link,
forcing a page refresh at the new location. If false,
this just changes the location without triggering a page
refresh. Use this if you are observing dcc.Location, for
instance. Defaults to true for absolute URLs and false
otherwise.
- n_clicks (number; default 0): An integer that represents the number of times
that this element has been clicked on.
- n_clicks_timestamp (number; default -1): An integer that represents the time (in ms since 1970)
at which n_clicks changed. This can be used to tell
which button was changed most recently.
- target (string; optional): Target attribute to pass on to the link. Only applies to external links."""
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, style=Component.UNDEFINED, className=Component.UNDEFINED, key=Component.UNDEFINED, color=Component.UNDEFINED, pill=Component.UNDEFINED, href=Component.UNDEFINED, tag=Component.UNDEFINED, loading_state=Component.UNDEFINED, external_link=Component.UNDEFINED, n_clicks=Component.UNDEFINED, n_clicks_timestamp=Component.UNDEFINED, target=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'style', 'className', 'key', 'color', 'pill', 'href', 'tag', 'loading_state', 'external_link', 'n_clicks', 'n_clicks_timestamp', 'target']
        self._type = 'Badge'
        self._namespace = 'dash_bootstrap_components'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'style', 'className', 'key', 'color', 'pill', 'href', 'tag', 'loading_state', 'external_link', 'n_clicks', 'n_clicks_timestamp', 'target']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(Badge, self).__init__(children=children, **args)
