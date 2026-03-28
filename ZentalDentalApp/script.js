// this variable helps us know if we are adding a new appointment
// or editing an existing one
var editIndex = -1;


// Register Function
function register() {
    var u = document.getElementById("user").value;
    var p = document.getElementById("pass").value;

    if (u === "" || p === "") {
        alert("Please fill in all fields");
        return;
    }

    localStorage.setItem("user", u);
    localStorage.setItem("pass", p);

    alert("Account created successfully!");
    window.location.href = "login.html";
}


// Login Function
function login() {
    var u = document.getElementById("user").value;
    var p = document.getElementById("pass").value;

    var savedUser = localStorage.getItem("user");
    var savedPass = localStorage.getItem("pass");

    if (u === savedUser && p === savedPass) {
        window.location.href = "home.html";
    } else {
        alert("Wrong username or password");
    }
}


// Logout Function
function logout() {
    window.location.href = "login.html";
}


// Update Services Function
function updateServices(selectedService) {
    var doctor = document.getElementById("doctor");
    var service = document.getElementById("service");

    if (!doctor || !service) {
        return;
    }

    var selectedDoctor = doctor.value;
    service.innerHTML = "";

    if (selectedDoctor === "Dr. Lusine Qablan") {
        service.innerHTML += "<option>Teeth Cleaning - 20 JD</option>";
        service.innerHTML += "<option>Kids Tooth Extraction - 25 JD</option>";
        service.innerHTML += "<option>Dental Checkup - 15 JD</option>";
    }

    if (selectedDoctor === "Dr. Tareq Amare") {
        service.innerHTML += "<option>Root Canal Treatment - 50 JD</option>";
        service.innerHTML += "<option>Re-Root Canal Treatment - 60 JD</option>";
        service.innerHTML += "<option>Molar Extraction - 35 JD</option>";
        service.innerHTML += "<option>Pain Examination - 20 JD</option>";
    }

    if (selectedDoctor === "Dr. Rame Mohammed") {
        service.innerHTML += "<option>Orthodontic Checkup - 20 JD</option>";
        service.innerHTML += "<option>Braces Installation - 100 JD</option>";
        service.innerHTML += "<option>Braces Adjustment - 40 JD</option>";
        service.innerHTML += "<option>Follow-up - 15 JD</option>";
    }

    if (selectedDoctor === "Dr. Omar Ahmad") {
        service.innerHTML += "<option>Dental Consultation - 10 JD</option>";
    }

    // if we are editing, select the old service automatically
    if (selectedService) {
        service.value = selectedService;
    }
}


// Book or Update Function
function book() {
    var name = document.getElementById("name").value;
    var doctor = document.getElementById("doctor").value;
    var service = document.getElementById("service").value;
    var button = document.getElementById("mainButton");

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

    var parts = service.split("-");
    var priceText = parts[1].replace("JD", "").trim();
    var price = Number(priceText);

    var appointment = {
        name: name,
        doctor: doctor,
        service: service,
        price: price
    };

    // add new appointment
    if (editIndex === -1) {
        apps.push(appointment);
        alert("Appointment booked successfully!");
    } 
    // update old appointment
    else {
        apps[editIndex] = appointment;
        alert("Appointment updated successfully!");
        editIndex = -1;
        button.innerText = "Book Appointment";
    }

    localStorage.setItem("apps", JSON.stringify(apps));

    // clear form after save
    document.getElementById("name").value = "";
    document.getElementById("doctor").selectedIndex = 0;
    updateServices();

    loadApps();
    loadReports();
}


// Load Appointments Function
function loadApps() {
    var apps = localStorage.getItem("apps");
    var list = document.getElementById("list");

    if (!list) {
        return;
    }

    if (apps === null) {
        apps = [];
    } else {
        apps = JSON.parse(apps);
    }

    list.innerHTML = "";

    for (var i = 0; i < apps.length; i++) {
        list.innerHTML += "<div class='card'>" +
            "<p><strong>Patient:</strong> " + apps[i].name + "</p>" +
            "<p><strong>Doctor:</strong> " + apps[i].doctor + "</p>" +
            "<p><strong>Service:</strong> " + apps[i].service + "</p>" +
            "<button onclick='editAppointment(" + i + ")'>Edit</button> " +
            "<button onclick='deleteAppointment(" + i + ")'>Delete</button>" +
            "</div>";
    }
}


// Delete One Appointment
function deleteAppointment(index) {
    var apps = localStorage.getItem("apps");

    if (apps === null) {
        apps = [];
    } else {
        apps = JSON.parse(apps);
    }

    apps.splice(index, 1);

    localStorage.setItem("apps", JSON.stringify(apps));

    loadApps();
    loadReports();

    alert("Appointment deleted successfully!");
}


// Edit Appointment Using Form
function editAppointment(index) {
    var apps = localStorage.getItem("apps");

    if (apps === null) {
        apps = [];
    } else {
        apps = JSON.parse(apps);
    }

    var currentAppointment = apps[index];

    // put current data inside the form
    document.getElementById("name").value = currentAppointment.name;
    document.getElementById("doctor").value = currentAppointment.doctor;

    // update services for selected doctor
    updateServices(currentAppointment.service);

    // save the edited appointment index
    editIndex = index;

    // change button text
    document.getElementById("mainButton").innerText = "Update Appointment";

    // move screen to form
    window.scrollTo(0, 0);
}


// Load Reports Function
function loadReports() {
    var apps = localStorage.getItem("apps");
    var p = document.getElementById("p");
    var r = document.getElementById("r");

    if (!p || !r) {
        return;
    }

    if (apps === null) {
        apps = [];
    } else {
        apps = JSON.parse(apps);
    }

    var total = 0;

    for (var i = 0; i < apps.length; i++) {
        total += apps[i].price;
    }

    p.innerText = "Total Patients: " + apps.length;
    r.innerText = "Total Revenue: " + total + " JD";
}


// run functions automatically
loadApps();
loadReports();