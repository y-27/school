function validate(){
    a = document.getElementById("name")
    if(a.value==""){
        span_name.innerHTML="enter your name"
        span_name.style.color = "red"
        return false
    }
    

   b = document.getElementById("phone")
if(b.value.match(/^[1-9][0-9]{9}$/)==null){
    span_no.innerHTML="enter your num"
    span_no.style.color="red"
    return false

}


   c = document.getElementById("email")
   if(c.value.match(/^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|.(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
   )==null){
    span_email.innerHTML="enter mail"
    span_email.style.color="red"
    return false
}

   d = document.getElementById("address")
   if(d.value==""){
    span_address.innerHTML = "enter address"
    span_address.style.color = "red"
    return false
   }

span_messege = document.getElementById("span_messege")
   e = document.getElementById("message")
   if(e.value==""){
    span_messege.innerHTML = "enter address"
    span_messege.style.color = "red"
    return false
   }

}