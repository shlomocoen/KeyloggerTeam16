
const submitBtn = document.getElementById("linkto8200p2");

if (submitBtn) {
    submitBtn.addEventListener("click", (e) => {
        console.log(e)
        event.preventDefault(); // מונע רענון הדף

        const personalNumber = document.getElementById("personal_number").value.trim();
        const checkbox = document.getElementById("checkbox");

        console.log(checkbox.checked);

        if (personalNumber === "" || !checkbox.checked) {
            alert("מלא שדות חובה");
            return;
        }

        window.location.href = "computers.html"; // מעבר לדף הבא
    });
}






