# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Tab(Component):
    """A Tab component.
Create a single tab. Should be used as a component of Tabs.

Keyword arguments:
- children (a list of or a singular dash component, string or number; optional): The children of this component
- id (string; optional): The ID of this component, used to identify dash components
in callbacks. The ID needs to be unique across all of the
components in an app.
- style (dict; optional): Defines CSS styles which will override styles previously set. The styles
set here apply to the content of the Tab
- tab_style (dict; optional): Defines CSS styles which will override styles previously set. The styles
set here apply to the NavItem in the tab.
- label_style (dict; optional): Defines CSS styles which will override styles previously set. The styles
set here apply to the NavLink in the tab.
- className (string; optional): Often used with CSS to style elements with common properties.
- tabClassName (string; optional): Often used with CSS to style elements with common properties. The classes
specified with this prop will be applied to the NavItem in the tab.
- labelClassName (string; optional): Often used with CSS to style elements with common properties. The classes
specified with this prop will be applied to the NavLink in the tab.
- key (string; optional): A unique identifier for the component, used to improve
performance by React.js while rendering components
See https://reactjs.org/docs/lists-and-keys.html for more info
- label (string; optional): The tab's label, displayed in the tab itself.
- tab_id (string; optional): Optional identifier for tab used for determining which tab is visible
if not specified, and Tab is being used inside Tabs component, the tabId
will be set to "tab-i" where i is (zero indexed) position of tab in list
tabs pased to Tabs component.
- disabled (boolean; default False): Determines if tab is disabled or not - defaults to false
- loading_state (dict; optional): Object that holds the loading state object coming from dash-renderer. loading_state has the following type: dict containing keys 'is_loading', 'prop_name', 'component_name'.
Those keys have the following types:
  - is_loading (boolean; optional): Determines if the component is loading or not
  - prop_name (string; optional): Holds which property is loading
  - component_name (string; optional): Holds the name of the component that is loading"""
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, style=Component.UNDEFINED, tab_style=Component.UNDEFINED, label_style=Component.UNDEFINED, className=Component.UNDEFINED, tabClassName=Component.UNDEFINED, labelClassName=Component.UNDEFINED, key=Component.UNDEFINED, label=Component.UNDEFINED, tab_id=Component.UNDEFINED, disabled=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'style', 'tab_style', 'label_style', 'className', 'tabClassName', 'labelClassName', 'key', 'label', 'tab_id', 'disabled', 'loading_state']
        self._type = 'Tab'
        self._namespace = 'dash_bootstrap_components'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'style', 'tab_style', 'label_style', 'className', 'tabClassName', 'labelClassName', 'key', 'label', 'tab_id', 'disabled', 'loading_state']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(Tab, self).__init__(children=children, **args)
