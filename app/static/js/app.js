
var mymodal = new bootstrap.Modal(document.getElementById('myModal'));
var mymodal2 = new bootstrap.Modal(document.getElementById('myModal2'));
let frm = document.getElementById('myForm');
document.addEventListener('DOMContentLoaded', function () {
    var calendarEl = document.getElementById('calendar');
    var calendar = new FullCalendar.Calendar(calendarEl, {
        themeSystem: 'standard',
        initialView: 'dayGridMonth',
        locale: 'es',
        headerToolbar: {
            left: 'prev next today',
            center: 'title',
            right: 'dayGridMonth timeGridWeek listWeek'
        },
        events: '/events/list',
        dateClick: function (info){
            frm.reset();
            //eliminar.classList.add('d-none');
            //document.getElementById('start').value = info.dateStr;
            
            document.getElementById('btnAccion').textContent = 'Registrar';
            document.getElementById('staticBackdropLabel').textContent = 'Registrar horario del Partido';
            mymodal.show();
        },
        eventClick: function(info) {
            //var event = calendar.getEventById('11') // an event object!

            document.getElementById('title2').innerHTML = info.event.title;
            document.getElementById('start2').innerHTML = info.event.start;
            //document.getElementById('end2').innerHTML = info.event.end;
            document.getElementById('idEvent').value = info.event.id;
            //document.getElementById('start').value = info.dateStr+' 00:00';
            //document.getElementById('staticBackdropLabel').textContent = 'Modificar Evento';
            document.getElementById('btnDelete').textContent = 'Eliminar';
            //jQuery('.eventUrl').attr('href',event.url);
            mymodal2.show();
        },
    });
    calendar.render();
    frm.addEventListener('submit', function (e) {
        e.preventDefault();
        var title = $('#title').val();
        var start = $('#start').val();
        var color = $('#color').val();
        if (title == '' || start == '' || color == '') {
            Swal.fire(
                'Aviso',
                'Todos los campos son requeridos',
                'warning'
            )
        } else {
            const url = '/events/store';
            const http = new XMLHttpRequest();
            http.open('POST', url, true);
            http.send(new FormData(frm));
            http.onreadystatechange = function () {
                if (this.readyState == 4 && this.status == 200) {
                    console.log(this.responseText);
                    const respuesta = JSON.parse(this.responseText);
                    console.log(respuesta);
                    if (respuesta.estado) {
                        calendar.refetchEvents();
                    }
                    mymodal.hide();
                    Swal.fire(
                        'Aviso',
                        respuesta.msg,
                        respuesta.tipo
                    )
                }
            }
        }
    })
});