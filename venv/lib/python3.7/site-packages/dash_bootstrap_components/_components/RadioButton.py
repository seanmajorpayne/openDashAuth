# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class RadioButton(Component):
    """A RadioButton component.
Creates a single radio button. Use the `checked` prop in your callbacks.

Keyword arguments:
- id (string; optional): The ID of this component, used to identify dash components in callbacks.
The ID needs to be unique across all of the components in an app.
- checked (boolean; default False): Whether RadioButton has been checked or not
- className (string; optional): The class of the container (div)
- style (dict; optional): The style of the container (div)
- key (string; optional): A unique identifier for the component, used to improve
performance by React.js while rendering components
See https://reactjs.org/docs/lists-and-keys.html for more info
- loading_state (dict; optional): Object that holds the loading state object coming from dash-renderer. loading_state has the following type: dict containing keys 'is_loading', 'prop_name', 'component_name'.
Those keys have the following types:
  - is_loading (boolean; optional): Determines if the component is loading or not
  - prop_name (string; optional): Holds which property is loading
  - component_name (string; optional): Holds the name of the component that is loading
- persistence (boolean | string | number; optional): Used to allow user interactions in this component to be persisted when
the component - or the page - is refreshed. If `persisted` is truthy and
hasn't changed from its previous value, a `value` that the user has
changed while using the app will keep that change, as long as
the new `value` also matches what was given originally.
Used in conjunction with `persistence_type`.
- persisted_props (list of a value equal to: 'checked's; default ['checked']): Properties whose user interactions will persist after refreshing the
component or the page. Since only `value` is allowed this prop can
normally be ignored.
- persistence_type (a value equal to: 'local', 'session', 'memory'; default 'local'): Where persisted user changes will be stored:
memory: only kept in memory, reset on page refresh.
local: window.localStorage, data is kept after the browser quit.
session: window.sessionStorage, data is cleared once the browser quit."""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, checked=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, key=Component.UNDEFINED, loading_state=Component.UNDEFINED, persistence=Component.UNDEFINED, persisted_props=Component.UNDEFINED, persistence_type=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'checked', 'className', 'style', 'key', 'loading_state', 'persistence', 'persisted_props', 'persistence_type']
        self._type = 'RadioButton'
        self._namespace = 'dash_bootstrap_components'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'checked', 'className', 'style', 'key', 'loading_state', 'persistence', 'persisted_props', 'persistence_type']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(RadioButton, self).__init__(**args)
