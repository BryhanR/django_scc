

window.onload = function(){
    loadDates();
}

function loadDates() {

    $('.date').datetimepicker({
        format: 'DD-MM-YYYY',
        defaultDate: moment(),
        icons: {
            time: "fa fa-clock-o",
            date: "fa fa-calendar",
            up: "fa fa-arrow-up",
            down: "fa fa-arrow-down"
        }
    });

        $('.opened_calendar').datepicker({
        language: "es",
            todayHighlight: true
    });

}

