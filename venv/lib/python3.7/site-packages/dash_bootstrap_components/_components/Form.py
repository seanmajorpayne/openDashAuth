# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Form(Component):
    """A Form component.
The Form component can be used to organise collections of input components
and apply consistent styling.

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
- inline (boolean; optional): Use inline=True to apply the `form-inline` class, allowing you to display
a series of labels, form controls, and buttons on a single horizontal row.
Form controls within inline forms vary slightly from their default states.
- n_submit (number; default 0): Number of times the `Enter` key was pressed while the input had focus.
- n_submit_timestamp (number; default -1): Last time that `Enter` was pressed.
- prevent_default_on_submit (boolean; default True): The form calls preventDefault on submit events. Use submit_allow_default
to override this and not call preventDefault on submit.
- loading_state (dict; optional): Object that holds the loading state object coming from dash-renderer. loading_state has the following type: dict containing keys 'is_loading', 'prop_name', 'component_name'.
Those keys have the following types:
  - is_loading (boolean; optional): Determines if the component is loading or not
  - prop_name (string; optional): Holds which property is loading
  - component_name (string; optional): Holds the name of the component that is loading"""
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, style=Component.UNDEFINED, className=Component.UNDEFINED, key=Component.UNDEFINED, inline=Component.UNDEFINED, n_submit=Component.UNDEFINED, n_submit_timestamp=Component.UNDEFINED, prevent_default_on_submit=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'style', 'className', 'key', 'inline', 'n_submit', 'n_submit_timestamp', 'prevent_default_on_submit', 'loading_state']
        self._type = 'Form'
        self._namespace = 'dash_bootstrap_components'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'style', 'className', 'key', 'inline', 'n_submit', 'n_submit_timestamp', 'prevent_default_on_submit', 'loading_state']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(Form, self).__init__(children=children, **args)
