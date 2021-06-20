
//Reference the DropDownList.
var ddlYears2 = document.getElementById("ddlYears2");
//Determine the Current Year.
var currentYear = (new Date()).getFullYear();
//Loop and add the Year values to DropDownList.
for (var i = 1950; i <= currentYear; i++) {
    var option = document.createElement("OPTION");
    option.innerHTML = i+1;
    option.value = i+1;
    ddlYears2.appendChild(option);
}


