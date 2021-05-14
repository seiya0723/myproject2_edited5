window.addEventListener("load" , function (){ 

    let d       = new Date();
    let year    = d.getFullYear();
    let month   = ('0' + (d.getMonth() + 1)).slice(-2);
    let day     = ('0' + d.getDate()).slice(-2);
    let dt      = year + "-" + month + "-" + day + " 09:00";


    let config_dt = {
        defaultDate: dt,
        enableTime: true,
        dateFormat: "Y-m-d H:i",
        "locale": "ja"
    }

    flatpickr("#pay_dt", config_dt);
});







