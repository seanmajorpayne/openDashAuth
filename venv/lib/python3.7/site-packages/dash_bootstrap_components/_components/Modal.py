# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Modal(Component):
    """A Modal component.
Create a toggleable dialog using the Modal component. Toggle the visibility
with the `is_open` prop.

Keyword arguments:
- children (a list of or a singular dash component, string or number; optional): The children of this component
- id (string; optional): The ID of this component, used to identify dash components
in callbacks. The ID needs to be unique across all of the
components in an app.
- style (dict; optional): Defines CSS styles which will override styles previously set.
- className (string; optional): Often used with CSS to style elements with common properties.
- tag (string; optional): HTML tag to use for the Modal, default: div
- is_open (boolean; optional): Whether modal is currently open.
- centered (boolean; optional): If true, vertically center modal on page.
- scrollable (boolean; optional): It true, scroll the modal body rather than the entire modal when it is too
long to all fit on the screen.
- autoFocus (boolean; optional): Puts the focus on the modal when initialized.
- size (string; optional): Set the size of the modal. Options sm, lg, xl for small, large or extra
large sized modals, or leave undefined for default size.
- role (string; optional): The ARIA role attribute.
- labelledBy (string; optional): The ARIA labelledby attribute
- keyboard (boolean; optional): Close the modal when escape key is pressed.
- backdrop (boolean | a value equal to: 'static'; optional): Includes a modal-backdrop element. Alternatively, specify 'static' for a
backdrop which doesn't close the modal on click.
- modalClassName (string; optional): CSS class to apply to the modal.
- backdropClassName (string; optional): CSS class to apply to the backdrop.
- contentClassName (string; optional): CSS class to apply to the modal content.
- fade (boolean; optional): Set to false for a modal that simply appears rather than fades into view.
- zIndex (number | string; optional): Set the z-index of the modal. Default 1050."""
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, style=Component.UNDEFINED, className=Component.UNDEFINED, tag=Component.UNDEFINED, is_open=Component.UNDEFINED, centered=Component.UNDEFINED, scrollable=Component.UNDEFINED, autoFocus=Component.UNDEFINED, size=Component.UNDEFINED, role=Component.UNDEFINED, labelledBy=Component.UNDEFINED, keyboard=Component.UNDEFINED, backdrop=Component.UNDEFINED, modalClassName=Component.UNDEFINED, backdropClassName=Component.UNDEFINED, contentClassName=Component.UNDEFINED, fade=Component.UNDEFINED, zIndex=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'style', 'className', 'tag', 'is_open', 'centered', 'scrollable', 'autoFocus', 'size', 'role', 'labelledBy', 'keyboard', 'backdrop', 'modalClassName', 'backdropClassName', 'contentClassName', 'fade', 'zIndex']
        self._type = 'Modal'
        self._namespace = 'dash_bootstrap_components'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'style', 'className', 'tag', 'is_open', 'centered', 'scrollable', 'autoFocus', 'size', 'role', 'labelledBy', 'keyboard', 'backdrop', 'modalClassName', 'backdropClassName', 'contentClassName', 'fade', 'zIndex']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(Modal, self).__init__(children=children, **args)
