// register
function register() {
    var u = document.getElementById("user").value;
    var p = document.getElementById("pass").value;
    localStorage.setItem("user", u);
    localStorage.setItem("pass", p);
    alert("Account created successfully!");
    window.location.href = "login.html";
}
// login 
function login() {
    var u = document.getElementById("user").value;
    var p = document.getElementById("pass").value;
    var su = localStorage.getItem("user");
    var sp = localStorage.getItem("pass");
    if (u === su && p === sp) {
        window.location.href = "home.html";
    } else {
        alert("Wrong username or password");
    }
}
// logout
function logout() {
    window.location.href = "login.html";
}
// update serv
function updateServices() {
    var doctor = document.getElementById("doctor");
    var service = document.getElementById("service");
    if (!doctor || !service) return;
    var d = doctor.value;
    service.innerHTML = "";
    if (d === "Dr. Lusine Qablan") {
        service.innerHTML += "<option>Teeth Cleaning - 20 JD</option>";
        service.innerHTML += "<option>Kids Tooth Extraction - 25 JD</option>";
        service.innerHTML += "<option>Dental Checkup - 15 JD</option>";
    }
    if (d === "Dr. Tareq Amare") {
        service.innerHTML += "<option>Root Canal Treatment - 50 JD</option>";
        service.innerHTML += "<option>Re-Root Canal Treatment - 60 JD</option>";
        service.innerHTML += "<option>Molar Extraction - 35 JD</option>";
        service.innerHTML += "<option>Pain Examination - 20 JD</option>";
    }
    if (d === "Dr. Rame Mohammed") {
        service.innerHTML += "<option>Orthodontic Checkup - 20 JD</option>";
        service.innerHTML += "<option>Braces Installation - 100 JD</option>";
        service.innerHTML += "<option>Braces Adjustment - 40 JD</option>";
        service.innerHTML += "<option>Follow-up - 15 JD</option>";
    }
    if (d === "Dr. Omar Ahmad") {
        service.innerHTML += "<option>Dental Consultation - 10 JD</option>";
    }
}
// book
function book() {
    var name = document.getElementById("name").value;
    var doctor = document.getElementById("doctor").value;
    var service = document.getElementById("service").value;
    if (name === "") {
        alert("Please enter patient name");
        return;
    }
    var apps = localStorage.getItem("apps");
    if (apps === null) {
        apps = [];
    } else {
        apps = JSON.parse(apps);
    }
    var price = Number(service.split("-")[1].replace("JD", "").trim());
    var obj = {
        name: name,
        doctor: doctor,
        service: service,
        price: price
    };
    apps.push(obj);
    localStorage.setItem("apps", JSON.stringify(apps));
    alert("Appointment booked successfully!");
    document.getElementById("name").value = "";
    loadApps();
}
// show mawa3ed
function loadApps() {
    var apps = localStorage.getItem("apps");
    var list = document.getElementById("list");
    if (!list) return;
    if (apps === null) {
        apps = [];
    } else {
        apps = JSON.parse(apps);
    }
    list.innerHTML = "";
    for (var i = 0; i < apps.length; i++) {
        list.innerHTML += "<div class='card'>" +
            "<b>Patient:</b> " + apps[i].name + "<br>" +
            "<b>Doctor:</b> " + apps[i].doctor + "<br>" +
            "<b>Service:</b> " + apps[i].service +
            "</div>";
    }
}
// report
function loadReports() {
    var apps = localStorage.getItem("apps");
    if (apps === null) {
        apps = [];
    } else {
        apps = JSON.parse(apps);
    }
    var total = 0;
    for (var i = 0; i < apps.length; i++) {
        total += apps[i].price;
    }
    var p = document.getElementById("p");
    var r = document.getElementById("r");
    if (p) p.innerText = "Total Patients: " + apps.length;
    if (r) r.innerText = "Total Revenue: " + total + " JD";
}
// Reset
function clearAppointments() {
    localStorage.removeItem("apps");
    alert("All appointments cleared!");
    window.location.reload();
}
// run auto
loadApps();
loadReports();