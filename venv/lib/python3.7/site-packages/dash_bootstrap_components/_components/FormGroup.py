# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FormGroup(Component):
    """A FormGroup component.
A component for grouping together inputs, labels, text and feedback.

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
- row (boolean; optional): Apply row class to FormGroup to allow labels and inputs to be displayed
horizontally in a row.
- check (boolean; optional): Apply `form-check` class instead of `form-group`. Useful when positioning
labels with checkbox / radio inputs. Usually it will be better to use the
pre-built dbc.Checklist or dbc.RadioItems components.
- inline (boolean; optional): If check is True, apply the `form-check-inline` class in addition to
`form-check`. If you want to make an inline list of checkboxes / radios
we recommend using either dbc.Checklist or dbc.RadioItems with inline=True

This prop has no effect if check=False.
- loading_state (dict; optional): Object that holds the loading state object coming from dash-renderer. loading_state has the following type: dict containing keys 'is_loading', 'prop_name', 'component_name'.
Those keys have the following types:
  - is_loading (boolean; optional): Determines if the component is loading or not
  - prop_name (string; optional): Holds which property is loading
  - component_name (string; optional): Holds the name of the component that is loading"""
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, style=Component.UNDEFINED, className=Component.UNDEFINED, key=Component.UNDEFINED, row=Component.UNDEFINED, check=Component.UNDEFINED, inline=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'style', 'className', 'key', 'row', 'check', 'inline', 'loading_state']
        self._type = 'FormGroup'
        self._namespace = 'dash_bootstrap_components'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'style', 'className', 'key', 'row', 'check', 'inline', 'loading_state']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(FormGroup, self).__init__(children=children, **args)
