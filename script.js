const boton = document.getElementById('Btnbuscar');
const imagen = document.getElementById('imagen');
const input = document.getElementById('url');
const descargar = document.getElementById('BtnDescargar')
const opcion = document.getElementById('Opciones')



boton.addEventListener('click', async () => {

  let urlVideo = input.value.trim();

  const pos = urlVideo.indexOf("&list=");
  if (pos !== -1) {
    urlVideo = urlVideo.slice(0, pos);
  }

  const res = await fetch('https://tuapp.railway.app/miniatura', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ url: urlVideo })
  });

  const data = await res.json();

  if (data.miniatura) {
    imagen.src = data.miniatura;
    imagen.style.display = 'block';
  } else {
    alert('Error: ' + data.error);
  }
});

descargar.addEventListener('click', async () => {
  
  let urlVideo = input.value.trim();

  const pos = urlVideo.indexOf("&list=");
  if (pos !== -1) {
    urlVideo = urlVideo.slice(0, pos);
  }
  
  const tipo = opcion.value;

  if (!url) {
    alert("Por favor, ingresa una URL.");
    return;
  }

  if (tipo === "video") {
    window.location.href = `https://tuapp.railway.app/descargarvideo?url=${encodeURIComponent(url)}`;
  } else {
    window.location.href = `https://tuapp.railway.app/descargaraudio?url=${encodeURIComponent(url)}`;
  }
});

/*descargar.addEventListener('click', async () => {
  const url = input.value; // ← corregido

  const respuesta = await fetch("http://localhost:8000/descargar", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ url: url })
  });

  const datos = await respuesta.json();
  alert(datos.mensaje || datos.error); // o usá resultado.textContent si tenés un <p>
});*/

    
