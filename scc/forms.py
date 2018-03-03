
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout,Fieldset
from crispy_forms.bootstrap import InlineField, FormActions, StrictButton


class CorrespondenciaListFormHelper(FormHelper):
    form_id = 'correspondencia-search-form'
    form_class = 'form-inline'
    field_template = 'bootstrap4/layout/inline_field.html'
    field_class = 'col-xs-3'
    label_class = 'col-xs-3'
    form_show_errors = True
    help_text_inline = False
    html5_required = True
    layout = Layout(
                Fieldset(
                    '<i class="fa fa-search"></i> Search Correspondencia Records',
                    InlineField('correspondencia_oficio'),
                    InlineField('corresponedencia_fecha_recibido')
                ),
                FormActions(
                    StrictButton(
                        '<i class="fa fa-search"></i> Search',
                        type='submit',
                        css_class='btn-primary',
                        style='margin-top:10px;')
                )
)