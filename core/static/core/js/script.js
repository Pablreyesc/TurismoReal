function sendPago()
{
   let form=document.form_pagar;
   form.submit();
}


function validacion()
{
   var nombre, apellido, usuario, contrasena;
   nombre = document.getElementById('txtNombre');
   apellido = document.getElementById('txtApellido');
   usuario = document.getElementById('txtUsuario');
   contrasena = document.getElementById('txtPass');
   if(nombre === "" || apellido === "" || usuario === "" || contrasena ===""){
      alert("Todos los campos son obligatorios");
      return false;
   }
   else if (nombre.length<3) {
      alert("El nombre debe contener mas de 3 caracteres");
      return false;
   }
   else if (apellido.length<3) {
      alert("El apellido debe contener mas de 3 caracteres");
      return false;
   }
   else if (usuario.length<3) {
      alert("El usuario debe contener mas de 3 caracteres");
      return false;
   }
   else if (contrasena.length<3) {
      alert("La contraseña debe contener mas de 3 caracteres");
      return false;
   }


}

const $txtNombre = document.getElementById('txtNombre');