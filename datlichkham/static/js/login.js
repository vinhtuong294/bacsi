var slideIndex = 0;
showSlides();

function showSlides () {
    var i;
    var slides = document.getElementsByClassName("slide");
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    slideIndex++;
    if (slideIndex > slides.length) { slideIndex = 1 }
    slides[slideIndex - 1].style.display = "block";
    setTimeout(showSlides, 3000); // Đổi ảnh sau mỗi 2 giây
}

document.getElementById("loginForm").addEventListener("submit", function (event) {
    event.preventDefault(); // Prevent default form submission

    // Fetch the input values
    var u = document.getElementById("username").value;
    var p = document.getElementById("password").value;
    console.log("username: ", u);
    console.log("password: ", p);

    // Make a POST request to the authentication API endpoint
    fetch("http://localhost:8080/api/auth/authenticate", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            username: u,
            password: p
        })
    })
        .then(response => {
            if (!response.ok) {
                alert("Tên tài khoản hoặc mật khẩu không chính xác!");
                throw new Error("Failed to authenticate");
            }
            return response.json();
        })
        .then(data => {
            alert("Đăng nhập thành công!");
            window.location.href = "http://localhost:8080/home";
            console.log("Authentication successful:", data);
        })
        .catch(error => {
            // show diaglog error
            alert("Đã có lỗi xảy ra, vui lòng thử lại sau!");
            console.error("Authentication error:", error.message);
        });
});