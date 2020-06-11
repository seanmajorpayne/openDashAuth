# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Textarea(Component):
    """A Textarea component.
A basic HTML textarea for entering multiline text based on the corresponding
component in dash-core-components

Keyword arguments:
- id (string; optional): The ID of this component, used to identify dash components
in callbacks. The ID needs to be unique across all of the
components in an app.
- key (string; optional): A unique identifier for the component, used to improve
performance by React.js while rendering components
See https://reactjs.org/docs/lists-and-keys.html for more info
- value (string; default ''): The value of the textarea
- autoFocus (string; optional): The element should be automatically focused after the page loaded.
- cols (string | number; optional): Defines the number of columns in a textarea.
- disabled (string | boolean; optional): Indicates whether the user can interact with the element.
- form (string; optional): Indicates the form that is the owner of the element.
- maxLength (string | number; optional): Defines the maximum number of characters allowed in the element.
- minLength (string | number; optional): Defines the minimum number of characters allowed in the element.
- name (string; optional): Name of the element. For example used by the server to identify the fields in form submits.
- placeholder (string; optional): Provides a hint to the user of what can be entered in the field.
- readOnly (boolean | a value equal to: 'readOnly', 'readonly', 'READONLY'; optional): Indicates whether the element can be edited.
- required (a value equal to: 'required', 'REQUIRED' | boolean; optional): Indicates whether this element is required to fill out or not.
- rows (string | number; optional): Defines the number of rows in a text area.
- wrap (string; optional): Indicates whether the text should be wrapped.
- accessKey (string; optional): Defines a keyboard shortcut to activate or add focus to the element.
- className (string; optional): Often used with CSS to style elements with common properties.
- contentEditable (string | number; optional): Indicates whether the element's content is editable.
- contextMenu (string; optional): Defines the ID of a <menu> element which will serve as the element's context menu.
- dir (string; optional): Defines the text direction. Allowed values are ltr (Left-To-Right) or rtl (Right-To-Left)
- draggable (a value equal to: 'true', 'false' | boolean; optional): Defines whether the element can be dragged.
- hidden (string; optional): Prevents rendering of given element, while keeping child elements, e.g. script elements, active.
- lang (string; optional): Defines the language used in the element.
- spellCheck (a value equal to: 'true', 'false' | boolean; optional): Indicates whether spell checking is allowed for the element.
- style (dict; optional): Defines CSS styles which will override styles previously set.
- tabIndex (string | number; optional): Overrides the browser's default tab order and follows the one specified instead.
- title (string; optional): Text to be displayed in a tooltip when hovering over the element.
- bs_size (string; optional): Set the size of the Textarea, valid options are 'sm', 'md', or 'lg'
- valid (boolean; optional): Apply valid style to the Textarea for feedback purposes. This will cause
any FormFeedback in the enclosing FormGroup with valid=True to display.
- invalid (boolean; optional): Apply invalid style to the Textarea for feedback purposes. This will cause
any FormFeedback in the enclosing FormGroup with valid=False to display.
- n_blur (number; default 0): Number of times the input lost focus.
- n_blur_timestamp (number; default -1): Last time the input lost focus.
- n_submit (number; default 0): Number of times the `Enter` key was pressed while the textarea had focus.
- n_submit_timestamp (number; default -1): Last time that `Enter` was pressed.
- n_clicks (number; default 0): An integer that represents the number of times
that this element has been clicked on.
- n_clicks_timestamp (number; default -1): An integer that represents the time (in ms since 1970)
at which n_clicks changed. This can be used to tell
which button was changed most recently.
- debounce (boolean; default False): If true, changes to input will be sent back to the Dash server only on enter or when losing focus.
If it's false, it will sent the value back on every change.
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
- persisted_props (list of a value equal to: 'value's; default ['value']): Properties whose user interactions will persist after refreshing the
component or the page. Since only `value` is allowed this prop can
normally be ignored.
- persistence_type (a value equal to: 'local', 'session', 'memory'; default 'local'): Where persisted user changes will be stored:
memory: only kept in memory, reset on page refresh.
local: window.localStorage, data is kept after the browser quit.
session: window.sessionStorage, data is cleared once the browser quit."""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, value=Component.UNDEFINED, autoFocus=Component.UNDEFINED, cols=Component.UNDEFINED, disabled=Component.UNDEFINED, form=Component.UNDEFINED, maxLength=Component.UNDEFINED, minLength=Component.UNDEFINED, name=Component.UNDEFINED, placeholder=Component.UNDEFINED, readOnly=Component.UNDEFINED, required=Component.UNDEFINED, rows=Component.UNDEFINED, wrap=Component.UNDEFINED, accessKey=Component.UNDEFINED, className=Component.UNDEFINED, contentEditable=Component.UNDEFINED, contextMenu=Component.UNDEFINED, dir=Component.UNDEFINED, draggable=Component.UNDEFINED, hidden=Component.UNDEFINED, lang=Component.UNDEFINED, spellCheck=Component.UNDEFINED, style=Component.UNDEFINED, tabIndex=Component.UNDEFINED, title=Component.UNDEFINED, bs_size=Component.UNDEFINED, valid=Component.UNDEFINED, invalid=Component.UNDEFINED, n_blur=Component.UNDEFINED, n_blur_timestamp=Component.UNDEFINED, n_submit=Component.UNDEFINED, n_submit_timestamp=Component.UNDEFINED, n_clicks=Component.UNDEFINED, n_clicks_timestamp=Component.UNDEFINED, debounce=Component.UNDEFINED, loading_state=Component.UNDEFINED, persistence=Component.UNDEFINED, persisted_props=Component.UNDEFINED, persistence_type=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'key', 'value', 'autoFocus', 'cols', 'disabled', 'form', 'maxLength', 'minLength', 'name', 'placeholder', 'readOnly', 'required', 'rows', 'wrap', 'accessKey', 'className', 'contentEditable', 'contextMenu', 'dir', 'draggable', 'hidden', 'lang', 'spellCheck', 'style', 'tabIndex', 'title', 'bs_size', 'valid', 'invalid', 'n_blur', 'n_blur_timestamp', 'n_submit', 'n_submit_timestamp', 'n_clicks', 'n_clicks_timestamp', 'debounce', 'loading_state', 'persistence', 'persisted_props', 'persistence_type']
        self._type = 'Textarea'
        self._namespace = 'dash_bootstrap_components'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'value', 'autoFocus', 'cols', 'disabled', 'form', 'maxLength', 'minLength', 'name', 'placeholder', 'readOnly', 'required', 'rows', 'wrap', 'accessKey', 'className', 'contentEditable', 'contextMenu', 'dir', 'draggable', 'hidden', 'lang', 'spellCheck', 'style', 'tabIndex', 'title', 'bs_size', 'valid', 'invalid', 'n_blur', 'n_blur_timestamp', 'n_submit', 'n_submit_timestamp', 'n_clicks', 'n_clicks_timestamp', 'debounce', 'loading_state', 'persistence', 'persisted_props', 'persistence_type']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(Textarea, self).__init__(**args)
