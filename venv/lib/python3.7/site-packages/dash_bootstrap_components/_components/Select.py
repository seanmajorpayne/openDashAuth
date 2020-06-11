# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Select(Component):
    """A Select component.
Create a HTML select element with Bootstrap styles. Specify options as a
list of dictionaries with keys label, value and disabled.

Keyword arguments:
- id (string; optional): The ID of this component, used to identify dash components
in callbacks. The ID needs to be unique across all of the
components in an app.
- style (dict; optional): Defines CSS styles which will override styles previously set.
- className (string; optional): Often used with CSS to style elements with common properties.
- key (string; optional): A unique identifier for the component, used to improve
performance by React.js while rendering components
See https://reactjs.org/docs/lists-and-keys.html for more info
- value (string | number; default ''): The value of the currently selected option.
- options (list; optional): An array of options for the select
- disabled (boolean; optional): Set to True to disable the Select.
- valid (boolean; optional): Apply valid style to the Input for feedback purposes. This will cause
any FormFeedback in the enclosing FormGroup with valid=True to display.
- invalid (boolean; optional): Apply invalid style to the Input for feedback purposes. This will cause
any FormFeedback in the enclosing FormGroup with valid=False to display.
- bs_size (string; optional): Set the size of the Input. Options: 'sm' (small), 'md' (medium)
or 'lg' (large). Default is 'md'.
- persistence (boolean | string | number; optional): Used to allow user interactions in this component to be persisted when
the component - or the page - is refreshed. If `persisted` is truthy and
hasn't changed from its previous value, a `value` that the user has
changed while using the app will keep that change, as long as
the new `value` also matches what was given originally.
Used in conjunction with `persistence_type`.
- persisted_props (list of a value equal to: 'value's; default ['value']): Properties whose user interactions will persist after refreshing the
component or the page. Since only `value` is allowed this prop can
normally be ignored.
- persistence_type (a value equal to: 'local', 'session', 'memory'; default 'local'): Where persisted user changes will be stored:
memory: only kept in memory, reset on page refresh.
local: window.localStorage, data is kept after the browser quit.
session: window.sessionStorage, data is cleared once the browser quit."""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, style=Component.UNDEFINED, className=Component.UNDEFINED, key=Component.UNDEFINED, value=Component.UNDEFINED, options=Component.UNDEFINED, disabled=Component.UNDEFINED, valid=Component.UNDEFINED, invalid=Component.UNDEFINED, bs_size=Component.UNDEFINED, persistence=Component.UNDEFINED, persisted_props=Component.UNDEFINED, persistence_type=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'style', 'className', 'key', 'value', 'options', 'disabled', 'valid', 'invalid', 'bs_size', 'persistence', 'persisted_props', 'persistence_type']
        self._type = 'Select'
        self._namespace = 'dash_bootstrap_components'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'style', 'className', 'key', 'value', 'options', 'disabled', 'valid', 'invalid', 'bs_size', 'persistence', 'persisted_props', 'persistence_type']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(Select, self).__init__(**args)
