window.onload = ()=>{
    console.log("loading 되었음!")
    // setTimeout(handleSignin, 10000);
}
    
// setTimeout((handleSignin)=>console.log("timeout"), 5000);
async function handleSignin(){
    
    const email = document.getElementById("email").value
    const password = document.getElementById("password").value
    console.log(email, password)
    
    
    const response = await fetch('http://127.0.0.1:8000/users/signup/', {
        headers:{
            'content-type':'application/json',
        },
        method:'POST',
        body: JSON.stringify({
            "email": email,
            "password": password
        })
    })
    // sleep(5000);
    console.log(response)
}