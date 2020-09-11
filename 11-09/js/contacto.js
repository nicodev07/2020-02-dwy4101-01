$(document).ready(function () {
    $('form[name="formContacto"]')
        .validate({
            rules: {
                txtNombre: {
                    required: true
                },
                txtEmail: {
                    required: true,
                    email: true
                }
            },
            messages: {
                txtNombre: {
                    required: 'El campo del nombre es requerido'
                },
                txtEmail: {
                    required: 'El campo del correo es requerido',
                    email: 'El campo del correo no tiene un formato válido de correo'
                }
            }
        })
})