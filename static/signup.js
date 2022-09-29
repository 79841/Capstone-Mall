let birthday = document.getElementById("birthday");
let day = document.getElementsByClassName("bir");
for (e of day) {
    e.addEventListener("change", function () {
        let output = "";
        for (e of day) {
            if (e.value.length == 1) {
                e.value = "0" + e.value;
            }
            output += e.value;
        }
        birthday.value = output;
    });
}
