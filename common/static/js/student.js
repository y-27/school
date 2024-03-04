function validate(){
    a = document.getElementById("name")
    if(a.value==""){
        span_name.innerHTML="enter your name"
        span_name.style.color = "red"
        return false
    }

    b = document.getElementById("password")
    if(b.value==""){
        span_password.innerHTML = "enter ur num"
        span_password.style.color = "red"
        return false
    }
}