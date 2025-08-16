document.getElementById('form02').addEventListener('submit', function(event) {
    event.preventDefault(); // Evita el envío por defecto del formulario

    const nombre = document.getElementById('nombre').value;
    const email = document.getElementById('email').value;
    const mensaje = document.getElementById('mensaje').value;

    fetch('/contacto', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ nombre, email, mensaje }),
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert('Mensaje enviado correctamente');
        } else {
            alert('Error: ' + data.message);
        }
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});
